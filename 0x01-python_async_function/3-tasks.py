#!/usr/bin/env python3
'''
Module for Task 3.
'''
import asyncio
from asyncio import Task

from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task:
    '''
    Creates an asynchronous task for wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))
