import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from bs4 import BeautifulSoup
import requests
TOKEN = '6625359880:AAFz1rAcuQj-7YZfu5hX42A9jcQNxFHNh_E'
bot = telebot.TeleBot(TOKEN)

info_genre = {}
dict_name_btn = {'Comedy': 'Комедия', 'Romantic': 'Романтика', 'Sport': 'Спорт', 'School': 'Школа', }
web_app = WebAppInfo(url="https://sergeykopko.github.io/anime.github.io/")
#start bot
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text='Выберите жанр и аниме:', web_app=web_app))
    bot.send_message(message.chat.id, f"""Даттебайо! (<i>だってばよ</i>)\n Я девчонка <b style="color:red;">Sakura</b>! Я помогу тебе в поиске аниме на твой вкус :з\n Нажмите "Выбрать жанр", чтобы начать свое путешествие! """, parse_mode="html", reply_markup=markup)




bot.infinity_polling(none_stop=True, interval=0)



