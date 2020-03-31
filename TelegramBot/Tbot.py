from telegram import Update
from telegram.ext import Updater, CallbackContext
from telegram.ext import Filters, MessageHandler
from .Commands import *


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == '110/70':
        update.message.reply_text(
            text="Спасибо, запись добавлена в дневник!")
    elif text == 'Инструкции':
        update.message.reply_text(
            text="Чтобы фиксировать артериальное давление в дневник, нужно вводить его в определенном формате - \"Систолическое Дитолическое\" через пробел. Например: 110 70. Также бот может отправлять вам статистику за день, неделю, месяц сюда или на эл. почту.")
    else:
        update.message.reply_text(
            text="Привет, я бот, которой поможет тебе вести дневник измерений артериального давления. Еще я могу возвращать статистику. Введите \"Инструкции\", чтобы понять, как заносить данные в дневник. Введите \"Команды\", чтобы узнать, что еще я умею.")

def main():
    print('Start')
    updater = Updater(
        token='1093115241:AAHC4pU5yX1w9jhPRkcXEqv9Wy_REo8C8Mc',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

if __name__ =='__main__':
    main()