

def statistic():
    pass


def report():
    pass

def instructions(text):
    text = "Чтобы фиксировать артериальное давление в дневник, нужно вводить его в определенном формате - \"Систолическое Дитолическое\" " \
           "через пробел. Например: <b>110 70</b>. Также бот может отправлять вам статистику за день, неделю, месяц сюда или на эл. почту."

    return text

def alternative_message(text):
     text="Я бот, которой поможет тебе вести дневник измерений артериального давления. " \
          "Введите 'Инструкции', чтобы понять, как заносить данные в дневник. Введите \"Команды\", чтобы узнать, что еще я умею."
     return text

def check_user_message(text):
    text = "Спасибо, запись добавлена в дневник!"
    return text
