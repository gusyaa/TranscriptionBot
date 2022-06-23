import requests
from bs4 import BeautifulSoup
import telebot

API_KEY = '' ## токен
    
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Введите слово:')

@bot.message_handler(content_types=['text'])

def tran(message):
    url = f'https://wooordhunt.ru/word/{message.text.lower()}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    reqWords = soup.find_all('span', class_='transcription')
    bot.send_message(message.chat.id, reqWords)
        
bot.polling()
