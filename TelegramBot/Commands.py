import re
'''
List of commands for GodFatherBot
instructions - посмотреть инструкции
bot - информация о боте
'''

def statistic():
    pass

def report():
    pass

def instructions(text):
    text = "Чтобы фиксировать артериальное давление в дневник, нужно вводить его в определенном формате: \n\n \"<b>Систолическое Дистолическое</b>\"\n\n" \
           "через пробел. Например:\n\n <b>\"110 70\"</b>\n\nТакже бот может отправлять вам статистику за день, неделю, месяц сюда или на эл. почту."
    return text

def alternative_message(text):
     text = "Я бот, которой помогает вести дневник измерений артериального давления. Введите косую черту: <b>\"/\"</b>, чтобы посмотерть список доступных команд"
     return text

def successful_user_message(user):
    text = f"Спасибо, {user.first_name}! Запись добавлена в дневник."
    return text


def processing_user_input(text):
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