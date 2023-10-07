import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN")
admins: list[int] = [
    420624020
]

REPORN_AN_ACCIDENT = 'Сообщить об аварии'
GET_PHONE = 'Узнать номер телефона службы'
FIND_OUT_ACCIDENT = 'Узнать ниличие аварии'
AREA_LIST = ['Центральный', 'Адлерский','Хостинский', 'Мацеста','Лазаревский']
RESOURCE_LIST = ['Газ', 'Свет', 'Вода']
RESULT_FORM = """
Тип: <b>{0}</b>
Район: <b>{1}</b>
Адресс: <b>{2}</b>
Описание: <b>{3}</b>
"""
SORRY_MESSAGE = "Извините, так я еще не умею, попробуйте написать ваш вопрос по другому или воспользуйтесь интерактивным меню!"
        
START_FORM = """
Приветствую
Ты можешь задать твой вопрос
"""

CONTACT: str = '(а тут уже ссылка на доки)'

DB_URL: str = os.getenv('MONGO_DB') if os.getenv('MONGO_DB') else 'mongodb://188.225.38.146:27017/problem'
