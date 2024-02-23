line = "-" * 15
empty_line = '\n'


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

    user_chooice = int(input('Proszę wybrać opcję menu: '))

    return user_chooice
