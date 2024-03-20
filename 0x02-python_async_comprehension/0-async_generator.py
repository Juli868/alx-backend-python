#!/usr/bin/env python3
"""Wait and tield a number."""
import asyncio
import random


async def async_generator() -> [float, None, None]:
    """Generate and yield a number after a sleep."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
