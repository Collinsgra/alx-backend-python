#!/usr/bin/env python3
'''task 102
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:

    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array: tuple = (12, 72, 91)

zoom_2x: list = zoom_array(array)

zoom_3x: list = zoom_array(array, 3)
