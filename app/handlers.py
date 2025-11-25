from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import F, Router

import app.keyboard as keyb
import app.base.request as req
# Creating routers, they connect everything
router = Router()

# Sending a message when click "/start"
@router.message(CommandStart())
async def cmd_start(message: Message):
    await req.set_user(message.from_user.id)
    await message.answer('<your text>', reply_markup=keyb.main) #Opens the keyboard

# If a specified word is sent to the bot, another specified text will be sent.
@router.message(F.text == '<your text>') 
async def github(message: Message):
    await message.answer('<your text>')

# If a specified word is sent to the bot, then another specified text will be sent and also Inline Keyboard(buttons)
@router.message(F.text == '<your text>')
async def projects(message: Message):
    await message.answer('<your text>', reply_markup=keyb.projects_kеуb)

# Accessing the database
@router.callback_query(F.data == '<your text_id>')      # Looking for an id
async def tg_bot(callback: CallbackQuery):
    await callback.answer('<your text>')                # Click notification output
    await callback.message.answer('<your text>')        # Displays a message