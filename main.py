from asyncio import run as run_async
from aiogram import Dispatcher
from handlers import start
from globals import bot, session, engine
from database import Base


async def main():
    dispatcher = Dispatcher()
    Base.metadata.create_all(engine)

    dispatcher.include_routers(start.router)

    await dispatcher.start_polling(bot)

    session.commit()
    engine.dispose()


if __name__ == '__main__':
    run_async(main())
