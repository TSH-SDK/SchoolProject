from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


class Keyboard:
    @staticmethod
    def choose_filter():
        inline_btn_1 = InlineKeyboardButton(text='Сортировка', callback_data='sort')
        inline_btn_2 = InlineKeyboardButton(text='Граница цены', callback_data='price')
        inline_btn_3 = InlineKeyboardButton(text='Срок доставки', callback_data='delivery')
        inline_btn_4 = InlineKeyboardButton(text='Найти', callback_data='search')
        inline_kb = InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1, inline_btn_2, inline_btn_3], [inline_btn_4]])
        return inline_kb

    @staticmethod
    def choose_sort():
        inline_btn_1 = InlineKeyboardButton(text="По популярности", callback_data="sort/nothing/")
        inline_btn_2 = InlineKeyboardButton(text="По рейтингу", callback_data="sort/rate/rating")
        inline_btn_3 = InlineKeyboardButton(text="По возрастанию цены", callback_data="sort/priceup/aprice")
        inline_btn_4 = InlineKeyboardButton(text="По убыванию цены", callback_data="sort/pricedown/dprice")
        inline_btn_5 = InlineKeyboardButton(text="По новинкам", callback_data="sort/newly/")
        inline_btn_6 = InlineKeyboardButton(text="Сначала выгодные", callback_data="sort/benefit/")
        inline_kb = InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1, inline_btn_2], [inline_btn_3, inline_btn_4],
                                                          [inline_btn_5, inline_btn_6]])
        return inline_kb

    @staticmethod
    def wb_delivery_data():
        inline_btn_1 = InlineKeyboardButton(text="Любой", callback_data="delivery/nothing/")
        inline_btn_2 = InlineKeyboardButton(text="Завтра", callback_data="delivery/24/0")
        inline_btn_3 = InlineKeyboardButton(text="Послезавтра", callback_data="delivery/48/1")
        inline_btn_4 = InlineKeyboardButton(text="До 3 дней", callback_data="delivery/72/")
        inline_btn_5 = InlineKeyboardButton(text="До 5 дней", callback_data="delivery/120/5")
        inline_kb = InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1],
                                                          [inline_btn_2, inline_btn_3],
                                                          [inline_btn_4, inline_btn_5]])
        return inline_kb
