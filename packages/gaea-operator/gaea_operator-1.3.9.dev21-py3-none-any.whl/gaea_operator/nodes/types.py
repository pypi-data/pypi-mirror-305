#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/25
# @Author  : yanxiaodong
# @File    : types.py
"""
from typing import List, Dict, Union
from pydantic import BaseModel


class Image(BaseModel):
    """
    Image
    """
    kind: str
    name: str


class ImageV2(BaseModel):
    """
    Image
    """
    acceleratorName: str = None
    acceleratorKind: str = None
    name: str


class ModelFormat(BaseModel):
    """
    ModelFormat
    """
    key: str
    acceleratorKind: str = None
    acceleratorName: str = None
    formats: List[str] = None


class Properties(BaseModel):
    """
    Properties
    """
    accelerator: str = ""
    computeTips: Dict[str, List] = {}
    flavourTips: Dict[str, str] = {}
    images: List[Union[Image, ImageV2]] = []
    modelFormats: Union[List[ModelFormat], Dict[str, Dict[str, List]]] = []