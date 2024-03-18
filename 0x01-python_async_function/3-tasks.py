#!/usr/bin/env python3
"""Define a function that returns async task."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """After considering the input, return the task."""
    result = asyncio.create_task(wait_random(max_delay))
    return result
