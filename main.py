import telebot
import requests

# Telegram bot tokenini kiritish
TOKEN = "7710185819:AAFl02pgP1yJ5FnYiQaKqs9m7DWOz8LiUUQ"  # Bot tokeningizni bu yerga joylashtiring
bot = telebot.TeleBot(TOKEN)

# Video yuklab olish uchun API URL (o'zingizning API URL'ni o'zgartiring)
API_URL = "https://some-video-api.com/download"  # Bu yerga videolarni yuklash uchun kerakli API URL'ni qo'yish

# /start komandasi
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Salom! Instagram yoki TikTok havolasini yuboring, men videoni yuklab beraman.")

# URL yuborilganida video yuklash
@bot.message_handler(func=lambda msg: msg.text.startswith("http"))
def download_video(message):
    url = message.text
    bot.reply_to(message, "Videoni yuklab olyapman, kuting...")
    try:
        # API’ga so‘rov yuborish
        response = requests.get(API_URL, params={"url": url})
        if response.status_code == 200:
            video = response.content
            bot.send_video(message.chat.id, video, caption="Mana, videongiz!")
        else:
            bot.reply_to(message, "Uzr, videoni yuklab bo'lmadi. Boshqa link yuboring.")
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {str(e)}")

# Botni ishga tushirish
bot.polling()