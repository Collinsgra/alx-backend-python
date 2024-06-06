#!/usr/bin/env python3
''' type-annotated function make_multiplier that takes a float multiplier as argument
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier functions.
    '''
    return lambda x: x * multiplier
