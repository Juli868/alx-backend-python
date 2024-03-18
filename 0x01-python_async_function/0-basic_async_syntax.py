#!/usr/bin/python3
"""Basics of Async."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for defined time."""
    time = random.uniform(0, max_delay)
    return (time)
    await asyncio.sleep(time)
