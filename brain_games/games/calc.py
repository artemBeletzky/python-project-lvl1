import random
from ..main_flow import start

resolve_operation = {
    '+': (lambda member_1, member_2: member_1 + member_2),
    '-': (lambda member_1, member_2: member_1 - member_2),
    '*': (lambda member_1, member_2: member_1 * member_2)
}

operations = ['+', '-', '*']


def generate_round() -> tuple:
    member_1 = random.randrange(20, 40)
    member_2 = random.randrange(20)
    operand = random.choice(operations)
    question = f'Question: {member_1} {operand} {member_2}'
    answer = resolve_operation[operand](member_1, member_2)
    return question, str(answer)


def calc() -> None:
    game_date = ('What is the result of the expression?', generate_round)
    start(game_date)
