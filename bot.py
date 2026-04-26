import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- CONFIGURATION ---
BOT_TOKEN = '8645025009:AAG9twtXsCS1i0ZbKvGRxx0Xj8OPjjuERqI'
bot = telebot.TeleBot(BOT_TOKEN)
BOT_USERNAME = 'Sandhya_Singh1_bot' 

# --- STICKERS ---
WELCOME_STICKER = 'CAACAgIAAxkBAAERHnlp7cT7370uNe00Gpzjx0w0Bgv7nAACFSIAAuRbEEq_alAESmP76zsE'
AGE_STICKER = 'CAACAgUAAxkBAAERHndp7cSsXXQdvo3TjhH0GfiDgZwC3wAC5Q4AAjJYSFa6Uuwv1lsKsTsE'

# --- 1. START COMMAND ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_sticker(message.chat.id, WELCOME_STICKER)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("➕ Add to Group", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
               InlineKeyboardButton("😎 Owner", url="https://t.me/Rockmishra20"))
    
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}! 👋\nI am @{BOT_USERNAME}. Rock Mishra's personal assistant from Nepal! 🇳🇵", reply_markup=markup)

# --- 2. SMART CHAT LOGIC ---
@bot.message_handler(func=lambda message: True)
def handle_chat(message):
    text = message.text.lower()
    chat_id = message.chat.id
    user_name = message.from_user.first_name

    # Age / Umra Query (Naya Feature!)
    if any(word in text for word in ['age', 'umra', 'kitne saal ke ho', 'umar']):
        bot.send_sticker(chat_id, AGE_STICKER)
        replies = [
            f"Bhai, main toh digital hoon, meri age toh har update ke sath badhti hai! वैसे रॉक मिश्रा ने मुझे अभी हाल ही में बनाया है। 😎",
            f"Umar mein kya rakha hai {user_name}? Dil toh bacha hai ji! 🤖✨",
            f"Meri age? Jitni der se tum mujhse chat kar rahe ho, bas utni hi hai! 😂"
        ]
        bot.reply_to(message, random.choice(replies))

    # Baki Purane Replies
    elif any(word in text for word in ['hi', 'hello', 'namaste']):
        bot.reply_to(message, f"Hello {user_name}! How's it going?")

    elif 'nepal' in text or 'kahan se ho' in text:
        bot.reply_to(message, "I'm from the beautiful mountains of Nepal! 🇳🇵")

    elif 'owner' in text or 'rock mishra' in text:
        bot.reply_to(message, "Rock Mishra (@Rockmishra20) is my creator and the best boss! 😎🔥")

# Fast Polling
if __name__ == "__main__":
    print(f"Bot @{BOT_USERNAME} is online and knows its age! 🚀")
    bot.polling(non_stop=True, interval=0, timeout=20)
    
