#!/usr/bin/env python3
""" wait_n and alter it into a new function task_wait_n"""
import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n and alter it into a new function task_wait_n"""
    task = task_wait_random(max_delay)
    task = [task_wait_random(max_delay) for i in range(n)]
    all_list = await asyncio.gather(*task)
    return sorted(all_list)
