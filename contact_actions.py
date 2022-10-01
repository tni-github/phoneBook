import logger as log
import csv
from io import UnsupportedOperation
import user_interface as ui
from dictionaries import dict_field as d1
from dictionaries import dict_translate as d2
import os
import re
import check as ch
from colorama import *
init()


def add_contact():
    '''
    Добавление контакта в новую строку.
    Первая строка - строка заголовков столбцов.
    Предусмотрены случаи:
    отсутствия файла, пустого файла, уже заполненного файла.
    '''
    ui.print_instructions_for_input()
    string_in_file, header = [], []
    for i in range(1, 7):
        header.append(d2[d1[i]])
        if i == 1:
            text = ui.input_data(d2[d1[i]])
            if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) != None:
                f = ch.check_double_surname(text)
            if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) == None:
                f = ch.check_textfield(text)
                f = str(f).capitalize()
            log.value_input_logger(text, i)
            log.value_string_logger(f)
        if i == 2:
            f = ch.check_textfield(ui.input_data(
                d2[d1[i]]))
            log.value_input_logger(f, i)
            f = str(f).capitalize()
            log.value_string_logger(f)
        if i == 3:
            f = ch.check_textfield(ui.input_data(
                d2[d1[i]]), 0)
            log.value_input_logger(f, i)
            f = str(f).capitalize()
            log.value_string_logger(f)
        if i == 4:
            f = ch.remove_spaces_in_string(ui.input_data(d2[d1[i]]))
            f = ch.check_mobile(f)
            log.value_input_logger(f, i)
            log.value_string_logger(f)
        if i == 5:
            f = ch.remove_spaces_in_string(ui.input_data(d2[d1[i]]))
            f = ch.check_homephone(f)
            log.value_input_logger(f, i)
            log.value_string_logger(f)
        if i == 6:
            f = ch.check_free_textfield(ui.input_data(
                d2[d1[i]]))
            log.value_input_logger(f, i)
            f = str(f).capitalize()
            log.value_string_logger(f)
        string_in_file.append(f)
        log.value_list_logger(string_in_file)
    try:
        open('contacts.csv')
        with open('contacts.csv', 'a', encoding='utf-8') as phonebook:
            file_writer = csv.writer(
                phonebook, delimiter='|', lineterminator="\r")
            if os.stat('contacts.csv').st_size != 0:
                file_writer.writerow(string_in_file)
            elif os.stat('contacts.csv').st_size == 0:
                file_writer.writerow(header)
                file_writer.writerow(string_in_file)
    except (FileNotFoundError, UnsupportedOperation):
        with open('contacts.csv', 'a', encoding='utf-8') as phonebook:
            file_writer = csv.writer(
                phonebook, delimiter='|', lineterminator="\r")
            file_writer.writerow(header)
            file_writer.writerow(string_in_file)


def find_contact(data):
    '''
    Поиск контакта по имени / фамилии.
    '''
    line = []
    count = 0
    try:
        open('contacts.csv')
        with open('contacts.csv', encoding='utf-8') as phonebook:
            file_reader = csv.reader(phonebook, delimiter='|')
            for row in file_reader:
                if data.capitalize() in row:
                    count += 1
                    line.append(row)
                    print(row)
            if count == 0:
                print('Нет совпадений.')
    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонная книга пуста, поэтому Вы не можете ее открыть!')
    return line


def open_phonebook():
    '''
    Функция открывает файл с контактами (если он есть) и выводит список в консоль.
    '''
    try:
        open('contacts.csv')
        with open('contacts.csv', encoding='utf-8') as phonebook:
            file_reader = csv.reader(phonebook, delimiter='|')
            for row in file_reader:
                if len(row) > 0:
                    print(row)
    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонной книги нет - Вы не можете ее открыть!')


def delete_contact(data):
    '''
    Фунция удаляет найденный контакт.
    '''
    try:
        open('contacts.csv')
        search_line = find_contact(data)
        if len(search_line) == 1:
            print(Fore.BLACK + Back.MAGENTA +
                  f'Найдено 1 совпадение:\n{search_line}\n')
            operation = ui.confirm_operation()
            if operation == '1':
                print(1)
            if operation == '2':
                print(Fore.BLACK + Back.MAGENTA +
                      'Вы отказались от удаления записи. Переходим в основное меню.')
        if len(search_line) > 1:
            for i in range(0, len(search_line)):
                print(Fore.BLACK + Back.MAGENTA + 'Больше одной строки')
                print(f'№ {i+1} - {search_line[i]}')
            line_del = input(
                'Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
            flag = False
            while flag == False:
                try:
                    int(line_del)
                    if int(line_del) > 0:
                        if int(line_del) < len(search_line):
                            print(1)
                            flag = True
                    else:
                        print(Fore.GREEN + Back.RED)
                        line_del = input(
                            'Неверно указан номер строки! Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
                except ValueError:
                    print(Fore.GREEN + Back.RED)
                    line_del = input(
                        'Неверно указан номер строки! Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонная книга пуста, поэтому удалять нечего!')


# delete_contact('Дарья')
