import asyncio


async def task1():
    await asyncio.sleep(2)
    print("タスク1が完了しました")


async def task2():
    await asyncio.sleep(3)
    print("タスク2が完了しました")


async def task3():
    await asyncio.sleep(1)
    print("タスク3が完了しました")


async def main():
    print("メイン処理を開始します")
    event_loop_task1 = asyncio.create_task(task1())
    event_loop_task2 = asyncio.create_task(task2())
    event_loop_task3 = asyncio.create_task(task3())

    print("イベントループ内のタスクを開始します")
    await event_loop_task1
    print("イベントループ内のタスク1とタスク3が完了しました")

    await event_loop_task2
    print("イベントループ内のタスク2が完了しました")

    print("イベントループではないタスク3を開始します")
    await task3()
    print("イベントループではないタスク3が完了しました")

    await event_loop_task3
    print("イベントループ内の全てのタスクが完了しました")
    print("イベントループではないタスク1を開始します")
    await task1()
    print("イベントループではないタスク1が完了しました")
    print("すべてのタスクが完了しました")


asyncio.run(main())
