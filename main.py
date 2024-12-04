import os
import time
import pyautogui

# Функция для открытия калькулятора
def open_calculator():
    # Для Windows
    os.system("start calc")

# Функция для автоматизации вычислений
def automate_calculator():
    time.sleep(2)  # Задержка для открытия приложения

    # Подождите, пока калькулятор не загрузится
    while True:
        # Найдите кнопки с помощью locateOnScreen
        button_1 = pyautogui.locateOnScreen('button_1.png', confidence=0.9)
        button_2 = pyautogui.locateOnScreen('button_2.png', confidence=0.9)
        button_plus = pyautogui.locateOnScreen('button_plus.png', confidence=0.9)
        button_7 = pyautogui.locateOnScreen('button_7.png', confidence=0.9)
        button_equals = pyautogui.locateOnScreen('button_equals.png', confidence=0.9)

        if button_1 and button_2 and button_plus and button_7 and button_equals:
            break

    # Клик по кнопкам калькулятора
    pyautogui.click(button_1)
    pyautogui.click(button_2)
    pyautogui.click(button_plus)
    pyautogui.click(button_7)
    pyautogui.click(button_equals)

# Запуск
open_calculator()
automate_calculator()
