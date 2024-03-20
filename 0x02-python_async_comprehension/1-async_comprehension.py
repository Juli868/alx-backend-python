#!/usr/bin/env python3
"""Utilise yield results in the new function."""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Iterate over the yielded number."""
    result = [num async for num in async_generator()]
    return result
