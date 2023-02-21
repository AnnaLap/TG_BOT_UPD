import game
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    global max_total
    global duel
    for key,val in game.total.items():
        if message.from_user.id == key:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        # game.new_game = True
        await message.answer(f'Привет, {message.from_user.full_name}'
                             f'Мы будем играть в конфеты. Чтобы выбрать количество конфет в игре напиши "/set <количество>" (по умолчанию 150)')
        max_total = 150
        my_game = {message.from_user.id : [message.from_user.first_name, max_total]}
        game.total = my_game
        print(duel)


@dp.message_handler(commands=['set'])
async def mes_set(message: Message):
    global max_total
    global duel
    max_total = int(message.text.split()[1])
    game.total = {message.from_user.id : [message.from_user.first_name, max_total]}
    await message.answer(f'Теперь в игре {max_total} конфет! Ходи первым:')
    print(duel)