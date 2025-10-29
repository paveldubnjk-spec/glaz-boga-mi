import telebot
from telebot import types

TOKEN = "ВСТАВЬ_СВОЙ_ТОКЕН_СЮДА"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("ℹ️ О боте")
    btn2 = types.KeyboardButton("📸 Фото")
    btn3 = types.KeyboardButton("🌐 Сайт")
    btn4 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! 👋\nВыбери действие ниже:", reply_markup=markup)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "ℹ️ О боте":
        bot.send_message(message.chat.id, "Я пример Telegram-бота, созданного на Python 🐍.")
    elif message.text == "📸 Фото":
        photo_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"
        bot.send_photo(message.chat.id, photo_url, caption="Вот фото 🐱")
    elif message.text == "🌐 Сайт":
        bot.send_message(message.chat.id, "Открой мой сайт: https://example.com 🌍")
    elif message.text == "❓ Помощь":
        bot.send_message(message.chat.id, "Напиши /start чтобы открыть меню снова 😊")
    else:
        bot.send_message(message.chat.id, "Я не понимаю эту команду 😅")
print("🤖 Бот запущен с главным меню...")
bot.polling()
python bot.py
я вставел в папку в блокнотеimport telebot
from telebot import types  # для кнопок

# 🔑 Вставь сюда свой токен
TOKEN = "7951898649:AAFy6dFXmxXNyUxxrIJW5LelNoQFVYLxWIM"

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🧠 Помощь")
    btn2 = types.KeyboardButton("ℹ️ Инфо")
    btn3 = types.KeyboardButton("👁 О создателе")
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "👋 Привет! Я — Глаз Бога.\nВыбери действие ниже:",
        reply_markup=markup
    )

# Обработка всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "🧠 Помощь":
        bot.send_message(
            message.chat.id,
            "Вот что я умею:\n"
            "✅ /start — начать\n"
            "✅ /help — список команд\n"
            "✅ /info — информация обо мне"
        )
    elif message.text == "ℹ️ Инфо":
        bot.send_message(
            message.chat.id,
            "👁 Я — бот, созданный на Python с библиотекой Telebot."
        )
    elif message.text == "👁 О создателе":
        bot.send_message(
            message.chat.id,
            "Мой создатель — ты! 😎"
        )
    else:
        bot.send_message(message.chat.id, f"Ты написал: {message.text}")

print("🤖 Бот запущен с кнопками...")
bot.polling()
SS