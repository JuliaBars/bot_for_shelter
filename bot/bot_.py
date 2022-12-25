from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    start_buttons = [
        "Выбрать собаку", "Выбрать кошку",
        "Как помочь", "Контакты"
    ]
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.reply(
        (f"Привет, {message.from_user.first_name}, я бот "
         "для поиска домашних животных"), reply_markup=keyboard)


@dp.message_handler(Text(equals="Контакты"))
async def contacts(message: types.Message):
    inline_markup = types.InlineKeyboardMarkup()
    inline_markup.add(types.InlineKeyboardButton(
        text="Telegram", url="https://t.me/zoohome_korolev"))
    inline_markup.add(types.InlineKeyboardButton(
        text="Instagram", url="https://www.instagram.com/zoohome_korolev/"))
    await message.answer("Контакты приюта:", reply_markup=inline_markup)


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
