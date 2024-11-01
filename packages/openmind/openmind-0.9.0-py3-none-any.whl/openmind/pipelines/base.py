# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# Copyright 2018 The HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Literal, Optional

from ..models.auto import AutoTokenizer
from ..utils import logging
from ..utils import is_transformers_available, is_mindformers_available, get_framework
from ..utils.exceptions import FrameworkNotSupportedError, PipelinePackageNotFoundError
from ..pipelines.pipeline_registry import PipelineRegistry
from .pipeline_utils import (
    download_from_repo,
    pipeline_patch,
    _get_default_model_and_revision,
    check_task,
    get_task_from_readme,
)
from ..utils.patch_utils import _apply_patches


SUPPORTED_TASK_PATCH_DICT = {
    "text-classification": {
        "model": {"pt": ("PyTorch-NPU/distilbert_base_uncased_finetuned_sst_2_english", "4e02f8e")}
    },
    "question-answering": {"model": {"pt": ("PyTorch-NPU/roberta_base_squad2", "b1c1638")}},
    "table-question-answering": {"model": {"pt": ("PyTorch-NPU/tapas_base_finetuned_wtq", "74f37f3")}},
    "fill-mask": {"model": {"pt": ("PyTorch-NPU/bert_base_uncased", "c5e6a69")}},
    "summarization": {"model": {"pt": ("PyTorch-NPU/bart_large_cnn", "6a37416")}},
    "text-generation": {"model": {"pt": ("Baichuan/Baichuan2_7b_chat_pt", "86b5fdf")}},
    "zero-shot-image-classification": {"model": {"pt": ("PyTorch-NPU/siglip_so400m_patch14_384", "94e5462")}},
    "feature-extraction": {"model": {"pt": ("PyTorch-NPU/xlnet_base_cased", "bc7408f")}},
    "depth-estimation": {"model": {"pt": ("PyTorch-NPU/dpt_large", "270fa97")}},
    "image-classification": {"model": {"pt": ("PyTorch-NPU/beit_base_patch16_224", "a46c2b5")}},
    "image-to-image": {"model": {"pt": ("PyTorch-NPU/swin2SR_classical_sr_x2_64", "407e816")}},
    "image-to-text": {"model": {"pt": ("PyTorch-NPU/blip-image-captioning-large", "059b23b")}},
    "mask-generation": {"model": {"pt": ("PyTorch-NPU/sam_vit_base", "d0ad399")}},
    "text2text-generation": {"model": {"pt": ("PyTorch-NPU/flan_t5_base", "d15ab63")}},
    "zero-shot-classification": {"model": {"pt": ("PyTorch-NPU/deberta_v3_large_zeroshot_v2.0", "d38d6f4")}},
    "zero-shot-object-detection": {"model": {"pt": ("PyTorch-NPU/owlvit_base_patch32", "ff06496")}},
    "token-classification": {"model": {"pt": ("PyTorch-NPU/camembert_ner", "1390d33")}},
    "translation": {"model": {"pt": ("PyTorch-NPU/t5_base", "68829a3")}},
    "visual-question-answering ": {"model": {"pt": ("PyTorch-NPU/blip_vqa_base", "4450392")}},
}

SUPPORTED_FRAMEWORKS = ("pt", "ms")
PIPELINE_REGISTRY = PipelineRegistry()

logger = logging.get_logger()


