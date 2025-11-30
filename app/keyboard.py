from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Creating a Reply keyboard that can send messages to a bot
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='<your text>'),
                                    KeyboardButton(text='<your text>')]],
                           resize_keyboard=True)

# Creating a Reply keyboard that cannot send messages to the bot, but can create buttons under the message
projects_kеуb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<your text>', callback_data='<your text_id>')],
    [InlineKeyboardButton(text='<your text>', callback_data='<your text_id>')]])
