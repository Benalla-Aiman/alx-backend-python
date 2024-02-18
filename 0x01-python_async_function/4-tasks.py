#!/usr/bin/env python3
'''
Module for Task 4.
'''
import asyncio
from typing import List
from functools import partial

from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes task_wait_random n times.
    '''
    create_task = partial(task_wait_random, max_delay)
    wait_times = await asyncio.gather(*(create_task() for _ in range(n)))
    return sorted(wait_times)
