from aiogram.types import Message
from loader import dp
from utils.misc.throttling import rate_limit
from nlp.chat import speak

# @rate_limit(3, 'start')
@dp.message_handler(content_types=['text'], state='*')
async def nlp(message: Message):
    print('message', message.text)
    text=speak(message.text)
    print(text)
    await message.answer(text)