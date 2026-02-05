import os
import telebot
from flask import Flask
from threading import Thread

# Это "заглушка", чтобы Koyeb не выключал бота
app = Flask('')
@app.route('/')
def home():
    return "Бот запущен и работает!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Основной код бота
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я твой бот, успешно запущенный на Koyeb.")

if __name__ == "__main__":
    Thread(target=run).start()
    print("Бот поехал...")
    bot.infinity_polling()
