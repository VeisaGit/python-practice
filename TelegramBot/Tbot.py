from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext
from telegram.ext import Filters, MessageHandler
from Commands import *
from db import *


def main():
    print('start')
    updater = Updater(
        token='1093115241:AAHC4pU5yX1w9jhPRkcXEqv9Wy_REo8C8Mc',
        use_context=True,
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling() #делает работу бота постоянной
    updater.idle()


def message_handler(update: Update, context: CallbackContext):
    text = update.effective_message.text
    user = update.effective_user

    if text == '110 70':
        update.message.reply_text(check_user_message(text,user), parse_mode=ParseMode.HTML)

        add_message(
            user_id=user.id,
            text=text,)

    elif text == 'Инструкции':
        update.message.reply_text(instructions(text), parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(alternative_message(text), parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    main()