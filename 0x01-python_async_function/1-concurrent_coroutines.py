#!/usr/bin/env python3
""" The list of the delays should be in ascending order
without using sort() because of concurrency."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ task 1 pythonasync project"""
    the_list = [await wait_random(max_delay) for i in range(n)]
    return sorted(the_list)
