#!/usr/bin/env python3
"""Perfoming an assync coroutine multiple times."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Perfom await n times."""
    result = [wait_random(max_delay) for i in range(n)]
    result = await asyncio.gather(*result)
    return sorted(result)
