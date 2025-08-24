import asyncio

#coroutine, async, await
#async def main():#await is always needed to run a coroutine
#    print("batman")
#    await villain("text")
#    task = asyncio.create_task(villain("text"))
#    await asyncio.sleep(0.5) #this tells the main function to chill and
    # let whatever task is in the function to run during the idle cppu time
#    print("finished")

#async def villain(text):
#    print(text)
#    await asyncio.sleep(10)

#asyncio.run(main())

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching data")
    return {"data":1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.8)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1 # a future
    print(value)
    await task2

asyncio.run(main())