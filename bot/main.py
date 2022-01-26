import settings
from aiogram import executor
from handlers import dp
from loader import bot


async def on_startup(dp):
    await bot.send_message(settings.ADMIN_ID, "Hello, I'm alive!")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
