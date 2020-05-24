# - *- coding: utf- 8 - *-
import re
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext
from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from db import *

'''
/****List of commands for GodFatherBot:****/
instructions - посмотреть инструкции
bot - информация о боте
average - среднее за выбранный период.
export30 - журнал за последние 30 дн.
del - удалить последнюю запись
'''

kybrd_rmv = ReplyKeyboardRemove()


def deviation_pressure():
    systolic_deviation = int(deviation_from_normal_pressure_and_heart_rate[0][0])
    diastolic_deviation = int(deviation_from_normal_pressure_and_heart_rate[0][1])

    if systolic_pressure_value > systolic_deviation + (systolic_deviation * percent_of_deviation) \
            or diastolic_pressure_value > diastolic_deviation + (diastolic_deviation * percent_of_deviation):
        update.message.reply_text(f'{ex_mark}Введенные вами данные <u>давления</u> выше{up_red_triangle}{percent}, '
                                  f'чем средний показатель за последние 30 дней. Пожалуйста, '
                                  f'обратите на это внимание.', parse_mode=ParseMode.HTML)

    elif systolic_pressure_value < systolic_deviation - (systolic_deviation * percent_of_deviation) \
            or diastolic_pressure_value < diastolic_deviation - (diastolic_deviation * percent_of_deviation):
        update.message.reply_text(f'{ex_mark}Введенные вами данные <u>давления</u> ниже{down_red_triangle}{percent}, '
                                  f'чем средний показатель за последние 30 дней. Пожалуйста, '
                                  f'обратите на это внимание.', parse_mode=ParseMode.HTML)


def deviation_heart_rate():
    heart_deviation = int(deviation_from_normal_pressure_and_heart_rate[0][2])

    if heart_rate > heart_deviation + (heart_deviation * percent_of_deviation):
        update.message.reply_text(
            f'{ex_mark}Введенные вами данные <u>пульса</u> выше{up_red_triangle}{percent},'
            f' чем средний показатель за последние 30 дней.'
            ' Пожалуйста, обратите на это внимание.', parse_mode=ParseMode.HTML)

    elif 0 < heart_rate < heart_deviation - (heart_deviation * percent_of_deviation):
        update.message.reply_text(
            f'{ex_mark}Введенные вами данные <u>пульса</u> ниже{down_red_triangle}{percent}, '
            f'чем средний показатель за последние 30 дней.'
            ' Пожалуйста, обратите на это внимание.', parse_mode=ParseMode.HTML)


def notifications():
    # TODO: интеграция напоминания померить давление
    pass


def instructions(text):
    text = "Чтобы внести показания артериального давления в дневник, введите их в формате: \n\n \"<b>Систолическое Диастолическое</b>\"\n\n" \
           "через пробел. Например:\n\n <b>\"110 70\"</b>\n\nТакже бот добавит к записи текущее число и время.\nЕще бот может отправлять вам статистику за месяц и рассчитывать среднее.\n" \
           "<a href=\'https://teletype.in/@veisa/ND0XgFKcN\'>Подробная инструкция</a>"
    return text


def information_about_bot(text):
    text = "Я бот, которой помогает вести дневник измерений артериального давления. Введите косую черту: <b>/</b>, чтобы посмотерть список доступных команд"
    return text


def export_statistic_excel_30days(update: Update, context: CallbackContext):
    user = update.effective_user
    monthly_statistic = monthly_statistic_query(user_id=user.id)

    # TODO: возможно проблема недоступности при одновременном обращении к файлу excel решается через указание, если эта книга не доступна, использовать другую. Использовав конструкцию try-except

    # Export to excel file
    wb = Workbook()
    ws = wb.active

    ws['A1'] = 'Дата и время измерения'
    ws['B1'] = 'Систолическое'
    ws['C1'] = 'Диасталическое'
    ws['D1'] = 'Пульс'

    for row in monthly_statistic:
        ws.append(row)

    wb.save("report_30_days.xlsx")

    doc = open('report_30_days.xlsx', 'rb')
    update.message.reply_document(doc)


def successful_user_message(user):
    text = f"Спасибо, {user.first_name}! Запись добавлена в дневник."
    return text


