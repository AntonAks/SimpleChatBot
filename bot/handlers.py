from aiogram import types
from loader import dp
from db import store_message


@dp.message_handler(commands=['start'])
async def _start_command(message: types.Message):
    await message.answer(f"Hello! Welcome to the simple chatbot")


@dp.message_handler()
async def echo_message(message: types.Message):
    store_message(message)
    await message.answer(f"echo answer: {message['text']}")
