import datetime
import json
import sys

data = {}
history = []
choice = -1
line1 = '-' * 60
line2 = "-" * 28


def load_data():
    with open("current_data.json", "r") as f:
        json_file = json.load(f)
        return json_file


def save_data(data):
    with open("current_data.json", 'w') as f:
        new_data = json.dumps(data, indent=4)
        f.write(new_data)


def last_invoice_info():

    data = load_data()

    l1, l2, value, total_consumption, year, month, day = data['last_invoice'].values(
    )

    price_1kWh = round(value / total_consumption, 4)

    print(line1)
    print(f'Data ostatniego odczytu / faktura: {day}.{month}.{year}')
    print(f'Stan taryfy dziennej L1 na ostatniej fakturze: {l1} kWh')
    print(f'Stan taryfy nocnej L2 na ostatniej fakturze: {l2} kWh')
    print(f'Ilość zużytych kWh na ostatniej fakturze: {total_consumption} ')
    print(f'Kwota do zapłaty z ostatniej faktury: {value} PLN')
    print(f'Średnia cena za 1 kWh z ostatniej faktury: {price_1kWh} PLN')
    print(line1)


def history_invoice_info():

    data = load_data()

    l1, l2, value, total_consumption, year, month, day = data['history'][0].values(
    )

    price_1kWh = round(value / total_consumption, 4)

    print(line1)
    print(f'Data ostatniego odczytu / faktura: {day}.{month}.{year}')
    print(f'Stan taryfy dziennej L1 na ostatniej fakturze: {l1} kWh')
    print(f'Stan taryfy nocnej L2 na ostatniej fakturze: {l2} kWh')
    print(f'Ilość zużytych kWh na ostatniej fakturze: {total_consumption} ')
    print(f'Kwota do zapłaty z ostatniej faktury: {value} PLN')
    print(f'Średnia cena za 1 kWh z faktury: {price_1kWh} PLN')
    print(line1)


def check_current_consumption():

    data = load_data()
    l1, l2, value, total_consumption, year, month, day = data['last_invoice'].values(
    )

    current_year = int(input("Podaj obecny rok (XXXX): "))
    current_month = int(input("Podaj bieżący miesiąc (cyfra): "))
    current_day = int(input("Podaj bieżący dzień (cyfra): "))
    current_l1 = int(input("Podaj aktualny stan taryfy dziennej:"))
    current_l2 = int(input("Podaj aktualny stan taryfy nocnej:"))

    invoice_day = datetime.date(year, month, day)
    current_date = datetime.date(current_year, current_month, current_day)
    delta = current_date - invoice_day
    l1_current_consumpion = current_l1 - l1
    l2_current_consumpion = current_l2 - l2
    total_current_consumpion = l1_current_consumpion + l2_current_consumpion

    print(line1)
    print(
        f'Ilość kWh zużytych w taryfie dziennej od ostatniej faktury: {l1_current_consumpion}')
    print(
        f'Ilość kWh zużytych w taryfie nocnej od ostatniej faktury: {l2_current_consumpion}')
    print(
        f'Całkowita ilość kWh zużytych od ostatniej faktury: {total_current_consumpion}')
    print(f'Ilość dni od ostatniej faktury: {delta.days}')
    print(
        f'Średnie dzienne zużycie od ostatniej faktury: {round(total_current_consumpion / delta.days,4)}')


def upade_invoice_info():

    new_invoice_year = int(input("Podaj rok z wystawionej faktury: "))
    new_invoice_month = int(input("Podaj miesiąc z wystawionej faktury: "))
    new_invoice_day = int(input("Podaj dzień z wystawionej faktury: "))
    new_invoice_l1 = int(
        input("Podaj ilość zużytych kWh w taryfie dziennej z obecnej faktury: "))
    new_invoice_l2 = int(
        input("Podaj ilość zużytych kWh w taryfie nocnej z obecnej faktury: "))
    new_invoice_total_consumption = int(
        input("Podaj całkowitą ilość zużytych kWh z ostatniej faktury: "))
    new_invoice_value = float(input("Podaj wartość nowej faktury (PLN): "))

    data = load_data()
    last_invoice, his = data.values()
    history = his
    history.append(last_invoice)
    data['history'] = history

    new_data = {
        "L1": new_invoice_l1,
        "L2": new_invoice_l2,
        "invoice_value": new_invoice_value,
        "total_consumption": new_invoice_total_consumption,
        "year": new_invoice_year,
        "month": new_invoice_month,
        "day": new_invoice_day
    }

    data['last_invoice'] = new_data

    save_data(data)


while choice != 5:

    print(f'{line2}MENU{line2}')
    print(f'1. Dane z ostaniej faktury')
    print(f'2. Sprawdź zużycie od ostatniej faktury')
    print(f'3. Wprowadź dane z nowej faktury')
    print(f'4. Dane historyczne')
    print(f'5. Wyjście')

    choice = int(input('Wybierz opcję z Menu: '))
    if choice == 1:
        last_invoice_info()
    elif choice == 2:
        check_current_consumption()
    elif choice == 3:
        upade_invoice_info()
    elif choice == 4:
        history_invoice_info()
    elif choice == 5:
        sys.exit("Dziękuję za korzystanie z programu!")
    else:
        print("Zły wybór, spróbuj jeszcze raz!")
