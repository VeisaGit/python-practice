from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext
from telegram.ext import Filters, MessageHandler
from Commands import *
from db import *
import datetime
import re


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
    date = datetime.datetime.today()
    date = date.strftime("%d/%m/%Y %Hч %Mм")

    pressure_value = processing_user_input(text)
    systolic_pressure_value = pressure_value[0]
    diastolic_pressure_value = pressure_value[1]

    update.message.reply_text(check_user_message(systolic_pressure, diastolic_pressure, user, date), parse_mode=ParseMode.HTML)

    add_message_to_db(
        user_id=user.id,
        systolic_pressure=systolic_pressure_value,
        diastolic_pressure=diastolic_pressure_value,
        date=date,)


    # elif text == 'Инструкции'
    #         :
    #     update.message.reply_text(instructions(text), parse_mode=ParseMode.HTML)
    # else:
    #     # update.message.reply_text(alternative_message(text), parse_mode=ParseMode.HTML)
    #     update.message.reply_text('this is shit')


if __name__ == '__main__':
    systolic_pressure = 0
    diastolic_pressure = 0
    main()