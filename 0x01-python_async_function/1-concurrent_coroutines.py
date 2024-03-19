#!/usr/bin/env python3
"""Perfoming an assync coroutine multiple times."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Perfom await n times."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    _, completed = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    result = [task.result() for task in _]
    return result
