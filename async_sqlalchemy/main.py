import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, select

Base = declarative_base()
base_dir = os.path.dirname(__file__)
DATABASE_URL = 'sqlite+aiosqlite:///' + \
    os.path.join(base_dir, 'example.sqlite')

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


async def init_db():
    print("[Init] データベースの初期化を開始します。")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print("[Init] 既存のテーブルを削除しました。")
        await conn.run_sync(Base.metadata.create_all)
        print("[Init] 新しいテーブルを作成しました。")


async def add_user(name):
    print(f"[Add User] {name}をデータベースに追加開始。")
    await asyncio.sleep(1)  # Simulating a delay
    async with async_session() as session:
        async with session.begin():
            user = User(name=name)
            session.add(user)
            print(f"[Add User] {name}をデータベースに追加完了。")


async def get_users():
    print("[Get Users] データベースからユーザーを取得します。")
    await asyncio.sleep(2)  # Simulating a delay
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        print("[Get Users] ユーザーの取得が完了しました。")
        return users


async def main_sequential():
    """逐次実行"""
    print("[Sequential] 逐次実行開始")
    await init_db()
    await add_user("中邑")
    await add_user("岡田")
    users = await get_users()
    for user in users:
        print(f"[Sequential] {user.id}: {user.name}")
    print("[Sequential] 逐次実行終了")


async def main_concurrent():
    """並行実行"""
    print("[Concurrent] 並行実行開始")
    await init_db()
    task1 = asyncio.create_task(add_user("中邑"))
    task2 = asyncio.create_task(add_user("岡田"))
    await asyncio.gather(task1, task2)  # 並行実行を待機
    users = await get_users()
    for user in users:
        print(f"[Concurrent] {user.id}: {user.name}")
    print("[Concurrent] 並行実行終了")


# 比較実行
print("[Start] 逐次実行と並行実行の比較を開始します。")
asyncio.run(main_sequential())
print("\n" + "-"*50 + "\n")
asyncio.run(main_concurrent())
