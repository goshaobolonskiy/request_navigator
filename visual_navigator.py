import tkinter as tk  
from tkinter import scrolledtext, messagebox  
import io  
import re  # Модуль для регулярных выражений  
import pyautogui  
from time import sleep  
import keyboard  

# Функция для загрузки содержимого файла test.txt  
def load_file_content():  
    try:  
        with io.open('test.txt', encoding='utf-8') as file:  
            content = file.readlines()  # считываем все строки  
            # Вставляем каждую строку в текстовое поле  
            for line in content:  
                text_area.insert(tk.END, line)  # Вставляем каждую строку
    except FileNotFoundError:  
        text_area.insert(tk.END, "Файл test.txt не найден.")  # Сообщение об ошибке, если файл не найден  

# Глобальная переменная для направления
k = ['']  # Начальное значение

def validate_input():  
    direction = direction_entry.get().strip()  
    direction_number = direction_number_entry.get().strip() # Получаем номер направления  

    # Проверяем, что направление не пустое и состоит только из букв (русских и английских) и пробелов  
    if not direction or not re.match("^[А-Яа-яЁёA-Za-z\s]+$", direction):  
        messagebox.showerror("Ошибка ввода", "Направление должно содержать только буквы (русские и английские) и пробелы и не должно быть пустым.")  
        return None  

    try:  
        # Проверяем, что группа — это целое число больше нуля  
        group_number = int(group_entry.get())  
        if group_number <= 0:  # Условие для проверки на положительное значение  
            messagebox.showerror("Ошибка ввода", "Группа должна быть целым числом больше нуля.")  
            return None  

        # Проверяем, что номер направления - целое число и находится в диапазоне от 1 до 3  
        direction_number = int(direction_number)  
        if not 1 <= direction_number <= 3:  
            messagebox.showerror("Ошибка ввода", "Номер направления должен быть целым числом от 1 до 3.")  
            return None  
        
        # Проверяем, что начальный и конечный номера — это числа  
        start_number = int(start_entry.get())  
        end_number = int(end_entry.get())  
        return direction, direction_number, group_number, start_number, end_number  
    except ValueError:  
        # Если произошла ошибка преобразования, показываем сообщение об ошибке  
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите числовые значения в группе и номерах.")  
        return None  

def start_program():  
    global k  # Объявляем переменную k как глобальную  

    validated_input = validate_input()  
    if validated_input is None:  
        return  # Если валидация не удалась, выходим из функции  

    direction, direction_number, group_number, start_number, end_number = validated_input  
    k[0] = direction  # Обновляем значение направления  

    # print("Программа запущена с параметрами:", k[0], direction_number, group_number, start_number, end_number)  

    # Основная логика обработки здесь...  
    list_stud = []  
    with io.open('test.txt', encoding='utf-8') as file:  
        for line in file:  
            list_stud.append(line)  

    family = []  
    name = []  
    surname = []  
    for i in list_stud:  
        family.append(i[:i.find(' ')])  
        name.append(i[i.find(' '):i.find(' ', i.find(' ')+1)])  
        if i.find(',') == -1:  
            surname.append(i[i.find(' ', i.find(' ')+1):int([n for n, char in enumerate(i) if char == ' '][2])])  
        else:  
            surname.append(i[i.find(' ', i.find(' ')+1):i.find(',')])  

    t = 0.5    # дополнительная задержка  

    if end_number == 0:  
        end_number = len(list_stud)  
    # print(type(k), type(group_number), type(start_number), type(end_number))  


    if group_number < 4:  
        group_number = 305 + group_number * 30  
    else:  
        group_number = 315 + group_number * 30  

    pyautogui.click(270, 1060)  # Переход в Яндекс  
    sleep(0.2)  
    for i in range(start_number, end_number):  # Изменено с 0 на end_number  
        f = open('result.txt', 'a')
        sleep(0.2 + t / 3)  
        pyautogui.click(115, 185)  
        sleep(0.4 + t / 2)  
        pyautogui.click(1268, 230)  
        sleep(1)  
        keyboard.write(k[0])  
        sleep(1)  
        #pyautogui.click(830, 260)  # Выбор направления (самое верхнее: y=260, вторая: y=290)  
        pyautogui.click(830, 260 + (direction_number - 1) * 30) # Выбираем нужное направление, добавляя смещение  
        sleep(0.1 + t)  
        pyautogui.click(1268, 305)  
        sleep(1)  
        pyautogui.click(1200, group_number)  # Выбор группы (самая верхняя: y=335, вторая: y=365 и т.д.)  
        sleep(0.5)  
        pyautogui.click(1150, 455)  
        sleep(0.3)  
        pyautogui.click()  
        keyboard.write(family[i] + name[i] + surname[i])  
        sleep(1.5)  

        try:  
            if pyautogui.locateOnScreen('images/check.png', region=(655, 430, 660, 200)):  # Проверка, тот ли это пользователь  
                pyautogui.click(950, 500)  # Выбор существующего пользователя  
                sleep(1)  
                x, y = pyautogui.locateCenterOnScreen('images/created.png', region=(1000, 550, 400, 250))  
                sleep(0.2)  
                pyautogui.click(x, y)  # Создание пользователя  
                sleep(1)  
                if pyautogui.locateOnScreen('images/error_2.png', region=(700, 450, 570, 220)):  # Если пользователь уже создан  
                    sleep(0.5)  
                    pyautogui.click(985, 595)  
                    sleep(0.3)  
                    pyautogui.click(1273, 145)  
                    f.write(f'{list_stud[i]}')  
                else:  
                    f.write(f'{list_stud[i]}')  
            else:  
                pyautogui.click(1235, 455)  
                pyautogui.click(625, 235)  
                sleep(0.1)  
                keyboard.write(family[i])  # Вставка фамилии  
                pyautogui.click(625, 310)  
                keyboard.write(name[i])  # Вставка имени  
                pyautogui.click(625, 380)  
                keyboard.write(surname[i])  # Вставка фамилии  
                sleep(0.2)  
                pyautogui.click(585, 640)  # Кнопка поиск  
                sleep(0.5)  

                if pyautogui.locateOnScreen('images/not_children2.png', region=(1000, 370, 230, 150)):  
                    f.write(f'${list_stud[i]}')  
                    sleep(0.2)  
                    pyautogui.click(745, 640)  
                    sleep(0.2)  
                    pyautogui.click(1273, 145)  
                elif pyautogui.locateOnScreen('images/many_children.png'):  
                    f.write(f'$$${list_stud[i]}')  
                    sleep(0.2)  
                    pyautogui.click(745, 640)  
                    sleep(0.2)  
                    pyautogui.click(1273, 145)  
                else:  
                    sleep(0.5)  
                    center = pyautogui.locateCenterOnScreen('images/created.png')  
                    if center:  # Проверяем, нашли ли мы изображение  
                        x, y = center  
                        pyautogui.click(x, y)  # Создание пользователя  
                        f.write(f'{list_stud[i]}')  

        except Exception as ex:  
            print(ex)  
        f.close()  
        sleep(4)  


