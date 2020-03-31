from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext
from telegram.ext import Filters, MessageHandler
from Commands import *


def main():
    print('Start')
    updater = Updater(
        token='1093115241:AAHC4pU5yX1w9jhPRkcXEqv9Wy_REo8C8Mc',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling() #делает работу бота постоянной
    updater.idle()

def message_handler(update: Update, context: CallbackContext):
    text = update.message.text

    if text:
        update.message.reply_text(check_user_message(text), parse_mode=ParseMode.HTML)
    elif text == 'Инструкции':
        update.message.reply_text(instructions(text), parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(alternative_message(text), parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    main()