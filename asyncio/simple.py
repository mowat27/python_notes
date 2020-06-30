import asyncio


def hello():
    return 'Hello'


async def greeting(name):
    # Normal functions can be called as normal
    # from inside an async function
    return f'{hello()}, {name}'


async def greet(names):
    for name in names:
        # Async functions can be called but
        # they must be awaited
        print(await greeting(name))


loop = asyncio.get_event_loop()
loop.run_until_complete(greet(["Bob", "Sharon", "Kylie"]))
