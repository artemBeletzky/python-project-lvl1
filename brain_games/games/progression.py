import random
from ..main_flow import start


def generate_progression(starting_point, step, length):
    progression = []
    stop = starting_point + (step * length)
    for i in range(starting_point, stop, step):
        progression.append(i)
    return progression


def generate_round():
    starting_point = random.randrange(50)
    step = random.randrange(2, 7)
    length = random.randrange(5, 15)
    progression = generate_progression(starting_point, step, length)
    hidden_element_index = random.randrange(len(progression))
    answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = str(progression)
    return question, str(answer)


def prog() -> None:
    game_date = ('What number is missing in the progression?', generate_round)
    start(game_date)
