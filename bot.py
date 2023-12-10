import asyncio
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import aiogram_bot, logger
from handlers import redirect_module, start
from keyboard import set_commands_menu

async def start_params() -> None:
    dp = Dispatcher(storage=MemoryStorage())
    logger.info('Bot started')

    dp.include_router(redirect_module.router)
    dp.include_router(start.router)

    await set_commands_menu(aiogram_bot)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await aiogram_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(aiogram_bot)



async def main():
    task1 = asyncio.create_task(start_params())
    await asyncio.gather(task1)

if __name__ == '__main__':
    try:
        while True:
            asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning('Bot stopped')
    except Exception as e:
        logger.error(e)

