import random
from ..main_flow import start


def generate_round() -> tuple:
    question = random.randrange(20)
    answer = "yes" if question % 2 == 0 else "no"
    return question, answer


def even():
    game_date = ('Answer "yes" if the number is even, otherwise answer "no".',
                 generate_round)
    start(game_date)
