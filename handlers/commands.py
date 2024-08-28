from aiogram import Router,F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile, URLInputFile
from .keyboards import *
from .admin import *

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f'''Приветики {message.from_user.full_name}!
    Я ботик, который продает ключики для игр \n чем могу помочь?''',reply_markup=menu_kb)

# @router.message(F.text.lower() == 'привет')
# async def hello(message: Message):
#     await message.answer('Привет, как дела?')

# @router.message(F.text.startswith('пока'))
# async def bye(message: Message):
#     await message.answer('До свидания!')

@router.message(F.text == 'Категории')
async def category(message: Message):
    await message.answer('Выберите категорию:',reply_markup=await categories_kb())

@router.message(F.text == 'Все игры')
async def games(message: Message):
    await message.answer('Выберите игру:',reply_markup=await all_games_kb2(page=1))

@router.callback_query(F.data.startswith('pages_'))
async def game_pag(callback: CallbackQuery):
    # await callback.message.delete()
    data = callback.data.split('_')
    page = int(data[1])
    await callback.message.edit_reply_markup(
        reply_markup=await all_games_kb2(page))

@router.message(Command('help'))
async def help(message: Message):
    await message.reply('Нужна помощь? \n Извинитесь, помощи не будет')


@router.message(Command('phone'))
async def phone(message: Message):
    await message.reply('Номер телефона: +996 82 92 31, не звоните пжшки')


@router.message(Command('id'))
async def id(message: Message):
    await message.reply(f'''Вот пожалуйста, ваша айдишка: {message.from_user.id}''')


@router.message(Command('username'))
async def username(message: Message):
    await message.answer(f'''Ваш username: {message.from_user.username}(поменяйте на нормальный)''')

@router.callback_query(F.data == 'back_to_categories')
async def back_to_categories(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите категорию:', reply_markup=await categories_kb())




@router.callback_query(F.data.startswith('category_'))
async def category_game(callback:CallbackQuery):
    await callback.message.delete()
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Игры по этой категории: ', reply_markup=await games_kb(category_id,page=1))


@router.callback_query(F.data.startswith('page_'))
async def game_paginate(callback: CallbackQuery):
    # await callback.message.delete()
    data = callback.data.split('_')
    category_id = data[1]
    page = int(data[2])
    await callback.message.edit_reply_markup(
        reply_markup=await games_kb(category_id,page))


from database.queryset import get_game

@router.callback_query(F.data.startswith('game_'))
async def game(callback:CallbackQuery):
    await callback.message.delete()
    game_id = callback.data.split('_')[1]
    game = await get_game(game_id)
    if game.image.startswith('https') or game.image.startswith('AgAC'):
        image = game.image
    else:
        image = FSInputFile(game.image)
    await callback.message.answer_photo(photo=image,caption=f'{game.name} \n {game.description}', 
     reply_markup=await back_to_categories_kb(game_id))
    
        


from payment import create_payment

@router.callback_query(F.data.startswith('buy_game_'))
async def buy_game(callback: CallbackQuery):
    game_id = callback.data.split('_')[2]
    game = await get_game(game_id)

    payment = await create_payment(game.price, f'Покупка игры {game.name}')
    await callback.message.answer(f'ссылка для оплаты {payment.confirmation.confirmation.url}')
























