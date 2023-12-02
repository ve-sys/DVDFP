#ВКЛЮЧИТЬ КОГДА ОСНОВНОЕ ЛЕГЛО
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import*
from config import token
print(f'Бот запущен|{token}')

bot = Bot(token)
dp = Dispatcher()

@dp.message()
async def echo(message: Message):
    await message.answer('Что то сломалось!\nУважаемый пользователь, бот находится на техослуживании\nПриносим извинения')


#не трогай, это техническое
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
