import datetime
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import logging
from aiogram import Bot, types
import json
from aiogram.dispatcher.filters import Command
#from module import Camera as cam
#from module import ObjectDetection as obj


# Threshhold Limit text filt to Dic
limit = {}
with open('threshold.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    key, value = line.strip().split(' : ')
    limit[key] = int(value)
print("Current Threshold Limit : ", limit)

new_limit = {}


# Bot Setup
bot = Bot(token="6197668602:AAHa4cgaujaHoy0yhqzfIefCjHgkBO_id_I")
chatid = 986316612 ##Deep
vendor = 5292090196

dp = Dispatcher(bot, storage=MemoryStorage())


def check_user(a):
    if chatid == a:
        return True
    else:
        return False

# Define your states


class Limitinfo(StatesGroup):
    tomato = State()
    banana = State()


# Inline Buttons for Telegram
btn1 = KeyboardButton('/start')
btn2 = KeyboardButton("Manual Order")
btn3 = KeyboardButton("Latest Stock")
btn4 = KeyboardButton("Latest Photo")
btn5 = KeyboardButton("/Change_Items_Quantity")
btn6 = KeyboardButton("Order Status")
btn7 = KeyboardButton("Order History")
btn8 = KeyboardButton("Mark Delivered")
btn9 = KeyboardButton("Check_Current_Limit")
kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    btn1, btn2).add(btn3, btn4).add(btn5,btn9).add(btn6, btn7).add(btn8)


# Handling Telegram Messages
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    print(f"Name: {message.from_user.first_name} Id: {message.chat.id} Started Bot")
    await message.answer(f"Hello {message.from_user.first_name}, Welcome This is SmartFridge Bot", reply_markup=kb1)




@dp.message_handler()
async def welcome(message: types.Message):
    if check_user(message.chat.id):
        
        # Latest Photo
        if message.text == "Latest Photo":
            print("Requested for Latest Photo")
            try:
                with open('time.txt', 'r') as file:
                    time = file.read()
                await bot.send_photo(message.chat.id, open("./image/autoimage.jpg", 'rb'), f"\nCaptured at :\n{time}")
            except:
                await message.answer("Something Wents Wrong. Try Again")

        # Manual Order
        if message.text == "Manual Order":
            await message.answer('Please choose an option:')

        ## Check_Current_Limit
        if message.text == "Check_Current_Limit":
            a = ""
            for key, value in limit.items():
                a += key + " : " + str(value) + "\n"
            print(a)
            await message.answer(f"Current Limit is: \n {a}")
            

        # Latest Stock
        if message.text == "Latest Stock":

            print("Requested for LatestStock")
            a = obj.classify('./image/autoimage.jpg')
            if isinstance(a, str):
                await message.answer("Something Wents Wrong !! Try Again.")
            elif isinstance(a, dict):
                with open('time.txt', 'r') as file:
                    time = file.read()
                print("Latest Stock:", a)
                msg = "\n".join(
                    [f"{key}: {value}" for key, value in a.items()])
                await message.answer(f"Latest Stock Update.\nTime:{time}):\n\n{msg}")

        # Order Status
        if message.text == "Order Status":
            print("Requested for Order Status")
            with open('order.txt', 'r') as hf:
                data = hf.read()
                if data:
                    await message.answer(f"Order Status:\n\n{data}")
                else:
                    await message.answer("No Order Status Found !!")
        

        # Order History
        if message.text == "Order History":
            print("Requested for Order History")
            with open('Order_History.txt', 'r') as hf:
                data = hf.read()
                if data:
                    await message.answer(f"Order History:\n\n******************\n{data}")
                else:
                    await message.answer("No Order History Found !!")
        # Order History
        if message.text == "Manual Order":
            await message.answer("Please Order Directly to Vendor: @vendorpromax")
            

    # Vendor Mark Delivered
    elif message.chat.id == vendor:
        if message.text == "Mark Delivered":
            print("Requested for Mark Delivered")
            with open("order.txt", "r") as f1:
                data = f1.read()
                if data:
                    data = data.replace("Pending", "Delivered")
                    print(data)
                    with open("Order_History.txt", "a") as f2:
                        f2.write(f"{data}Delivered_Date:{datetime.datetime.now().strftime('%I:%M %p %d-%m-%Y')}\n******************\n")
                    with open("order.txt", "w") as f3:
                        pass
                    await message.answer("Done !!")
                else:
                    await message.answer("No Order Found !!")
                
    else:
        await message.answer("You are not valid user !!")



print("Bot is Running...")
executor.start_polling(dp)
