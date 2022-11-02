# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:41:12 2022

@author: vujvalsai
"""

from pydantic import BaseModel

class Iris(BaseModel):
    SpecalLength: float 
    SepalWidth: float 
    PetalLength: float 
    PetalWidth: float