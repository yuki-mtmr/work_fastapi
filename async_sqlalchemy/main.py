import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, select

Base = declarative_base()
base_dir = os.path.dirname(__file__)
DATABASE_URL = 'sqlite+aiosqlite:///' + os.path.join(base_dir, 'exmple.sqlite')

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
    print("データベースの初期化を開始します。")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print("既存のテーブルを削除しました。")
        await conn.run_sync(Base.metadata.create_all)
        print("新しいテーブルを作成しました。")


async def add_user(name):
    print(f"{name}をデータベースに追加します。")
    async with async_session() as session:
        async with session.begin():
            user = User(name=name)
            session.add(user)
            print(f"{name}をデータベースに追加しました。")


async def get_users():
    print("データベースからユーザーを取得します。")
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        print("ユーザーの取得が完了しました。")
        return users


async def main():
    await init_db()
    await add_user("中邑")
    await add_user("岡田")
    users = await get_users()
    for user in users:
        print(f"{user.id}: {user.name}")


asyncio.run(main())
