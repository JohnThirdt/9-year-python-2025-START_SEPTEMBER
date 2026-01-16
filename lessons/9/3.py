import asyncio
import time


async def make_coffee():
    print("Начали готовить кофе")
    await asyncio.sleep(3)
    print("Кофе готов")
    return "кофе"


async def make_toast():
    print("Начали делать тост")
    await asyncio.sleep(2)
    print("Тост готов!")
    return "тост"


async def main():
    start = time.time()

    # 5s
    # await make_coffee()
    # await make_toast()

    # 3s
    coffee_task = asyncio.create_task(make_coffee())
    toast_task = asyncio.create_task(make_toast())

    coffee = await coffee_task
    toast = await toast_task

    end = time.time()
    print(f"Всё готово! {coffee} + {toast}")
    print(f"Заняло {end - start:.1f} с")

asyncio.run(main())