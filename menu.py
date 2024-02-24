line = "-" * 15
empty_line = '\n'


def check_user_choice(choice):
    try:
        return int(choice)
    except ValueError:
        print()
        print("Nie wybrano cyfry!")


def handle_manu():

    print(empty_line)
    print(f'{line}Menu{line}')
    print(empty_line)
    print(f'1. Dane z ostatniej faktury')
    print(f'2. Pokaż dane z wybranego miesiąca')
    print(f'3. Policz bierzące zużycie energii')
    print(f'4. Dodaj dane z nowej faktury')
    print(f'5. Usuń pozycję')
    print(f'0. Wyjście')
    print(empty_line)

    user_choice = input('Proszę wybrać opcję menu: ')

    return check_user_choice(user_choice)
