import sqlite3

def initialize_database():
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    return conn, cursor

def create_courier_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courier (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lastName TEXT,
            firstName TEXT,
            patr TEXT,
            passport TEXT,
            birthDate DATE,
            hireDate DATE,
            workSt TIME,
            workEnd TIME,
            city TEXT,
            street TEXT,
            building TEXT,
            apartment TEXT,
            phone TEXT
        )
    """)


def create_sender_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sender (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lastName TEXT,
            firstName TEXT,
            patr TEXT,
            birthDate DATE,
            postalCode TEXT,
            city TEXT,
            street TEXT,
            building TEXT,
            apartment TEXT,
            phone TEXT
        )
    """)


def add_courier_sample(cursor):
    courier_data = (
        "Petrov", "Petr", "Petrovich", "1234 567890", "15.08.1990", "01.09.2022",
        "09:00", "18:00", "Saint Petersburg", "Nevsky", "25", "5", "+79161234567"
    )
    cursor.execute("""
        INSERT INTO courier (
            last_name, first_name, patronymic, passport, birth_date, hire_date, 
            work_start, work_end, city, street, building, apartment, phone
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, courier_data)


def add_sender_sample(cursor):
    sender_data = (
        "Sidorov", "Sid", "Sidorovich", "25.12.1985", "123456", "Moscow",
        "Tverskaya", "10", "2", "+79165554433"
    )
    cursor.execute("""
        INSERT INTO sender (
            last_name, first_name, patronymic, birth_date, postal_code, city, 
            street, building, apartment, phone
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sender_data)


def update_sender_phone(cursor):
    sender_identifiers = ("Sidorov", "Sid", "Sidorovich", "25.12.1985")
    cursor.execute("""
        UPDATE sender 
        SET phone = "+79001234567" 
        WHERE last_name = ? AND first_name = ? AND patronymic = ? AND birth_date = ?
    """, sender_identifiers)


connection, cursor = initialize_database()

create_courier_table(cursor)
create_sender_table(cursor)
add_courier_sample(cursor)
add_sender_sample(cursor)
update_sender_phone(cursor)

connection.commit()
connection.close()