# Создаем главное окно  
root = tk.Tk()  
root.title("Настройки программы")  
root.geometry("800x500")  

# Поле для ввода направления  
tk.Label(root, text="Направление:").grid(row=0, column=0, padx=10, pady=10)  
direction_entry = tk.Entry(root, width=30)  
direction_entry.grid(row=0, column=1, padx=10, pady=10)  

# Поле для ввода номера направления на сайте  
tk.Label(root, text="Номер направления на сайте:").grid(row=1, column=0, padx=10, pady=10)  
direction_number_entry = tk.Entry(root, width=30)  
direction_number_entry.insert(0, "1")  # Значение по умолчанию = 1  
direction_number_entry.grid(row=1, column=1, padx=10, pady=10)  


# Поле для ввода группы  
tk.Label(root, text="Группа:").grid(row=2, column=0, padx=10, pady=10)  
group_entry = tk.Entry(root, width=30)  
group_entry.grid(row=2, column=1, padx=10, pady=10)  

# Поле для ввода номера участника, с которого начинаем  
tk.Label(root, text="Номер участника, с которого начинаем:").grid(row=3, column=0, padx=10, pady=10)  
start_entry = tk.Entry(root, width=30)  
start_entry.insert(0, "0")  # начальное значение  
start_entry.grid(row=3, column=1, padx=10, pady=10)  

# Поле для ввода номера, на котором заканчиваем  
tk.Label(root, text="Заканчиваем: (по умолчанию 0 - до конца файла)").grid(row=4, column=0, padx=10, pady=10)  
end_entry = tk.Entry(root, width=30)  
end_entry.insert(0, "0")  # начальное значение  
end_entry.grid(row=4, column=1, padx=10, pady=10)  

# Текстовое поле для отображения содержимого test.txt  
tk.Label(root, text="Содержимое файла test.txt:").grid(row=5, column=0, padx=10, pady=10)  
text_area = scrolledtext.ScrolledText(root, width=58, height=10)  
text_area.grid(row=5, column=1, padx=10, pady=10)  

# Загрузка содержимого файла при старте приложения  
load_file_content()  

# Кнопка запуска  
start_button = tk.Button(root, text="Запуск", command=start_program)  
start_button.grid(row=6, column=1, padx=10, pady=20)  

# Запуск главного цикла  
root.mainloop()