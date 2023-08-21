import requests
import json
import html
from translate import Translator


class QuestionWithAnswer:
    def __init__(self, num_of_questions, language, result, sentences):
        self.language = language
        self.result = result
        self.questions = []
        self.answers = []
        self.num_of_questions = num_of_questions
        self.sentences = sentences

    def __del__(self):
        print(self.sentences['del'])

    def append_questions_and_anwsers(self):
        for i in range(self.num_of_questions):
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
            user_response = input(self.sentences['user_res'] + " [y/n]: ")
            if user_response.lower() == 'y':
                user_response = True
            else:
                user_response = False
            if self.answers.pop() == user_response:
                print(self.sentences["well_done"], "\n")
                points += 1
            else:
                print(self.sentences["error"], "\n")
        print(self.sentences["points"], points)


def choose_language(languages):
    print(languages)
    lang = input("Choose your language: ")
    return lang


def main():
    languages = ['en', 'pl', 'cs', 'fr', 'de', 'hu', 'pt', 'ru', 'es', 'uk']
    chosen_lang = choose_language(languages)
    sentences = {"del": "The question and answer set has been removed!",
                 "user_res": "What is the correct answer yes or no? Enter ",
                 "well_done": "Well done, you guessed it!",
                 "error": "Sorry, error!",
                 "points": "Number of points scored: "}
    for key, value in sentences.items():
        translator = Translator(from_lang='en', to_lang=chosen_lang)
        translation = translator.translate(value)
        sentences.update({key: translation})

    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    result = json.loads(response.text)
    first_game = QuestionWithAnswer(10, chosen_lang, result, sentences)

    first_game.append_questions_and_anwsers()
    first_game.display_questions()


if __name__ == "__main__":
    main()

