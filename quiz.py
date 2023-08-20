import requests
import json
import html
from translate import Translator


class QuestionWithAnswer:
    def __init__(self, num_of_questions, language, result):
        self.language = language
        self.result = result
        self.questions = []
        self.answers = []
        self.num_of_qestions = num_of_questions

    def append_questions_and_ansers(self):
        for i in range(self.num_of_qestions):
            question = html.unescape(self.result['results'][i]['question'])
            translator = Translator(from_lang='en', to_lang=self.language)
            translation = translator.translate(question)
            answer = html.unescape(self.result['results'][i]['correct_answer'])
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


def main():
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    result = json.loads(response.text)
    first_game = QuestionWithAnswer(10, 'pl', result)
    first_game.append_questions_and_ansers()
    first_game.display_questions()


if __name__ == "__main__":
    main()

