from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from database.queryset import *


menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Категории')],[KeyboardButton(text='Все игры')]
],resize_keyboard=True,input_field_placeholder='Але, нажмите кнопочку', one_time_keyboard=True)

# inline_test = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Аркада',callback_data='button1')],
#     [InlineKeyboardButton(text='Шутер',callback_data='button2')],
#     [InlineKeyboardButton(text='Гонки',callback_data='button3')]
# ])


async def categories_kb():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data=f'category_{category.id}'
        ))
    return builder.adjust(2).as_markup()


async def categories_kb2():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data=f'category2_{category.id}'
        ))
    return builder.adjust(2).as_markup()

async def categories_kb3():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data=f'category3_{category.id}'
        ))
    return builder.adjust(2).as_markup()

async def all_games_kb():
    builder = InlineKeyboardBuilder()
    games = await get_all_games()
    for game in games:
        builder.add(InlineKeyboardButton(
            text = game.name,
            callback_data=f'game_{game.id}'
        ))
    return builder.adjust(2).as_markup()


# async def games_kb(category_id):
#     builder = InlineKeyboardBuilder()
#     games = await get_games(category_id)
#     for game in games:
#         builder.add(InlineKeyboardButton(
#             text = game.name,
#             callback_data=f'game_{game.id}'
#         ))
#     builder.add(InlineKeyboardButton(
#         text = 'Назад к категориям',
#         callback_data= 'back_to_categories'
#     ))
#     return builder.adjust(2).as_markup()


PAGE_SIZE = 2
async def games_kb(category_id,page):
    offset = (page-1) * PAGE_SIZE   
    builder = InlineKeyboardBuilder()
    all_games = await get_games(category_id, offset=offset,limit=PAGE_SIZE)
    for game in all_games:
        builder.add(InlineKeyboardButton(
            text = game.name,
            callback_data=f'game_{game.id}'
        ))
    if page > 1:
        builder.add(InlineKeyboardButton(
            text = '<<',
            callback_data=f'page_{category_id}_{page-1}'
        ))
    if len(all_games) == PAGE_SIZE:
        builder.add(InlineKeyboardButton(
            text = '>>',
            callback_data=f'page_{category_id}_{page+1}'
        ))
    return builder.adjust(2).as_markup()


PAGE_SIZE = 2
async def all_games_kb2(page):
    offset = (page-1) * PAGE_SIZE   
    builder = InlineKeyboardBuilder()
    all_games = await get_all_games2(offset=offset,limit=PAGE_SIZE)
    for game in all_games:
        builder.add(InlineKeyboardButton(
            text = game.name,
            callback_data=f'game_{game.id}'
        ))
    if page > 1:
        builder.add(InlineKeyboardButton(
            text = '<<',
            callback_data=f'pages_{page-1}'
        ))
    if len(all_games) == PAGE_SIZE:
        builder.add(InlineKeyboardButton(
            text = '>>',
            callback_data=f'pages_{page+1}'
        ))
    return builder.adjust(2).as_markup()



async def back_to_categories_kb(game_id):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text = 'Назад к категории',
        callback_data= 'back_to_categories'
    ))
    builder.add(InlineKeyboardButton(
        text = 'Удалить игру',
        callback_data= f'delete_{game_id}'
    ))
    builder.add(InlineKeyboardButton(
        text = 'Купить',
        callback_data= f'buy_game_{game_id}'
    ))
    return builder.adjust(2).as_markup()

# async def delete_game_kb(game_id):
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Удалить игру',
#         callback_data= f'delete_{game_id}'
#     ))
#     return builder.adjust(1).as_markup()























