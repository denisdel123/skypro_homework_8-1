class Question:

    def __init__(self, text_question, complexity_questions, correct_asked):
        self.text_question = text_question
        self.complexity_questions = complexity_questions
        self.correct_asked = str(correct_asked)

        self.question_asked = False
        self.asked_user = None
        self.points_per_question = int(complexity_questions) * 10

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"{self.text_question}\nСложность {self.complexity_questions}/5"

    def is_correct(self, user_ask):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """

        return user_ask == self.correct_asked

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points_per_question

    def build_positive_feedback(self):
        """Возвращает:
        Ответ верный, получено __ баллов
        """

        return f"Ответ верный, получено {self.points_per_question} баллов\n"

    def build_negative_feedback(self):
        """Возвращает:
        Ответ неверный, верный ответ __
        """

        return f"Ответ неверный, верный ответ {self.correct_asked}\n"
