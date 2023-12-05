#ВКЛЮЧИТЬ КОГДА ОСНОВНОЕ ЛЕГЛО
import sqlite3
import Data.date as dd
databasename=dd.databasename
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import*
from config import token1
print(f'Бот запущен|{token1}')

bot = Bot(token1)
dp = Dispatcher()

@dp.message()
async def echo(message: Message):
    msg=message.text
    with sqlite3.connect(databasename) as db:
        cursor = db.cursor()
        await message.answer(f'Запрос:{msg}')
        cursor.execute(msg)
        try:
            await message.answer(f'Ответ:{cursor.fetchall()}')
        except:
            ...


#не трогай, это техническое
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
