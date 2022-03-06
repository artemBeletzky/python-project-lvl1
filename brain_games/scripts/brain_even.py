#!/usr/bin/env python3

import prompt
import random
from ..cli import welcome_user


def congratulate(name):
    print(f'Congratulations, {name}!')


def notify_wrong_answer(name, correct_answer, user_answer):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name}!")


def brain_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0
    required_correct_answers_count = 3
    while correct_answers_count < required_correct_answers_count:
        number = random.randrange(20)
        correct_answer = "yes" if number % 2 == 0 else "no"
        print(f'Question: {number}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            notify_wrong_answer(name, correct_answer, user_answer)
            return

    congratulate(name)


def main():
    name = welcome_user()
    brain_even(name)


if __name__ == "__main__":
    main()
