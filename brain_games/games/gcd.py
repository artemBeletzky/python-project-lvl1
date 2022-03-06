import random
from ..main_flow import start


def find_gcd(a, b):
    greater_number = max(a, b)
    smaller_number = min(a, b)
    remainder = greater_number - smaller_number
    if remainder % smaller_number <= 0:
        return smaller_number
    return find_gcd(remainder, smaller_number)


def generate_round() -> tuple:
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    question = f'{x} {y}'
    answer = find_gcd(x, y)
    return question, str(answer)


def gcd() -> None:
    game_date = ('Find the greatest common divisor'
                 ' of given numbers.', generate_round)
    start(game_date)