def processing_user_input(text):
    """
    Функция выбирает из пользовательского ввода показания давления и пульса. К внесению в журнал допускаюся только совпадения с шаблонами:
    Шаблоны только для давления:
    • 100 90
    • 100 100
    • 90 100
    • 90 90
    Шаблоны для давления с пульсом:
    • 100 90 90
    • 100 90 100
    • 100 100 90
    • 100 100 100
    • 90 100 90
    • 90 100 100
    • 90 90 90
    • 90 90 100
    :param text: ввод пользователя
    :return: одно из совпадений, если найдено
    """
    space_counter = text.count(' ')

    if space_counter == 1:

        v1 = re.fullmatch(r'\d\d\d\s\d\d\d', text)  # 100 100
        v2 = re.fullmatch(r'\d\d\d\s\d\d', text)  # 100 90
        v3 = re.fullmatch(r'\d\d\s\d\d\d', text)  # 90 100
        v4 = re.fullmatch(r'\d\d\s\d\d', text)  # 90 90

        if v1:
            systolic_pressure = text[0:3]
            diastolic_pressure = text[4:7]
            return systolic_pressure, diastolic_pressure

        elif v2:
            systolic_pressure = text[0:3]
            diastolic_pressure = text[4:6]
            return systolic_pressure, diastolic_pressure

        elif v3:
            systolic_pressure = text[0:2]
            diastolic_pressure = text[3:6]
            return systolic_pressure, diastolic_pressure

        elif v4:
            systolic_pressure = text[0:2]
            diastolic_pressure = text[3:5]
            return systolic_pressure, diastolic_pressure


    elif space_counter == 2:

        v1_1 = re.fullmatch(r'\d\d\d\s\d\d\d\s\d\d', text)  # 100 100 90
        v1_2 = re.fullmatch(r'\d\d\d\s\d\d\d\s\d\d\d', text)  # 100 100 100

        v2_1 = re.fullmatch(r'\d\d\s\d\d\s\d\d', text)  # 90 90 90
        v2_2 = re.fullmatch(r'\d\d\s\d\d\s\d\d\d', text)  # 90 90 100

        v3_1 = re.fullmatch(r'\d\d\s\d\d\d\s\d\d', text)  # 90 100 90
        v3_2 = re.fullmatch(r'\d\d\s\d\d\d\s\d\d\d', text)  # 90 100 100

        v4_1 = re.fullmatch(r'\d\d\d\s\d\d\s\d\d', text)  # 100 90 90
        v4_2 = re.fullmatch(r'\d\d\d\s\d\d\s\d\d\d', text)  # 100 90 100

        if v1_1:
            systolic_pressure = text[0:3]
            diastolic_pressure = text[4:7]
            heart_rate = text[8:11]
            return systolic_pressure, diastolic_pressure, heart_rate

        elif v1_2:
            systolic_pressure = text[0:3]
            diastolic_pressure = text[4:7]
            heart_rate = text[8:12]
            return systolic_pressure, diastolic_pressure, heart_rate

        elif v2_1:
            systolic_pressure = text[0:2]
            diastolic_pressure = text[3:5]
            heart_rate = text[6:8]
            return systolic_pressure, diastolic_pressure, heart_rate

        elif v2_2:
            systolic_pressure = text[0:2]
            diastolic_pressure = text[3:5]
            heart_rate = text[6:10]
            return systolic_pressure, diastolic_pressure, heart_rate

        elif v3_1:
            systolic_pressure = text[0:2]
            diastolic_pressure = text[3:6]
            heart_rate = text[7:10]
            return systolic_pressure, diastolic_pressure, heart_rate

        elif v3_2:
            systolic_pressure = text[0:2]
            diastolic_pressure = text[3:6]
            heart_rate = text[7:11]
            return systolic_pressure, diastolic_pressure, heart_rate

        elif v4_1:
            systolic_pressure = text[0:3]
            diastolic_pressure = text[4:6]
            heart_rate = text[7:10]
            return systolic_pressure, diastolic_pressure, heart_rate

        elif v4_2:
            systolic_pressure = text[0:3]
            diastolic_pressure = text[4:6]
            heart_rate = text[7:11]
            return systolic_pressure, diastolic_pressure, heart_rate


def start_average_query(bot, update):
    reply_keyboard = [['Да', 'Нет']]
    bot.message.reply_text('Дополнить значение средним для пульса?',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                                                            one_time_keyboard=True))
    return "time_limit"


def query_with_heart_rate(bot, update):
    reply_keyboard = [['24 часа', '7 дней', '14 дней', '30 дней']]
    bot.message.reply_text('Выберите кол-во дней для расчета:',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                                                            one_time_keyboard=True))
    return "amount_of_days_pressure_with_heart_rate"


def query_without_heart_rate(bot, update):
    reply_keyboard = [['24 часа', '7 дней', '14 дней', '30 дней']]
    bot.message.reply_text('Выберите кол-во дней для расчета:',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                                                            one_time_keyboard=True))
    return "amount_of_days_pressure_without_heart_rate"


