import pyautogui
from time import sleep
import keyboard
import io

list_stud = []
with io.open('test.txt', encoding='utf-8') as file:
    for line in file:
        list_stud.append(line)

# print(list_stud[0].find(' '))
family = []
name = []
surname = []
for i in list_stud:
    family.append(i[:i.find(' ')])
    name.append(i[i.find(' '):i.find(' ',i.find(' ')+1)])
    if i.find(',') == -1:
        surname.append(i[i.find(' ', i.find(' ')+1):int([n for n, char in enumerate(i) if char == ' '][2])])
    else:
        surname.append(i[i.find(' ',i.find(' ')+1):i.find(',')])
# print(surname)

k = ['Английский язык'] # выбор программы
t = 0.5    # дополнительная задержка

pyautogui.click(270, 1060) # Переход в яндекс
sleep(0.2)
for i in range(0, len(list_stud)): #
    f = open('result.txt','a')
    # pyautogui.click(600,20)
    sleep(0.2)
    pyautogui.click(115, 185)
    sleep(0.4)
    pyautogui.click(1268, 230)
    sleep(1)
    keyboard.write(k[0])
    sleep(1)
    pyautogui.click(830, 260) #Выбор направления (Самая верхнее: y=260, вторая: y=290)
    sleep(0.1+t)
    pyautogui.click(1268, 305)
    sleep(1)
    pyautogui.click(1200, 335) #Выбор группы (Самая верхняя: y=335, вторая: у=365, третья: y=395, четвертая: y=425, 460, 490, 520)
    sleep(0.5)
    pyautogui.click(1150, 455)
    sleep(0.3)
    pyautogui.click()
    keyboard.write(family[i]+name[i]+surname[i])
    sleep(1.5)

    try:
        if pyautogui.locateOnScreen('check.png', region=(655,430, 660, 200)):  #Проверка тот ли это пользователь
            pyautogui.click(950, 500)#Выбор существующего пользователя
            sleep(1)
            # pyautogui.click(1155, 745) #Создание пользователя
            x, y = pyautogui.locateCenterOnScreen('created.png', region=(1000,550, 400, 250))
            sleep(0.2)
            pyautogui.click(x,y) #Создание пользователя
            sleep(1)
            if pyautogui.locateOnScreen('error_2.png', region=(700,450, 570, 220)): #Если пользователь уже был создан
                # print('WORK')
                sleep(0.5)
                pyautogui.click(985, 595)
                sleep(0.3)
                pyautogui.click(1273, 145)
                f.write(f'{list_stud[i]}')
            else: f.write(f'{list_stud[i]}')
        else: 
            # print('go yet')
            pyautogui.click(1235, 455)
            pyautogui.click(625, 235)
            sleep(0.1)
            keyboard.write(family[i]) #Вставка фамилии
            pyautogui.click(625, 310)
            keyboard.write(name[i]) #Вставка имени
            pyautogui.click(625,380)
            keyboard.write(surname[i]) #Вставка имени
            sleep(0.2)
            pyautogui.click(585, 640)#Кнопка поиск
            sleep(0.5)
            # try:
            if pyautogui.locateOnScreen('not_children2.png', region=(1000,370, 230, 150)): #
                # print('Clidren not have')
                f.write(f'${list_stud[i]}')
                sleep(0.2)
                pyautogui.click(745,640)
                sleep(0.2)
                pyautogui.click(1273, 145)
            elif pyautogui.locateOnScreen('many_children.png'): #, region=(1260,720, 200, 65)
                # print("many_children")
                f.write(f'$$${list_stud[i]}')
                sleep(0.2)
                pyautogui.click(745,640)
                sleep(0.2)
                pyautogui.click(1273, 145)
            else:
                # print('ALL GOOD')
                sleep(0.5)
                # pyautogui.click(1155, 745) #Создание пользователя

                center = pyautogui.locateCenterOnScreen('created.png')
                if center:  # Проверяем, нашли ли мы изображение  
                    x, y = center  
                    pyautogui.click(x, y)  #Создание пользователя  
                    f.write(f'{list_stud[i]}')
                # x, y = pyautogui.locateCenterOnScreen('created.png')
                # pyautogui.click(x, y) #Создание пользователя
                # f.write(f'{list_stud[i]}')

                
    except Exception as ex:
        print(ex)
    f.close()
    sleep(4)

#     pyautogui.click(1155, 745) #Создание пользователя

