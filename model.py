from aiogram import Bot, Dispatcher, executor, types
from pycbrf import ExchangeRates
from datetime import date

TOKEN = '5505836319:AAFIQ0x1PVZu8HMebi6VBGEgqNM7K87dnZI'

bot = None
dp = None

def tg_init():
    global bot, dp
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        await message.reply(f'Введите код валюты (форматы: USD; R01235; 840)')
    
    @dp.message_handler()
    async def echo(message: types.Message):
            t = date.today()
            tf = "{}-{}-{}".format(t.year, t.month, t.day)
            r = get_rates(tf, message.text)
            if r == None:
                await message.answer(f'Валюта не найдена!')
            else:                 
                await message.answer(f'Курс валюты {r[1]} на дату {tf} равен {r[6]}')
    executor.start_polling(dp, skip_updates=True)

def get_rates(date: str, code: str):
    rates = ExchangeRates(date)
    return rates[code]