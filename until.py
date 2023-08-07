from question import Question
import requests
import json
import random

jsonq = "https://jsonkeeper.com/b/FIQV"
way_to_txt = 'data/text.txt'
way_to_questions = 'data/questions.json'


"""Создали главную функцию где будем вызывать методы из класса"""


def main():
    point = 0
    coat = 0

    """обращаемся к json читаем его"""
    with open(way_to_questions, 'r', encoding='utf=8') as file:
        list_questions = json.load(file)

    print("Игра начинается!\n")
    name = input("введите имя: ")

    """С помощью цикла мы передаем в класс данные из словаря"""
    random.shuffle(list_questions)

    for i in list_questions:
        questions = Question(i["q"], i["d"], i["a"])
        print(questions.build_question())
        ask = questions.is_correct(input("Ваш ответ: ").lower().strip())

        """Проверка ответа пользователя"""
        if ask:
            print(questions.build_positive_feedback())
            point += questions.get_points()
            coat += 1
        else:
            print(questions.build_negative_feedback())

    """добавляем в текстовый файл результат игры"""
    with open(way_to_txt, 'a', encoding='utf-8') as file:
        prin = file.write(f"Имя: {name}, Баллы: {point}\n")

        """Выводим результат пользователю на консоль"""
    print(f"Вот и все!\nОтвечено {coat} вопроса из {len(list_questions)}")

    """обращаемся к текстовому файлу и записываем в переменную список"""
    with open(way_to_txt, 'r', encoding='utf-8') as file:
        result = file.readlines()

        """Выводим рекорды с именами пользователю на консоль"""
        for i in result:
            print(f"{i}", end='')