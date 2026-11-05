import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, MenuButtonWebApp

# 1. BotFather-dan olgan API TOKEN'ingizni shu yerga yozing:
BOT_TOKEN = "8936658941:AAGif7NekAlLfbMQPn2t__XxNXK73oH734I"

# 2. Vercel, Netlify yoki GitHub Pages'ga yuklagan Mini App havolangizni yozing:
WEB_APP_URL = "https://rasta-mini-app.vercel.app"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    """
    /start buyrug'i kelganda foydalanuvchiga Mini App tugmasi bilan xabar yuborish
    """
    # Inline WebApp tugmasini yaratish
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Rasta B2B Mini App-ni Ochish",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )

    welcome_text = (
        f"Salom, <b>{message.from_user.first_name}</b>! 👋\n"
        f"<b>Rasta B2B</b> rasmiy botiga xush kelibsiz.\n"
        f"Do'koningiz uchun ulgurji mahsulotlarni buyurtma qilish va firmalar "
        f"katalogini ko'rish uchun quyidagi tugmani bosing:"
    )

    await message.answer(welcome_text, parse_mode="HTML", reply_markup=keyboard)


async def set_main_menu():
    """
    Botning chap pastki burchagidagi Menyu (Menu Button) tugmasiga Mini App-ni ulash
    """
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="🚀 Rasta B2B",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    )

async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    # Menyu tugmasini sozlash
    await set_main_menu()
    # Botni ishga tushirish (Polling)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi!")