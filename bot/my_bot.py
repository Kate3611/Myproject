import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from bot.config import my_token
from aiogram import F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from random import randint

logging.basicConfig(level=logging.INFO)
bot = Bot(token=my_token, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Мангалы"),
        types.KeyboardButton(text="Мангалы с навесом"),
        types.KeyboardButton(text="Аксессуары")
    )
    builder.row(
        types.KeyboardButton(text="Информация")
    )
    builder.row(
        types.KeyboardButton(text="Хочу получить скидку"),
        types.KeyboardButton(text="Отправить контакт", request_contact=True)

    )

    await message.answer("Вас приветствует Grills.by :) Выбери нужное",
                         reply_markup=builder.as_markup(resize_keyboard=True))

    @dp.message(F.text.lower() == "мангалы")
    async def model(message):
        await message.reply("Барбекю 800 - 650 руб.\n"
                            "Барбекю 1000 - 710 руб.\n"
                            "Барбекю Лофт 800 - 870 руб.\n"
                            "Барбекю Лофт 1000 - 930 руб.\n"
                            "Барбекю 800 с печью - 1600 руб.\n")

    @dp.message(F.text.lower() == "мангалы с навесом")
    async def model(message):
        await message.reply("Барбекю 1000 с навесом - 1320 руб.\n"
                            "Барбекю 800 с навесом - 1260 руб.\n"
                            "Барбекю Лофт 1000 с навесом - 1320 руб.\n"
                            "Барбекю Лофт 800 с навесом - 1260 руб.\n"
                            "Барбекю 800 с навесом и печью - 2100 руб.\n"
                            "Барбекю Лофт 800 с навесом и печью - 2200 руб.\n"
                            "Модульный Лофт навес - 660 руб.\n"
                            "Модульный навес - 540 руб.\n")

    @dp.message(F.text.lower() == "хочу получить скидку")
    async def without_puree(message):
        await message.reply("Отправь сообщение: /random,и испытай свою удачу!")

    @dp.message(F.text.lower() == "аксессуары")
    async def accessories(message):
        await message.reply("Решетка-гриль (нерж.) с ручкой - 80 руб.\n"
                            "Подставка под казан/садж - 60 руб.\n"
                            "Дубовая доска на боковую полку - 40 руб.\n"
                            "Кочерга+совок - 37 руб.\n"
                            "Разделитель жаровни - 20 руб.\n"
                            "Шампуры- 8 руб.\n"
                            "Антипригарный тефлоновый коврик - 15 руб.\n"
                            "Шумовка+половник - 40 руб.\n")

    @dp.message(F.text.lower() == "информация")
    async def model_info(message):
        await message.reply("/info1 - для получения информации о Мангалах\n"
                            "/info2 - для получения информации о Мангалах с навесом\n"
                            "/info3 - для получения информации о Мангалах снавесом и печью\n"
                            "/info4 - для получения информации о Навесах\n")




# async def contact_keyboard():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     first_button = KeyboardButton(text=("📱 Отправить"), request_contact=True)
#     markup.add(first_button)
#     return markup
#
#
# # handlers.py
# @dp.message_handler(Command("contact"))
# async def share_number(message: types.Message):
#     await message.answer("Нажмите на кнопку ниже, чтобы отправить контакт", reply_markup=await contact_keyboard())
#
# @dp.message_handler(content_types=types.ContentType.CONTACT)
# async def get_contact(message: types.Message):
#     contact = message.contact
#     await message.answer(f"Спасибо, {contact.full_name}.\n"
#                          f"Ваш номер {contact.phone_number} был получен")






@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажми на кнопку, чтобы бот отправил число",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 1001)))
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )

@dp.message(Command("info1"))
async def cmd_info(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Б800"),
            types.KeyboardButton(text="Б1000"),
            types.KeyboardButton(text="Б Лофт 800"),
            types.KeyboardButton(text="Б Лофт 1000"),
            types.KeyboardButton(text="Б800 с печью")
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери интересующее"
    )
    await message.answer('Барбекю было сокращено как "Б"', reply_markup=keyboard)

@dp.message(F.text.lower() == "б800")
async def specification(message: types.Message):
    await message.reply("Общая длина: 140 см \n"
                        "Высота: 100 см \n"
                        "Вес: 51 кг \n"
                        "Длина жаровни: 80 см \n"
                        "Толщина стали: 5 мм\n")

