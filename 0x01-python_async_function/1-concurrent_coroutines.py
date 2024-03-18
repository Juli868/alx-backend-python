#!/usr/bin/env python3
"""Perfoming an assync coroutine multiple times."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Perfom await n times."""
    result = []
    for i in range(0, max_delay):
        result.append(asyncio.run(wait_random(max_delay)))
    return (sorted(result))
