import menu
import fetch_data
import select_dict
import db_actions
import submenu


menu_is_active = True


while menu_is_active:
    choice = menu.handle_manu()

    match choice:
        case 1:
            print()
            key = 'last_invoice'
            fetch_data.fetch_from_db(select_dict.select[key], key)

        case 2:
            print()
            user_year = int(input("Podaj poszukiwany rok (XXXX): "))
            user_month = int(input("Podaj poszukiwany miesiąc (1-12): "))
            print()
            key = 'selected_month'
            fetch_data.fetch_from_db(
                f'SELECT rowid,  * FROM power WHERE year = {user_year} AND month = {user_month}', key)

        case 3:
            print()
            key = 'calculate_consumption'
            fetch_data.fetch_from_db(select_dict.select['last_invoice'], key)

        case 4:
            print()
            user_month = input("Podaj nazwę miesiąca po angielsku: ")
            user_l1 = int(input("Podaj obecną wartość taryfy L1: "))
            user_l2 = int(input("Podaj obecną wartość taryfy L2: "))
            print(user_month, user_l1, user_l2)

            # db_actions.add_item('May', 3343, 6757, 155.08, 166, 2024, 5, 16)
            print('Ta opcja nie jest jeszcze dostępna')

        case 5:
            print()
            # db_actions.delete_item()
            print('Ta opcja nie jest jeszcze dostępna')

        case 0:

            menu_is_active = False
            print("Dziękujemy za skorzystanie z programu.")

        case _:
            print("Nie ma takie opcji do wyboru!")
