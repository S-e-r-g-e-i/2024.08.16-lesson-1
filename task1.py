# Пространство имён (Задача "Счётчик вызовов")
calls = 0


def count_calls():  # подсчитывающая вызовы остальных функций
    global calls
    calls = calls + 1


def string_info(string):    #принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    count_calls()
    cortege_string = (len(string), string.upper(), string.lower())
    print(cortege_string)


def is_contains(sting, list_to_search):    # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN
    count_calls()
    cortege_string_list_to_search = (sting, list_to_search)
    for i in range(0, len(list_to_search), 1):
        if sting.upper() == list_to_search[i].upper():
            print(True)
            break
        else:
            if i == len(list_to_search) - 1:
                print(False)
            continue

string_info('ArOnoV')
string_info('OrLoV')
is_contains('Aronov', ['ArovoN', 'AronoV', 'noVar', 'VoNoRa'])
is_contains('Orlov', ['orLon', 'LOvaR', 'Vorla', 'orLovA'])
print(calls)
