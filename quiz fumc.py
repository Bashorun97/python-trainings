import random

state_capital = {'Plateau': 'Jos', 'Lagos': 'Ikeja', 'Kwara': 'Ilorin','Edo': 'Benin', 'Adamawa': 'Yola'}
count = 0


def main():
    while count != 0:
        quiz_question = random.choice(list(state_capital.keys()))
        correct_answer = state_capital.get(quiz_question)
        answer = input('What\'s the capital of ' + quiz_question + ' state: ')

        if answer.lower() == correct.lower():
            correct_function()

        else:
            incorrect_function()
main()

def correct_function():
    del state_capital[quiz_question]
    print('That is correct')

def incorrect_function():
    print('That\'s wrong')
    