def pipeline(
    task: Optional[str] = None,
    model=None,
    config=None,
    tokenizer=None,
    feature_extractor=None,
    image_processor=None,
    framework: Optional[Literal["pt", "ms"]] = None,
    **kwargs,
):
    """
    Build a pipeline instance.
    Belowing docstring is mostly adapted from transformers.pipelines.pipeline

    Args:
        task:
            The task defining which pipeline will be returned.
        model:
            The model that will be used by the pipeline to make predictions.
            This can be a model identifier or an actual instance of a pretrained model.
            If not provided, the default for the `task` will be loaded.
        config:
            The configuration that will be used by the pipeline to instantiate
            the model. This can be a model identifier or an actual pretrained model
            configuration.
        tokenizer:
            The tokenizer that will be used by the pipeline to encode data for
            the model. This can be a model identifier or an actual pretrained tokenizer.
        feature_extractor:
            The feature extractor that will be used by the pipeline to encode data for
            the model. This can be a model identifier or an actual pretrained
             feature extractor.
        image_processor:
            The image_processor that will be used by the pipeline.
        framework (`str`, *optional*):
            The framework to use, either `"pt"` for PyTorch or "ms" for mindspore.
            The specified framework must be installed.
        kwargs:
            Additional keyword arguments passed along to the specific pipeline init.
            e.g. for transformers pipeline:
                revision (`str`, *optional*, defaults to `"main"`):
                    When passing a task name or a string model identifier:
                    The specific model version to use. It can be a branch name,
                    a tag name, or a commit id, since we use a git-based system for
                    storing models and other artifacts on openmind hub, so `revision`
                     can be any identifier allowed by git.
                use_fast (`bool`, *optional*, defaults to `True`):
                    Whether to use a Fast tokenizer if possible
                    (a [`PreTrainedTokenizerFast`]).
                device (`int` or `str` or `torch.device`):
                    Defines the device (*e.g.*, `"cpu"`, `"npu:0"`) on which this pipeline will be allocated.
                device_map (`str` or `Dict[str, Union[int, str, torch.device]`,
                *optional*):
                    Sent directly as `model_kwargs` (just a simpler shortcut).
                    When `accelerate` library is present, set `device_map="auto"` to
                    compute the most optimized `device_map` automatically.
                    Do not use `device_map` AND `device` at the same time as they will
                    conflict.
                torch_dtype (`str` or `torch.dtype`, *optional*):
                    Sent directly as `model_kwargs` (just a simpler shortcut) to use
                    the available precision for this model
                    (`torch.float16`, `torch.bfloat16`, ... or `"auto"`).
                trust_remote_code (`bool`, *optional*, defaults to `False`):
                    Whether to allow for custom code defined on the Hub in their own
                    modeling, configuration, tokenization or even pipeline files.
                    This option should only be set to `True` for repositories you trust
                    and in which you have read the code, as it will execute code present
                     on the Hub on your local machine.
                model_kwargs (`Dict[str, Any]`, *optional*):
                    Additional dictionary of keyword arguments passed along to the
                    model's `from_pretrained(...,**model_kwargs)` function.

    Returns:
        A suitable pipeline for the task.

    Examples:

    ```python
    >>> from openmind import pipeline

    >>> # will use transformers pipeline if not specified
    >>> pipeline_ins = pipeline("sentiment-analysis")

    >>> # if you want to use mindspore pipeline
    >>> pipeline_ins = pipeline("sentiment-analysis", framework="ms")
    ```
    """
    ORI_SUPPORTED_TASKS = None
    ORI_PIPELINE_REGISTRY = None
    if is_transformers_available():
        ORI_SUPPORTED_TASKS, ORI_PIPELINE_REGISTRY = pipeline_patch(change_dict=SUPPORTED_TASK_PATCH_DICT)

    try:
        if task is None and model is None:
            raise RuntimeError(
                "Impossible to instantiate a pipeline without either a task or a model being specified. "
                "Please provide a task class or a model"
            )

        if model is None and tokenizer is not None:
            raise RuntimeError(
                "Impossible to instantiate a pipeline with tokenizer specified but not the model as the provided tokenizer"
                " may not be compatible with the default model. Please provide a PreTrainedModel class or a"
                " path/identifier to a pretrained model when providing tokenizer."
            )

        if model is None and feature_extractor is not None:
            raise RuntimeError(
                "Impossible to instantiate a pipeline with feature_extractor specified but not the model as the provided"
                " feature_extractor may not be compatible with the default model. Please provide a PreTrainedModel class"
                " or a path/identifier to a pretrained model when providing feature_extractor."
            )

        revision = kwargs.get("revision", None)
        cache_dir = kwargs.get("cache_dir", None)
        force_download = kwargs.get("force_download", False)
        use_auth_token = kwargs.get("use_auth_token", None)
        trust_remote_code = kwargs.get("trust_remote_code", None)
        _commit_hash = kwargs.get("_commit_hash", None)
        torch_dtype = kwargs.get("torch_dtype", None)

        if task is not None and model is None:
            normalized_task, targeted_task, task_options = check_task(task)
            model, default_revision = _get_default_model_and_revision(targeted_task, framework, task_options)

        if isinstance(model, str):
            model_name_or_path = download_from_repo(
                model, revision=revision, cache_dir=cache_dir, force_download=force_download
            )
            pipeline_tag = get_task_from_readme(model_name_or_path)
            if task is not None:
                if pipeline_tag is not None:
                    if task != pipeline_tag:
                        logger.warning(f"The task `{task}` does not match the model `{model}`")
                else:
                    logger.warning("Cannot infer the task from the provided model.")
            else:
                if pipeline_tag is not None:
                    task = pipeline_tag
                else:
                    raise RuntimeError(
                        "Cannot infer the task from the provided model, please provide the task explicitly."
                    )
        else:
            if task is None:
                raise RuntimeError("If model is an actual instance of a pretrained model, must provide the task.")
            else:
                model_name_or_path = model

        if tokenizer is not None:
            if isinstance(tokenizer, str):
                tokenizer_name_or_path = download_from_repo(
                    tokenizer, revision=revision, cache_dir=cache_dir, force_download=force_download
                )
            else:
                tokenizer_name_or_path = tokenizer
        else:
            if (task == "text-generation" or task == "text_generation") and isinstance(model, str):
                tokenizer_kwargs = {
                    "revision": revision,
                    "token": use_auth_token,
                    "trust_remote_code": trust_remote_code,
                    "_commit_hash": _commit_hash,
                    "torch_dtype": torch_dtype,
                }
                tokenizer_name_or_path = AutoTokenizer.from_pretrained(model, **tokenizer_kwargs)
            else:
                tokenizer_name_or_path = tokenizer

        if isinstance(config, str):
            config_name_or_path = download_from_repo(
                config, revision=revision, cache_dir=cache_dir, force_download=force_download
            )
        else:
            config_name_or_path = config

        if isinstance(feature_extractor, str):
            feature_extractor_name_or_path = download_from_repo(
                feature_extractor, revision=revision, cache_dir=cache_dir, force_download=force_download
            )
        else:
            feature_extractor_name_or_path = feature_extractor

        if isinstance(image_processor, str):
            image_processor_name_or_path = download_from_repo(
                image_processor, revision=revision, cache_dir=cache_dir, force_download=force_download
            )
        else:
            image_processor_name_or_path = image_processor

        if framework is not None:
            if framework not in SUPPORTED_FRAMEWORKS:
                raise FrameworkNotSupportedError(framework=framework)
        else:
            framework = get_framework()

        if framework == "ms":
            if not is_mindformers_available():
                raise PipelinePackageNotFoundError(pipeline="mindspore", package="mindformers")
            from mindformers.pipeline import pipeline as pipeline_func

            kwargs.pop("revision", None)
            kwargs.pop("cache_dir", None)
            kwargs.pop("force_download", False)

            # MindFormers only receive param `device_id` with integer type.
            if "device_id" in kwargs and not isinstance(kwargs["device_id"], int):
                try:
                    kwargs["device_id"] = int(kwargs["device_id"])
                except ValueError:
                    raise ValueError("The `device_id` parameter can not be converted to integer type.")

            pipe = pipeline_func(
                task=task,
                model=model_name_or_path,
                config=config_name_or_path,
                tokenizer=tokenizer_name_or_path,
                feature_extractor=feature_extractor_name_or_path,
                image_processor=image_processor_name_or_path,
                framework=framework,
                **kwargs,
            )

        elif framework == "pt":
            if not is_transformers_available():
                raise PipelinePackageNotFoundError(pipeline="transformers", package="transformers")
            from transformers.pipelines import pipeline as pipeline_func

            model_kwargs = {
                "cache_dir": kwargs.pop("cache_dir", None),
                "force_download": kwargs.pop("force_download", False),
            }
            if "model_kwargs" in kwargs:
                model_kwargs.update(kwargs["model_kwargs"])
                kwargs.pop("model_kwargs")

            pipe = pipeline_func(
                task=task,
                model=model_name_or_path,
                config=config_name_or_path,
                tokenizer=tokenizer_name_or_path,
                feature_extractor=feature_extractor_name_or_path,
                image_processor=image_processor_name_or_path,
                framework=framework,
                model_kwargs=model_kwargs,
                **kwargs,
            )

        return pipe
    finally:
        # Rollback the patch operation of transformers
        if is_transformers_available():
            import transformers

            patch_list = [
                ("SUPPORTED_TASKS", ORI_SUPPORTED_TASKS),
                ("PIPELINE_REGISTRY", ORI_PIPELINE_REGISTRY),
            ]
            _apply_patches(patch_list, transformers.pipelines)
