import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import sqlite3
import random


con = sqlite3.connect('D:/YaOgeBot/database/zadaniya.db')
cur = con.cursor()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7159623761:AAFvAboAw81T7OZMXG9YXRUu8UfR9gPPBxU")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("▶️ Введите /practice, чтобы начать практику "
                         "❔ Введите /help, если возникли вопросы")

@dp.message(Command("practice"))
async def cmd_start(message: types.Message):
    id = cur.execute("""SELECT id FROM usl ORDER BY RANDOM()""")
    l_id = [list(p) for p in id]
    rand_id = random.choice(l_id)[0]
    text = cur.execute("SELECT usl_text FROM usl WHERE id=?;", (rand_id,))
    result = [list(row) for row in text][0][0]
    res = result.encode().decode('utf-8')
    ans = cur.execute("SELECT true FROM usl WHERE id=?;", (rand_id,))
    await message.answer(res)
    mess = message.text
    if mess == ans:
        await message.answer('Верно')
    else:
        await message.answer('Ошибка')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())