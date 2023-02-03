# 1.Создайте любую программу.py при помощи виртуального окружения и PIP.
# Отправте репозиторий где будет этот файл и файл requirements.txt
# 2.Создайте любого бота телеграмм(можно самый простой), главное чтобы у
# вас к след. уроку был свой бот в телеграмме, в нем вы сможете работать над
# созданием нового бота на 10 семинаре.

from aiogram import Bot, Dispatcher, types, executor
import datetime


async def on_start(_):
    print('Бот запущен!')

bot = Bot('')
dp = Dispatcher(bot)


@dp.message_handler(lambda message: message.text == 'foo')


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.reply(f'Привет, {message.from_user.first_name}!\nЕсли \
хочешь узнать время - напиши /time')


@dp.message_handler(commands=['time'])
async def mes_time(message: types.Message):
    await message.reply(f'{datetime.datetime.now()}!')


@dp.message_handler()
async def mes_all(message: types.Message):
    await message.reply(f'{message.from_user.full_name}, смотри, что я поймал - {message.text}!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)