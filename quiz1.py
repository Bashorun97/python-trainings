import random
def main():
    state_capital = {'Abia': 'Umuahia', 'Lagos': 'Ikeja', 'Kwara': 'Ilorin','Edo': 'Benin', 'Borno': 'Maiduguri'}
    incorrect_answers = set()

    while len(state_capital)>0:
        choice = random.choice(list(state_capital.keys()))
        print(choice)
main()
