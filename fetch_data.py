import sqlite3
import submenu


def fetch_from_db(select, key):

    connection = sqlite3.connect("my_power.db")

    c = connection.cursor()

    c.execute(select)
    data = c.fetchall()

    match key:

        case 'last_invoice':
            _, month, l1, l2, value, total, y, m, d = data[0]
            average = round((value / total), 4)
            submenu.show_last_invoice(d, m, y, l1, l2, total, value, average)

        case 'selected_month':
            for _, month, l1, l2, value, total, y, m, d in data:
                submenu.show_month_to_choose(month, y, value, total)

            if len(data) == 0:
                print(
                    "Brak danych dla tego mięsiąca. Pamiętaj, że faktury są wystawiane raz na dwa miesiące!")

        case 'calculate_consumption':
            _, month, l1, l2, value, total, y, m, d = data[0]
            submenu.show_consumption_menu(y, m, d, l1, l2)

    connection.commit()
    connection.close()
