import random


def main():
    state_capital = {'Plateau': 'Jos', 'Lagos': 'Ikeja', 'Kwara': 'Ilorin','Edo': 'Benin', 'Adamawa': 'Yola'}
    count = 7

    while count != 0:
        quiz_question = random.choice(list(state_capital.keys()))
        correct_answer = state_capital.get(quiz_question)

        answer = input('What\'s the capital of ' + quiz_question + ' state: ')
        if answer.lower() == correct_answer.lower():
            del state_capital[quiz_question]
            print('That\'s correct')

        else:
            print('That\'s wrong')
        count -= 1
        quit()
    print('lives exhausted')
main()
