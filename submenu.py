from datetime import date
import data_difference


def show_last_invoice(day, month, year, l1, l2, total, value, price):
    print(f'Data ostatniego odczytu / faktura: {day}.{month}.{year}')
    print(f'Stan taryfy dziennej L1 na ostatniej fakturze: {l1} kWh')
    print(f'Stan taryfy nocnej L2 na ostatniej fakturze: {l2} kWh')
    print(f'Ilość zużytych kWh na ostatniej fakturze: {total} ')
    print(f'Kwota do zapłaty z ostatniej faktury: {value} PLN')
    print(f'Średnia cena za 1 kWh z faktury: {price} PLN')


def show_consumption_menu(y, m, d, l1, l2):
    current_l1 = int(input('Podaj obecny stan taryfy L1: '))
    current_l2 = int(input('Podaj obecny stan taryfy L2: '))
    startdate = date(y, m, d)
    current_consumption_l1 = current_l1 - l1
    current_consumption_l2 = current_l2 - l2
    total_curreent = current_consumption_l1 + current_consumption_l2
    days = data_difference.get_difference(startdate)
    average_current_consumption = round(total_curreent / days, 4)
    print()
    print(f'Od ostatniej faktury minęło: {days} dni')
    print(f'Całkowite bierzące zużycie: {total_curreent} kWh')
    print(
        f'Średnie dzienne zużycie od ostatniej faktury: {average_current_consumption} kWh')


def show_month_to_choose(month, year):
    print(f'{month}, {year}')
