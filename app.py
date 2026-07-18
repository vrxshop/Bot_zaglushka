import os
import asyncio
import threading
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# ==================================================
# FLASK ДЛЯ RENDER
# ==================================================
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "🤖 Бот работает!"

@flask_app.route('/health')
def health():
    return "OK", 200

# ==================================================
# КОНФИГУРАЦИЯ
# ==================================================
BOT_TOKEN = "ТВОЙ_ТОКЕН_СЮДА"  # ← ЗАМЕНИ НА СВОЙ ТОКЕН!

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# ==================================================
# ХЭНДЛЕРЫ
# ==================================================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = """🚀 <b>Бот переехал!</b>

Мы переехали на новый, более быстрый и удобный бот.

👉 <b>Переходите по ссылке:</b> <a href="https://t.me/Jfuglbot">@Jfuglbot</a>

Все доступы и бонусы сохранены. Подписка переносится автоматически.

Спасибо, что вы с нами! ❤️"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 ПЕРЕЙТИ В НОВЫЙ БОТ", url="https://t.me/Jfuglbot")]
    ])

    await message.answer(text, reply_markup=keyboard, disable_web_page_preview=False)

@dp.message()
async def any_message(message: types.Message):
    """На любое сообщение отвечаем ссылкой на новый бот"""
    text = """🚀 <b>Бот переехал!</b>

👉 <b>Переходите по ссылке:</b> <a href="https://t.me/Jfuglbot">@Jfuglbot</a>

Все доступы и бонусы сохранены."""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 ПЕРЕЙТИ В НОВЫЙ БОТ", url="https://t.me/Jfuglbot")]
    ])

    await message.answer(text, reply_markup=keyboard, disable_web_page_preview=False)

# ==================================================
# ЗАПУСК
# ==================================================
async def main():
    print("=" * 60)
    print("🚀 БОТ-РЕДИРЕКТ ЗАПУЩЕН!")
    print("📌 Все сообщения перенаправляют на @Jfuglbot")
    print("=" * 60)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print("✅ Flask запущен в фоновом потоке!")
    asyncio.run(main())
