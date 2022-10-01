from datetime import datetime as dt
from time import time
# from dictionaries import dict_operations as d
from dictionaries import dict_field as d1
from dictionaries import dict_translate as d2
from dictionaries import dict_operations as d3


def value_input_logger(text, i):
    '''
    Логгер для записи значений, введенных пользователем.
    '''
    time = dt.now().strftime('%H:%M:%S')
    data_name = d2[d1[i]]
    if i == 1:
        with open('log.log', 'a', encoding='utf-8') as file:
            file.write('\n{}{}\n'.format(time, '-------НОВАЯ ЗАПИСЬ-------'))
            file.write(
                '\n{};**название поля для ввода**;{}'.format(time, data_name))
            file.write('\n{};введенное значение;{}'.format(time, text))
    else:
        with open('log.log', 'a', encoding='utf-8') as file:
            file.write(
                '\n{};**название поля для ввода**;{}'.format(time, data_name))
            file.write('\n{};введенное значение;{}'.format(time, text))


def value_list_logger(data):
    '''
    Логгер для записи списка значений, введенных пользователем.
    '''
    time = dt.now().strftime('%H:%M:%S')
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write('\n{};строка, которая предназначена для справочника после очередного добавления доп. поля (с учетом предыдущих значений);{}\n'.format(
            time, data))


def value_string_logger(data):
    '''
    Логгер для записи преобразований со значениями, введенными пользователем.
    '''
    time = dt.now().strftime('%H:%M:%S')
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write('\n{};преобразованное значение;{}\n'.format(
            time, data))


def operation_logger(data):
    '''
    Логгер для записи операции, введенной пользователем.
    '''
    time = dt.now().strftime('%H:%M:%S')
    data = d3[data]
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write('\n{}{}\n'.format(
            time, '-------ЗАПИСЬ ОПЕРАЦИИ СО СПРАВОЧНИКОМ (НАЧАЛО)-------'))
        file.write('\n{};операция со справочником;{}\n'.format(
            time, data))
        file.write('\n{}{}\n'.format(
            time, '-------ЗАПИСЬ ОПЕРАЦИИ СО СПРАВОЧНИКОМ (КОНЕЦ)-------'))
