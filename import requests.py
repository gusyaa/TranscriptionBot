from msilib.schema import Error
import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://wooordhunt.ru/word/heritage' ## ссылка на слово для парсинга
API_KEY = '5538778970:AAF_yxIXqIUEcNCiYP5QynoNaq-_udO0qlQ' ## токен!

def parser(url):
    
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    phWord = soup.find_all('div', class_='transcription')
    return [c.text for c in phWord]

wordlist = parser(URL)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Введите слово:')

@bot.message_handler(content_types=['text'])

def send_transcription(message):
    while True:
        try:
            bot.send_message(message.chat.id, wordlist)
            break
        except Error:
            bot.send_message(message.chat.id, 'Не удалось найти слово!')
    
bot.polling()

"""@bot.message_handler(content_types=["text"])
def handle_text(message):

    print(message)
    your_str = message.text"""