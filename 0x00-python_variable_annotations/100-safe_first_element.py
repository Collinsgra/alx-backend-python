#!/usr/bin/env python3
'''task 100
'''
from typing import Iterable, List, Sequence, Tuple, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ task 100"""
    if lst:
        return lst[0]
    else:
        return None
