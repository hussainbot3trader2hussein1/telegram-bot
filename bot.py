import telebot

TOKEN = "8367363898:AAEos27ddpK5GzB1EmteTBjKfhC9y3QJYEI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 هلا بيك! هذا بوت تجريبي.\n\nالأوامر:\n/buy صعود 📈\n/sell نزول 📉\n/help مساعدة")

@bot.message_handler(commands=['buy'])
def buy(message):
    bot.reply_to(message, "📈 إشارة صعود (ديمو فقط)")

@bot.message_handler(commands=['sell'])
def sell(message):
    bot.reply_to(message, "📉 إشارة نزول (ديمو فقط)")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "🧪 هذا بوت تجريبي بدون ربح حقيقي.")

bot.infinity_polling()
