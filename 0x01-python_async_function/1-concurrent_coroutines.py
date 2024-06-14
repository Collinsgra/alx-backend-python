#!/usr/bin/env python3
""" The list of the delays should be in ascending order
without using sort() because of concurrency."""
import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        Insert delay while maintaining the ascending order
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return delays