def pressure_query_without_heart_rate_1(update, context: CallbackContext):
    user = update.effective_user
    one_day_average = last_day_average_query_without_heart_rate(user_id=user.id)
    sistolic_average = one_day_average[0][0]
    diastolic_average = one_day_average[0][1]
    update.message.reply_text('Среднее значение вашего давления \nза последние 24 часа -  <b>{}/{}</b>'
                              ''.format(round(sistolic_average), round(diastolic_average)), reply_markup=kybrd_rmv,
                              parse_mode=ParseMode.HTML)

    return ConversationHandler.END


def pressure_query_without_heart_rate_7(update, context: CallbackContext):
    user = update.effective_user
    seven_day_average = seven_days_average_query_without_heart_rate(user_id=user.id)
    sistolic_average = seven_day_average[0][0]
    diastolic_average = seven_day_average[0][1]
    update.message.reply_text('Среднее значение вашего давления \nза последние 7 дней -  <b>{}/{}</b>'
                              ''.format(round(sistolic_average), round(diastolic_average)), reply_markup=kybrd_rmv,
                              parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def pressure_query_without_heart_rate_14(update, context: CallbackContext):
    user = update.effective_user
    fourteen_day_average = fourteen_days_average_query_without_heart_rate(user_id=user.id)
    sistolic_average = fourteen_day_average[0][0]
    diastolic_average = fourteen_day_average[0][1]
    update.message.reply_text('Среднее значение вашего давления \nза последние 14 дней -  <b>{}/{}</b>'
                              ''.format(round(sistolic_average), round(diastolic_average)), reply_markup=kybrd_rmv,
                              parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def pressure_query_without_heart_rate_30(update, context: CallbackContext):
    user = update.effective_user
    thirty_day_average = thirty_days_average_query_without_heart_rate(user_id=user.id)
    sistolic_average = thirty_day_average[0][0]
    diastolic_average = thirty_day_average[0][1]
    update.message.reply_text('Среднее значение вашего давления \nза последние 30 дней -  <b>{}/{}</b>'
                              ''.format(round(sistolic_average), round(diastolic_average)), reply_markup=kybrd_rmv,
                              parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def pressure_query_with_heart_rate_1(update, context: CallbackContext):
    user = update.effective_user
    one_day_average = last_day_average_query_with_heart_rate(user_id=user.id)
    sistolic_average = one_day_average[0][0]
    diastolic_average = one_day_average[0][1]
    heart_rate = one_day_average[0][2]
    update.message.reply_text('Среднее значение вашего давления \nза последние 24 часа -  <b>{}/{}</b>. \nПульса - '
                              '<b>{}</b>'.format(round(sistolic_average), round(diastolic_average), round(heart_rate)),
                              reply_markup=kybrd_rmv, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def pressure_query_with_heart_rate_7(update, context: CallbackContext):
    user = update.effective_user
    seven_day_average = seven_day_average_query_with_heart_rate(user_id=user.id)
    sistolic_average = seven_day_average[0][0]
    diastolic_average = seven_day_average[0][1]
    heart_rate = seven_day_average[0][2]
    update.message.reply_text('Среднее значение вашего давления \nза последние 7 дней -  <b>{}/{}</b>. \nПульса - '
                              '<b>{}</b>'.format(round(sistolic_average), round(diastolic_average), round(heart_rate)),
                              reply_markup=kybrd_rmv, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def pressure_query_with_heart_rate_14(update, context: CallbackContext):
    user = update.effective_user
    fourteen_day_average = fourteen_day_average_query_with_heart_rate(user_id=user.id)
    sistolic_average = fourteen_day_average[0][0]
    diastolic_average = fourteen_day_average[0][1]
    heart_rate = fourteen_day_average[0][2]
    update.message.reply_text('Среднее значение вашего давления \nза последние 14 дней -  <b>{}/{}</b>. \nПульса - '
                              '<b>{}</b>'.format(round(sistolic_average), round(diastolic_average), round(heart_rate)),
                              reply_markup=kybrd_rmv, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def pressure_query_with_heart_rate_30(update, context: CallbackContext):
    user = update.effective_user
    thirty_day_average = thirty_day_average_query_with_heart_rate(user_id=user.id)
    sistolic_average = thirty_day_average[0][0]
    diastolic_average = thirty_day_average[0][1]
    heart_rate = thirty_day_average[0][2]
    update.message.reply_text('Среднее значение вашего давления \nза последние 30 дней -  <b>{}/{}</b>. \nПульса - '
                              '<b>{}</b>'.format(round(sistolic_average), round(diastolic_average), round(heart_rate)),
                              reply_markup=kybrd_rmv, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def wrong_input(bot, update):
    bot.message.reply_text('Нажмите на одну из кнопок ниже.')
