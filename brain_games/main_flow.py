import prompt

rounds_count = 3


def start(game_data: tuple) -> None:
    description, generate_round = game_data
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)
    for i in range(rounds_count):
        question, answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer"
                  f" was '{answer}'. Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
