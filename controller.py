import user_interface as ui
import contact_actions as ca
import os
os.system("cls")


# 'Какую операцию вы хотите выполнить? \n 1 - Открыть текущий справочник \n 2 - Добавить новую запись \n 3 - Удалить запись \n 4 - Поиск записи (вывод на экран) \n 5 Импорт из json \n 6 Экспорт в json\n')

def button_click():
    '''
    Запуск и отработка приложения.
    '''
    operation = ui.get_operation()
    if operation == 1:
        result = ca.open_phonebook()
    elif operation == 2:
        result = ca.add_contact()
    elif operation == 3:
        data = ui.input_text()
        print('Функция в стадии разработки.')
    elif operation == 4:
        data = ui.input_text()
        result = ca.find_contact(data)
    elif operation == 5:
        print('Функция в стадии разработки.')
    elif operation == 6:
        print('Функция в стадии разработки.')
    # ui.view_result(result)
