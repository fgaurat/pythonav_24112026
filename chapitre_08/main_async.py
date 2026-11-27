import asyncio
import time

async def hello(name):
    
    return f"hello {name}"


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    
    # s = await hello("fred")
    # print(s)
    # r1 = await add(1,2)
    # print(r1)
    # r2 = await add(2,5)
    # print(r2)
    
    all_add = [add(1,2),add(2,4),add(5,6)]
    
    
    r = await asyncio.gather(*all_add)
    print(r)
    
    end = time.perf_counter()
    print(f"{end-start:0.2f}s")
    

if __name__=='__main__':
    asyncio.run(main())
