#!/usr/bin/env python3
"""Time complexity."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Find the time used in processing."""
    start_time = time.time()
    processes = asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())

    first, second, third, last = await processes
    end_time = time.time()
    return end_time - start_time
