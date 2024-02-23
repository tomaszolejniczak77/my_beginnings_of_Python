import sqlite3


def create_new_table():

    connection = sqlite3.connect("my_power.db")
    c = connection.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS power (
          invoice_period text,
          l1_value float,
          l2_value float,
          invoice_value float,
          period_total int,
          year int,
          month int,
          day int
    )""")

    connection.commit()
    connection.close()


def add_item(period, l1, l2, value, total, y, m, d):
    connection = sqlite3.connect("my_power.db")

    c = connection.cursor()

    item = (period, l1, l2, value, total, y, m, d)

    c.execute('INSERT INTO power VALUES (?, ?, ?, ?, ?, ?, ?, ?)', item)
    print('New data saved!')

    connection.commit()
    connection.close()


def delete_item():
    connection = sqlite3.connect("my_power.db")

    c = connection.cursor()

    c.execute("DELETE FROM power WHERE rowid = 4")

    connection.commit()
    connection.close()
