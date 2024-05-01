import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="6197668602:AAHa4cgaujaHoy0yhqzfIefCjHgkBO_id_I")
dp = Dispatcher(bot)

items = ['Apple', 'Banana', 'Egg', 'Milk']

# Define the handler for the inline keyboard
@dp.callback_query_handler(lambda c: c.data in items)
async def process_callback_quantity(callback_query: types.CallbackQuery):
    item = callback_query.data
    await bot.answer_callback_query(callback_query.id)

    # Ask for the quantity
    quantity_keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in range(1, 10):
        button = types.InlineKeyboardButton(text=str(i), callback_data=str(i))
        quantity_keyboard.add(button)
    await bot.send_message(callback_query.from_user.id, f"How many {item}s would you like?", reply_markup=quantity_keyboard)

    # Define a new callback handler for the quantity
    @dp.callback_query_handler(lambda c: c.data.isdigit() and 0 < int(c.data) < 10)
    async def process_quantity(callback_query: types.CallbackQuery):
        quantity = callback_query.data
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(5292090196, f"{quantity} {item}s ordered.")
        await bot.send_message(callback_query.from_user.id, "Order placed.")

    # Register the new callback handler
    dp.register_callback_query_handler(process_quantity)

# Define the handler for the "/start" command
@dp.message_handler(commands=['/start'])
async def send_inline_keyboard(message: types.Message):
    # Create the inline keyboard
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    for item in items:
        button = types.InlineKeyboardButton(text=item, callback_data=item)
        inline_keyboard.add(button)

    # Send the inline keyboard
    await bot.send_message(message.chat.id, "Choose an item:", reply_markup=inline_keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
