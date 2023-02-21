import random

from loader import dp
from aiogram.types import Message
import game


@dp.message_handler()
async def mes_help(message: Message):
    for key,val in game.total.items():
        if message.from_user.id == key:
            count = message.text
            if count.isdigit() and 0 < int(count) < 29:
                val[1] -= int(count)
                if await check_win(message, 'Ты', val):
                    return True
                await message.answer(f'{val[0]} взял {count} конфет и на столе осталось {val[1]}\n'
                                     f'Теперь ход бота...')
                bot_take = random.randint(1, 28) if val[1] > 28 else val[1]
                val[1] -= bot_take
                if await check_win(message, 'Бот', val):
                    return True
                await message.answer(f'Бот Виталий взял {bot_take} конфет и '
                                     f'на столе осталось {val[1]}\n'
                                     f'Теперь твой ход...')
            else:
                await message.answer(f'Введите число от 1 до 28')


async def check_win(message: Message, win: str, val: list):
    if val[1] <= 0:
        await message.answer(f'{win} победил! Поздравляю!')
        del game.total[message.from_user.id]
        return True
    return False
