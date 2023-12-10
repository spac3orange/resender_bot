from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.types.message import ContentType
from config import aiogram_bot, config_aiogram, bot_status
from filters import IsAdmin
router = Router()
router.message.filter(
    IsAdmin(F)
)

@router.message(Command(commands='start'))
async def start(message: Message):
    await bot_status.set_status(True)
    await message.answer(f'Приветствую, {message.from_user.username}')
    await message.answer(f'Бот запущен')


@router.message(Command(commands='stop'))
async def stop(message: Message):
    await bot_status.set_status(False)
    await message.answer(f'Бот остановлен')