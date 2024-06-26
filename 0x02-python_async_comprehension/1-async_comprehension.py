#!/usr/bin/env python3
""" coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers"""

import asyncio
from typing import List
import time
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers"""
    gen = [i async for i in async_generator()]
    return gen
