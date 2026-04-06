print("GuessTheNumber (Угадай число)")
print("__________")
print("Привет! Загадано число от 1 до 100, угадай его")
print("У тебя 5 попыток")
print("Получится ли у тебя угадать хоть раз?")
print("__________")

import random
number = random.randint(1, 100)
popytki = 5
i = "да"

while i == "да": 
    if popytki != 0: 
        number_input = int(input("Введите число от 1 до 100: "))
        if number_input > 0 and number_input <= 100:
            popytki -= 1    
            if number_input > number:
                if popytki != 0:
                    print("❌ Неверно! Загаданное число МЕНЬШЕ")
                    print("-1 попытка, осталость:", popytki)
                    print("__________")
            elif number_input < number:
                if popytki != 0:
                    print("❌ Неверно! Загаданное число БОЛЬШЕ")
                    print("-1 попытка, осталость:", popytki)
                    print("__________")
            else:
                print("🥳 Ура!")
                print("✅ Вы угадали загаданное число!")
                print("__________")
                print("Хотите сыграть ещё раз?")
                print("да/нет")
                i = input().lower()
                print("__________")
                if i == "да":
                    popytki = 5
                    number = random.randint(1, 100)
                    print("Новая игра")
                elif i != "да":
                    print("Игра окончена!")
        else:
            print("❌ Число должно быть в диапазоне от 1 до 100!")
            print("__________")           
            
    else:
        if number_input != number:
            print("__________")
            print("😥 Вы проиграли!")
            print("Загаданное число:", number)
            print("__________")
            print("Хотите сыграть ещё раз?")
            print("да/нет")
            i = input().lower()
            print("__________")
        if i == "да":
            popytki = 5
            number = random.randint(1, 100)
            print("Новая игра")
        elif i != "да":
            print("Игра окончена!")
            
