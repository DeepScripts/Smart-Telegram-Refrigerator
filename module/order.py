# bot.py

import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Initialize the bot and dispatcher objects
bot = Bot(token="6197668602:AAHa4cgaujaHoy0yhqzfIefCjHgkBO_id_I")
dp = Dispatcher(bot)
chat_id = '5292090196'
# Define the method that will be called to send the message
async def send_message(a):
    orderlist = a
    message = "Please Deliver items as below\n"
    for key in orderlist:
        message += f"{key} : {str(orderlist[key])} \n"
    await bot.send_message(chat_id, message)


# Define the command handler that will call the `send_message` method
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    chat_id = message.chat.id
    await send_message(chat_id)


# Start the event loop and run the bot
async def main():
    await bot.start_polling()
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    executor.start(dp, loop=loop)
