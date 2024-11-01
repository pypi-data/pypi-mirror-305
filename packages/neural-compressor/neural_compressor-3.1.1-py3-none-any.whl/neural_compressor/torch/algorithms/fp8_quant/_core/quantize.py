# Copyright (c) 2024 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import habana_frameworks.torch.core as htcore
import torch
import torch.nn as nn

from .._quant_common.helper_modules import PatchedUnmeasuredModule
from .._quant_common.quant_config import get_hqt_config
from ..utils.logger import logger
from .common import UNMEASURED_MODELS, generate_model_info, mod_default_dict, parent_child_mod_dict
from .measure import load_measurements
from .scale import get_config, scale_method_mapping, scaling_methods


def patch_module(mod, qconfig, mod_dict, patched_mod=None):
    """Replaces the module with patched module according to mod_dict.

    Args:
        mod (nn.module): The module that will be replaced with a patched module that quantize the inputs/outputs.
        qconfig (ModuleExtraConfig): The quantization config object with the information how to quantize the inputs/outputs.
        mod_dict (dict): dictionary from module name to its patched module.

    Returns:
        nn.module: The new patched module after patching.
    """
    parent = parent_child_mod_dict[mod].parent
    name = parent_child_mod_dict[mod].name
    if patched_mod is None:
        patched_mod = mod_dict[mod.__class__.__name__].patched_module(mod, qconfig)
    setattr(parent, name, patched_mod)


def apply_hf_hook(module):
    """Applies hf_hook on a given module so its weights will be loaded from disk to cpu and then we can quantize it."""
    if hasattr(module, "_hf_hook"):
        module._hf_hook.pre_forward(module)
        module._hf_hook.detach_hook(module)
        delattr(module, "_hf_hook")
    if hasattr(module, "_old_forward"):
        module.forward = module._old_forward
        delattr(module, "_old_forward")


def quantize_params(mod, mod_extra_config):
    """Quantizes the weights of the given module according to the quantization info from mod_extra_config.

    Args:
        mod (nn.module): The module that its weights will be quantized.
        mod_extra_config (ModuleExtraConfig): The quantization config object with the information how to quantize the inputs/outputs.
    """
    for param_name in mod_extra_config.params:
        quantizer = mod_extra_config.params[param_name]
        param = getattr(mod, param_name)
        quantized_param = quantizer(param.to("hpu"))
        delattr(mod, param_name)
        setattr(mod, param_name, nn.Parameter(quantized_param))
        quantized_param = getattr(mod, param_name)
        quantized_param.requires_grad_(False)
        htcore.mark_step()


def prepare_model(model, qconfig, mod_list, hp_dtype=torch.float):
    """Replaces the model submodules according to the mod_list with patched quantization modules.
    Configures patched modules with the quantization/dequantization methods to apply on their input and output tensors.
    Quantizes the model parameters as they are static.

    Args:
        model (nn.module): The model to quantize.
        qconfig (dict): Dict that maps between patched module and its quantization info.
        mod_list (list): The specific submodules that will be quantized in the model.
    """
    config = get_hqt_config(model)
    patched_modules = []
    patched_module_types = set()
    with torch.no_grad():
        for name, mod in model.named_modules():
            if name in qconfig[UNMEASURED_MODELS]:
                if not config.cfg["ignore_modules_wo_measures"]:
                    patch_module(mod, None, None, PatchedUnmeasuredModule(name))
                else:
                    logger.debug("Module %s was not quantized.", name)
                continue
            # When offloading weight to disk, need to transfer the weight from disk to cpu using hf_hook
            apply_hf_hook(mod)
            if name in mod_list:
                if name in qconfig:
                    mod_extra_config = qconfig[name]
                    if not config.cfg["fake_quant"]:
                        quantize_params(mod, mod_extra_config)
                else:
                    # patched module without measure/quant
                    mod_extra_config = None
                patch_module(mod, mod_extra_config, mod_default_dict)
                patched_modules.append(name)
                patched_module_types.add(type(mod))
    logger.debug("Patched module types: %s", patched_module_types)
    logger.debug("Patched modules: %s", patched_modules)
    logger.debug("Total patched modules: %d", len(patched_modules))
    model = model.to("hpu")
    htcore.mark_step()


def quantize(model, mod_list):
    """Builds quantization config object that contains for each submodule its quantization functions as preparation for quantization.

    Args:
        model (nn.module): The model that will be quantized.
        mod_list (list, optional): The specific modules that will be quantized in the model.
    """
    config = get_hqt_config(model)
    generate_model_info(model)
    hp_dtype = config.cfg["hp_dtype"]
    lp_dtype = config.cfg["fp8_config"]
    measurement = {}
    scale_file = None
    use_stats_files = config.cfg["use_stats_files"]
    if use_stats_files:
        measurement = load_measurements(model, config.cfg["measure_file"])
        scale_file = config.cfg["scale_file"]
    # FIXME make sure this takes unit_scale or measured scale, from Configs
    scaling_method_name = scale_method_mapping[(config.cfg["scale_method"], config.cfg["observer"])]
    scaling_method = scaling_methods[scaling_method_name]
    params = config.cfg["scale_params"]
    params["hp_dtype"] = hp_dtype
    params["lp_dtype"] = lp_dtype
    qconfig = get_config(
        model,
        measurement,
        mod_default_dict,
        scaling_method,
        params,
        scale_file,
        mod_list,
    )
    prepare_model(model, qconfig, mod_list, hp_dtype=hp_dtype)
