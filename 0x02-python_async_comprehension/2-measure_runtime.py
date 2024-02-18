#!/usr/bin/env python3
""" Module documentation """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Function documentation"""
    start = time.perf_counter()
    coroutines = []
    for i in range(4):
        coroutines.append(async_comprehension())
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return end - start
