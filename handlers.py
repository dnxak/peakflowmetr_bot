from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    # тоже самое await bot.send_message(msg.chat.id, "Text")


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message()
async def message_handler(msg: Message):
   await msg.answer(f'Добрый день, {msg.from_user.first_name}. Твой ID: {msg.from_user.id}. Твое сообщение: "{msg.text}"')
