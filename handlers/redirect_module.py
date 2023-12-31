from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.types.message import ContentType
from config import aiogram_bot, from_channel, target_channel, bot_status
import json
from handlers.json_actions import *
router = Router()

counter = 2
id_list = []
json_path = 'id_history.json'

async def get_order_id(message: Message):
    message_words = message.text.split()
    for i in message_words:
        if i.startswith('#id'):
            return i


@router.channel_post()
async def monitor_chat(message: Message):
    print(message.chat.id)
    print(id_list)
    if await bot_status.get_status() is False:
        return
    if message.chat.id != from_channel:
        return

    print(f'new message: \n{message.text}')
    global counter
    if any(x.lower() in message.text.lower() for x in ['new order', 'modified', 'pending order', 'closed', 'daily report', 'weekly report', 'monthly report']):
        order_id = await get_order_id(message)
        orders_json = await load_id_list_from_json(json_path)
        print('new order')
        if 'NEW ORDER' in message.text:
            counter += 1
            print(f'NEW_ORDERS_COUNTER: {counter}')
            if counter % 3 == 0:
                mess_id = message.message_id
                await aiogram_bot.forward_message(target_channel, message.chat.id, mess_id)
                id_list.append(order_id)
                await add_id_to_json(order_id, json_path)
                print(f'order id: {order_id} added to resended list')

        elif 'MODIFIED' in message.text:
            print(type(order_id), type(id_list))
            if order_id in orders_json:
                print(f'order id: {order_id} in resended list')
                await aiogram_bot.forward_message(target_channel, message.chat.id, message.message_id)
                print('Message forwarded')

        elif 'PENDING ORDER' in message.text:
            if order_id in orders_json:
                print(f'order id: {order_id} in resended list')
                await aiogram_bot.forward_message(target_channel, message.chat.id, message.message_id)
                print('Message forwarded')

        elif 'CLOSED' in message.text:
            if order_id in orders_json:
                print(f'order id: {order_id} in resended list')
                await aiogram_bot.forward_message(target_channel, message.chat.id, message.message_id)
                await remove_id_from_json(order_id, json_path)
                print('Message forwarded and deleted from id_list')

        elif 'DAILY REPORT' in message.text:
            await aiogram_bot.forward_message(target_channel, message.chat.id, message.message_id)
            print('Daily report forwarded')

        elif 'WEEKLY REPORT' in message.text:
            await aiogram_bot.forward_message(target_channel, message.chat.id, message.message_id)
            print('Weekly report forwarded')

        elif 'MONTHLY REPORT' in message.text:
            await aiogram_bot.forward_message(target_channel, message.chat.id, message.message_id)
            print('Weekly report forwarded')