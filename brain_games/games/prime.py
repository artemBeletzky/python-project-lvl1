import random

from ..main_flow import start


def is_prime(num):
    if num <= 1:
        return False

    divider = num - 1
    is_divisible_with_no_remainder = False
    while divider > 1 and is_divisible_with_no_remainder is not True:
        is_divisible_with_no_remainder = num % divider == 0
        divider -= 1

    result = not is_divisible_with_no_remainder

    return result


def generate_round():
    question = random.randrange(1, 50)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def prime() -> None:
    game_date = ('Answer "yes" if given number is prime.'
                 ' Otherwise answer "no".', generate_round)
    start(game_date)