@dp.message(F.text.lower() == "б1000")
async def specification(message: types.Message):
    await message.reply("Общая длина: 160 см \n"
                        "Высота: 100 см \n"
                        "Вес: 61 кг \n"
                        "Длина жаровни: 100 см \n"
                        "Толщина стали: 5 мм\n")

@dp.message(F.text.lower() == "б лофт 800")
async def specification(message: types.Message):
    await message.reply("Общая длина: 160 см \n"
                        "Высота: 100 см \n"
                        "Вес: 65 кг \n"
                        "Длина жаровни: 80 см \n"
                        "Толщина стали: 5 мм\n")

@dp.message(F.text.lower() == "б лофт 1000")
async def specification(message: types.Message):
    await message.reply("Общая длина: 180 см \n"
                        "Высота: 100 см \n"
                        "Вес: 75 кг \n"
                        "Длина жаровни: 100 см \n"
                        "Толщина стали: 5 мм\n")

@dp.message(F.text.lower() == "б800 с печью")
async def specification(message: types.Message):
    await message.reply("Общая длина: 175 см \n"
                        "Высота: 100 см \n"
                        "Вес: 150 кг \n"
                        "Длина жаровни: 80 см \n"
                        "Толщина стали: 5 мм\n")



@dp.message(Command("info2"))
async def cmd_info(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Б1000 с навесом"),
            types.KeyboardButton(text="Б800 с навесом"),
            types.KeyboardButton(text="Б Лофт 1000 с навесом"),
            types.KeyboardButton(text="Б Лофт 800 с навесом"),
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери интересующее"
    )
    await message.answer('Барбекю было сокращено как "Б"', reply_markup=keyboard)

@dp.message(F.text.lower() == "б1000 с навесом")
async def specification(message: types.Message):
    await message.reply("Общая длина: 192 см \n"
                        "Высота: 220 см \n"
                        "Вес: 130 кг \n"
                        "Длина жаровни: 100 см \n"
                        "Толщина стали: 5 мм\n")

@dp.message(F.text.lower() == "б800 с навесом")
async def specification(message: types.Message):
    await message.reply("Общая длина: 172 см \n"
                        "Высота: 220 см \n"
                        "Вес: 120 кг \n"
                        "Длина жаровни: 80 см \n"
                        "Толщина стали: 5 мм\n")

@dp.message(F.text.lower() == "б лофт 1000 с навесом")
async def specification(message: types.Message):
    await message.reply("Общая длина: 179 см \n"
                        "Высота: 220 см \n"
                        "Вес: 130 кг \n"
                        "Длина жаровни: 100 см \n"
                        "Толщина стали: 5 мм\n")

@dp.message(F.text.lower() == "б лофт 800 с навесом")
async def specification(message: types.Message):
    await message.reply("Общая длина: 159 см \n"
                        "Высота: 220 см \n"
                        "Вес: 115 кг \n"
                        "Длина жаровни: 80 см \n"
                        "Толщина стали: 5 мм\n")



@dp.message(Command("info3"))
async def cmd_info(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Б800 с навесом и печью"),
            types.KeyboardButton(text="Б Лофт 800 с навесом и печью"),
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери интересующее"
    )
    await message.answer('Барбекю было сокращено как "Б"', reply_markup=keyboard)


@dp.message(F.text.lower() == "б800 с навесом и печью")
async def specification(message: types.Message):
    await message.reply("Общая длина: 183 см \n"
                        "Высота: 220 см \n"
                        "Вес: 195 кг \n"
                        "Длина жаровни: 80 см \n"
                        "Толщина стали: 5 мм\n")


@dp.message(F.text.lower() == "б лофт 800 с навесом и печью")
async def specification(message: types.Message):
    await message.reply("Общая длина: 185 см \n"
                        "Высота: 220 см \n"
                        "Вес: 220 кг \n"
                        "Длина жаровни: 80 см \n"
                        "Толщина стали: 5 мм\n")



@dp.message(Command("info4"))
async def cmd_info(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Модульный Лофт навес"),
            types.KeyboardButton(text="Модульный навес"),
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери интересующее"
    )
    await message.answer('Навес - отличное дополнение к вашему мангалу!', reply_markup=keyboard)


@dp.message(F.text.lower() == "модульный лофт навес")
async def specification(message: types.Message):
    await message.reply("Общая длина: 198 см \n"
                        "Высота: 220 см \n"
                        "Вес: 87 кг \n")


@dp.message(F.text.lower() == "модульный навес")
async def specification(message: types.Message):
    await message.reply("Общая длина: 178 см \n"
                        "Высота: 220 см \n"
                        "Вес: 60 кг \n")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())