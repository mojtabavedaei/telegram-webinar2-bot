import telebot
import random

BOT_TOKEN = "8930390321:AAGHZWYO4t_1bB84FtPKqsU5AfPgPfYJzRg"

bot = telebot.TeleBot(BOT_TOKEN)

user_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_state[chat_id] = {"step": "name"}
    bot.reply_to(message, "سلام 🌿\nبرای ثبت‌نام وبینار، لطفاً نام و نام خانوادگی خود را وارد کنید:")

@bot.message_handler(func=lambda m: True)
def handle(message):
    chat_id = message.chat.id

    if chat_id not in user_state:
        bot.reply_to(message, "لطفاً /start را بزنید تا ثبت‌نام شروع شود.")
        return

    step = user_state[chat_id]["step"]

    if step == "name":
        user_state[chat_id]["name"] = message.text
        user_state[chat_id]["step"] = "age"
        bot.reply_to(message, "سن خود را وارد کنید:")

    elif step == "age":
        user_state[chat_id]["age"] = message.text
        user_state[chat_id]["step"] = "marital"
        bot.reply_to(message, "وضعیت تأهل خود را وارد کنید (مجرد / متأهل):")

    elif step == "marital":
        user_state[chat_id]["marital"] = message.text
        user_state[chat_id]["step"] = "phone"
        bot.reply_to(message, "شماره تماس خود را وارد کنید:")

    elif step == "phone":
        user_state[chat_id]["phone"] = message.text

        tracking_code = "WB-" + str(random.randint(10000, 99999))
        user_state[chat_id]["tracking"] = tracking_code

        bot.reply_to(
            message,
            f"ثبت‌نام شما انجام شد ✅\n"
            f"کد رهگیری: {tracking_code}\n"
            f"لینک وبینار بعداً برای شما ارسال خواهد شد."
        )

        del user_state[chat_id]

bot.polling()
