# Simple example for using the metronome

import asyncio
from metronome.metronome import Metronome

# define a callback
async def print_time_stamp(x):
  print(x)

# collect all the metronome's callbacks
cbs = [print_time_stamp]

# create the metronome
metronome = Metronome(cbs)

# produce the coroutine
metronome_coro = metronome.run()

# asyncio boilerplate to run the coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(metronome_coro)
