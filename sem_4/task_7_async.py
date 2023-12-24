import asyncio
import time
from random import randint

array = []
async def create_array():
    global array
    for _ in range(2000):
        array.append(randint(1, 100))
    print(f'Заполнили массив за {time.time() - start_time:.5f}')
async def count_sum():
    sum_ = 0
    for num in array:
        sum_ += num
    print(f'Вычислили сумму за {time.time()-start_time:.5f}, сумма - {sum_}')

start_time = time.time()

async def main():
    task1 = asyncio.create_task(create_array())
    task2 = asyncio.create_task(count_sum())
    await task1
    await task2
asyncio.run(main())
