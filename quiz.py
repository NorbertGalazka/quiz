import requests
import json
import html
from translate import Translator

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
result = json.loads(response.text)


class QuestionWithAnswer:
    def __init__(self, num_of_questions, language):
        self.language = language
        self.questions = []
        self.answers = []
        self.num_of_qestions = num_of_questions

    def append_questions_and_ansers(self):
        for i in range(self.num_of_qestions):
            question = html.unescape(result['results'][i]['question'])
            translator = Translator(from_lang='en', to_lang=self.language)
            translation = translator.translate(question)
            answer = html.unescape(result['results'][i]['correct_answer'])
            if answer == "True":
                answer = True
            else:
                answer = False
            self.questions.append(translation)
            self.answers.append(answer)

    def display_questions(self):
        points = 0
        while self.questions:
            print(self.questions.pop())
            user_response = input("Jaka jest prawidłowa udpowiedź tak czy nie? Wpisz [t/n]: ")
            if user_response == 't':
                user_response = True
            else:
                user_response = False
            if self.answers.pop() == user_response:
                print("Brawo, udało ci się zgadnąć!!\n")
                points += 1
            else:
                print("Niestety, błąd!\n")
        print(f"Liczba zdobytych punktów: {points}")


first_game = QuestionWithAnswer(10, 'pl')
first_game.append_questions_and_ansers()
first_game.display_questions()



