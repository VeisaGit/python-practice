import re
'''
List of commands for GodFatherBot
instructions - посмотреть инструкции
bot - информация о боте
average - среднее за последние 30 дн.
export30 - журнал за последние 30 дн.
'''

def average_mean_30d():
    #TODO: Включить сюда среднее значение за последние 30 дней.
    pass

def notifications():
    #TODO: рассмотреть необходимость интеграции напоминания померить давление
    pass

def report():
    # TODO: Включить сюда отправку отчета на почту. Или файлом в ответ пользователю.
    pass

def instructions(text):
    text = "Чтобы внести показания артериального давления в дневник, введите их в формате: \n\n \"<b>Систолическое Дистолическое</b>\"\n\n" \
           "через пробел. Например:\n\n <b>\"110 70\"</b>\n\nТакже бот добавит к записи текущее число и время.\nЕще бот может отправлять вам статистику за месяц.\n " \
           "Введите косую черту: <b>/</b>, чтобы посмотерть список доступных команд."
    # TODO: в будущем добавить статистику за неделю. День ?
    return text

def information_about_bot(text):
     text = "Я бот, которой помогает вести дневник измерений артериального давления. Введите косую черту: <b>/</b>, чтобы посмотерть список доступных команд"
     return text

def successful_user_message(user):
    text = f"Спасибо, {user.first_name}! Запись добавлена в дневник."
    return text


def processing_user_input(text):
    """
    Функция выбирает из пользовательского ввода показания давления. К внесению в журнал допускаюся только совпадения с шаблонами:
    • 110 70
    • 110 100
    • 99 70
    • 99 100
    :param text: ввод пользователя
    :return: одно из совпадений, если найдено
    """
    v1 = re.fullmatch(r'\d\d\d\s\d\d\d', text)
    v2 = re.fullmatch(r'\d\d\d\s\d\d', text)
    v3 = re.fullmatch(r'\d\d\s\d\d\d', text)
    v4 = re.fullmatch(r'\d\d\s\d\d', text)

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