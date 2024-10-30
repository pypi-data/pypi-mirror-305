import asyncio
from .broker import broker, app


def subscriber(queue_name):
    return broker.subscriber(queue_name)


async def run_async():
    await app.run()


def run():
    asyncio.run(run_async())
