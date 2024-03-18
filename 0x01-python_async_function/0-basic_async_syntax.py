#!/usr/bin/python3
import asyncio
import random
async def wait_random(max_delay: int = 10)->float:
    time= random.uniform(0,max_delay)
    return(time)
    await asyncio.sleep(time)
