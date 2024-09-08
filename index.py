from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Play Game", url="https://your-game-url.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Click below to start the game:', reply_markup=reply_markup)

def main():
    updater = Updater("7016641965:AAEojr8sPFuoNIpXo8LVzglg9y6MTUtds9U", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

