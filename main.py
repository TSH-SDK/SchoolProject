import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.filters.command import Command, CommandObject
from decouple import config
from KeyBoards import Keyboard

from WbPars import wb_pars
from YaPars import ya_pars

TOKEN = config('BOT_TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher()

requests = {

}


async def sort_func(id_of_chat):
    requests[f"{id_of_chat}"]["wb"]["sort"] = 1
    await bot.send_message(text="Выберите тип сортировки", reply_markup=Keyboard.choose_sort(), chat_id=id_of_chat)


async def price_func(id_of_chat):
    if not requests[f"{id_of_chat}"]["price_low"]:
        await bot.send_message(text="Введите нижний порог цены", chat_id=id_of_chat)
    else:
        await bot.send_message(text="Введите высший порог цены", chat_id=id_of_chat)


async def delivery_func(id_of_chat):
    requests[f"{id_of_chat}"]["wb"]["delivery"] = 1
    await bot.send_message(text="Выберите подходящий срок доставки", chat_id=id_of_chat,
                           reply_markup=Keyboard.wb_delivery_data())


add_funcs = {
    "sort": lambda x: sort_func(x),
    "price": lambda x: price_func(x),
    "delivery": lambda x: delivery_func(x),
}


@dp.callback_query()
async def start_callback(cq: CallbackQuery):
    if cq.data == "search":
        await cq.answer()
        await bot.send_message(text="Подождите. Идет поиск товаров...", chat_id=cq.from_user.id)
        data_wb = wb_pars(requests[f"{cq.from_user.id}"]["item_name"], requests[f"{cq.from_user.id}"])

        await bot.send_photo(photo=data_wb[1]["photo"],
                             caption=f"Название товара: {data_wb[1]['name']}\n"
                             f"Цена без скидки: {data_wb[1]['r_price']}\n"
                             f"Цена со скидкой: {data_wb[1]['d_price']}\n"
                             f"Рейтинг: {data_wb[1]['rate']}\n"
                             f"Срок доставки: {data_wb[1]['delivery_time']}\n"
                             f"Ссылка: {data_wb[1]['link']}",
                             chat_id=cq.from_user.id)
        await bot.send_photo(photo=data_wb[2]["photo"],
                             caption=f"Название товара: {data_wb[2]['name']}\n"
                             f"Цена без скидки: {data_wb[2]['r_price']}\n"
                             f"Цена со скидкой: {data_wb[2]['d_price']}\n"
                             f"Рейтинг: {data_wb[2]['rate']}\n"
                             f"Срок доставки: {data_wb[2]['delivery_time']}\n"
                             f"Ссылка: {data_wb[2]['link']}",
                             chat_id=cq.from_user.id)
        await bot.send_photo(photo=data_wb[3]["photo"],
                             caption=f"Название товара: {data_wb[3]['name']}\n"
                             f"Цена без скидки: {data_wb[3]['r_price']}\n"
                             f"Цена со скидкой: {data_wb[3]['d_price']}\n"
                             f"Рейтинг: {data_wb[3]['rate']}\n"
                             f"Срок доставки: {data_wb[3]['delivery_time']}\n"
                             f"Ссылка: {data_wb[3]['link']}",
                             chat_id=cq.from_user.id)

        data_ya = ya_pars(requests[f"{cq.from_user.id}"]["item_name"], requests[f"{cq.from_user.id}"])

        await bot.send_photo(photo=data_ya[0]["photo"],
                             caption=f"Название товара: {data_ya[0]['name']}\n"
                                     #f"Цена без скидки: {data_ya[0]['r_price']}\n"
                                     #f"Цена со скидкой: {data_ya[0]['d_price']}\n"
                                     #f"Рейтинг: {data_ya[0]['rate']}\n"
                                     #f"Срок доставки: {data_ya[0]['delivery_time']}\n"
                                     f"Ссылка: {data_ya[0]['link']}",
                             chat_id=cq.from_user.id)
        await bot.send_photo(photo=data_ya[1]["photo"],
                             caption=f"Название товара: {data_ya[1]['name']}\n"
                                     #f"Цена без скидки: {data_ya[1]['r_price']}\n"
                                     #f"Цена со скидкой: {data_ya[1]['d_price']}\n"
                                     #f"Рейтинг: {data_ya[1]['rate']}\n"
                                     #f"Срок доставки: {data_ya[1]['delivery_time']}\n"
                                     f"Ссылка: {data_ya[1]['link']}",
                             chat_id=cq.from_user.id)
        await bot.send_photo(photo=data_ya[2]["photo"],
                             caption=f"Название товара: {data_ya[2]['name']}\n"
                                     #f"Цена без скидки: {data_ya[2]['r_price']}\n"
                                     #f"Цена со скидкой: {data_ya[2]['d_price']}\n"
                                     #f"Рейтинг: {data_ya[2]['rate']}\n"
                                     #f"Срок доставки: {data_ya[2]['delivery_time']}\n"
                                     f"Ссылка: {data_ya[2]['link']}",
                             chat_id=cq.from_user.id)
        requests[f"{cq.from_user.id}"] = {}

    elif cq.data.split("/")[0] == "sort":
        await cq.answer()
        if not requests[f"{cq.from_user.id}"]["wb"]["sort"]:
            await add_funcs[cq.data](cq.from_user.id)
        else:
            requests[f"{cq.from_user.id}"]["wb"]["sort"] = cq.data.split("/")[1]
            requests[f"{cq.from_user.id}"]["ya"]["sort"] = cq.data.split("/")[-1]
            await bot.send_message(text=f"Привет, твой товар - {' '.join(requests[f'{cq.from_user.id}']['item_name'])}",
                                   reply_markup=Keyboard.choose_filter(), chat_id=cq.from_user.id)
    elif cq.data == "price":
        await cq.answer()
        requests[f"{cq.from_user.id}"]["current"] = "price"
        await add_funcs[cq.data](cq.from_user.id)
    elif cq.data.split("/")[0] == "delivery":
        await cq.answer()
        if not requests[f"{cq.from_user.id}"]["wb"]["delivery"]:
            await add_funcs[cq.data](cq.from_user.id)
        else:
            requests[f"{cq.from_user.id}"]["delivery"] = cq.data.split("/")[1]
            requests[f"{cq.from_user.id}"]["ya"]["sort"] = cq.data.split("/")[-1]
            await bot.send_message(text=f"Привет, твой товар - {' '.join(requests[f'{cq.from_user.id}']['item_name'])}",
                                   reply_markup=Keyboard.choose_filter(), chat_id=cq.from_user.id)


@dp.message(Command('start'))
async def start(msg: Message):
    requests[f"{msg.from_user.id}"] = {
        "item_name": None,
        "price_low": 0,
        "price_high": 0,
        "current": None,
        "ya": {
            "sort": None,
            "delivery": None,
        },
        "wb": {
            "sort": None,
            "delivery": None,
        }
    }
    await msg.answer('Напишите: "/find название товара"')


@dp.message(Command("find"))
async def find_item(msg: Message, command: CommandObject):
    requests[f"{msg.from_user.id}"] = {
        "item_name": None,
        "price_low": 0,
        "price_high": 0,
        "current": None,
        "ya": {
            "sort": None,
            "delivery": None,
        },
        "wb": {
            "sort": None,
            "delivery": None,
        }
    }
    requests[f"{msg.from_user.id}"]["item_name"] = msg.text.split()[1:]
    await msg.answer(f"Привет, твой товар - {command.text}",
                     reply_markup=Keyboard.choose_filter())


@dp.message()
async def handler(msg: Message):
    if requests[f"{msg.from_user.id}"]["current"] == "price":
        if not requests[f"{msg.from_user.id}"]["price_low"]:
            requests[f"{msg.from_user.id}"]["price_low"] = msg.text
            await price_func(msg.from_user.id)
        else:
            requests[f"{msg.from_user.id}"]["price_high"] = msg.text
            requests[f"{msg.from_user.id}"]["current"] = None
            await msg.answer(f"Привет, твой товар - {' '.join(requests[f'{msg.from_user.id}']['item_name'])}",
                             reply_markup=Keyboard.choose_filter())


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
