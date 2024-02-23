import menu
import fetch_data
import select_dict
import db_actions


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
            key = 'selected_month'
            fetch_data.fetch_from_db(select_dict.select[key], key)

        case 3:
            print()
            key = 'calculate_consumption'
            fetch_data.fetch_from_db(select_dict.select['last_invoice'], key)

        case 4:
            print()
            db_actions.add_item('March', 3363, 6667, 250.15, 300, 2024, 3, 20)

        case 5:
            print()
            db_actions.delete_item()

        case 0:

            menu_is_active = False
            print("Dziękujemy za skorzystanie z programu.")

        case _:
            print('Niepoprawny wybór!')
