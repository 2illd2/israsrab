import sqlite3

conn = sqlite3.connect("magazin.db")
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS mammals
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                species TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                weight REAL NOT NULL)
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS trainers
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                experience INTEGER NOT NULL)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS enclosures
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                capacity INTEGER NOT NULL)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS positions
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                position_id INTEGER NOT NULL,
                FOREIGN KEY(position_id) REFERENCES positions(id))
''')
conn.commit()

def add_mammal(name, species, age, gender, weight):
    cursor.execute("INSERT INTO mammals (name, species, age, gender, weight) VALUES (?, ?, ?, ?, ?)", (name, species, age, gender, weight))
    conn.commit()
    print("Млекопитающий успешно добавлен в базу данных")

def update_mammal(mammal_id, name=None, species=None, age=None, gender=None, weight=None):
    update_values = []
    if name:
        update_values.append(("name", name))
    if species:
        update_values.append(("species", species))
    if age:
        update_values.append(("age", age))
    if gender:
        update_values.append(("gender", gender))
    if weight:
        update_values.append(("weight", weight))
    if len(update_values) == 0:
        print("Необходимо указать хотя бы одно поле для изменения")
        return
    update_query = "UPDATE mammals SET "
    for i in range(len(update_values)):
        update_query += "=?".format(update_values[i][0])
        if i != len(update_values) - 1:
            update_query += ", "
    update_query += " WHERE id=?"
    cursor.execute(update_query, [x[1] for x in update_values] + [mammal_id])
    conn.commit()
    print("Информация о млекопитающем успешно изменена")

def delete_mammal(mammal_id):
    cursor.execute("DELETE FROM mammals WHERE id=?", (mammal_id,))
    conn.commit()
    print("Млекопитающий успешно удален из базы данных")

def filter_mammals_by_species(species):
    cursor.execute("SELECT * FROM mammals WHERE species=?", (species,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Млекопитающие данного вида не найдены")
    else:
        for row in rows:
            print("ID: , Имя: , Вид: , Возраст: , Пол: , Вес: ".format(row[0], row[1], row[2], row[3], row[4], row[5]))

def add_trainer(name, age, gender, experience):
    cursor.execute("INSERT INTO trainers (name, age, gender, experience) VALUES (?, ?, ?, ?)", (name, age, gender, experience))
    conn.commit()
    print("Тренер успешно добавлен в базу данных")

def update_trainer(trainer_id, name=None, age=None, gender=None, experience=None):
    update_values =[]
    if name:
        update_values.append(("name", name))
    if age:
        update_values.append(("age", age))
    if gender:
        update_values.append(("gender", gender))
    if experience:
        update_values.append(("experience", experience))
    if len(update_values) == 0:
        print("Необходимо указать хотя бы одно поле для изменения")
        return
    update_query = "UPDATE trainers SET "
    for i in range(len(update_values)):
        update_query += "=?".format(update_values[i][0])
        if i != len(update_values) - 1:
            update_query += ", "
    update_query += " WHERE id=?"
    cursor.execute(update_query, [x[1] for x in update_values] + [trainer_id])
    conn.commit()
    print("Информация о тренере успешно изменена")

def delete_trainer(trainer_id):
    cursor.execute("DELETE FROM trainers WHERE id=?", (trainer_id,))
    conn.commit()
    print("Тренер успешно удален из базы данных")

def filter_trainers_by_experience(min_experience):
    cursor.execute("SELECT * FROM trainers WHERE experience>=?", (min_experience,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Тренеры с необходимым опытом не найдены")
    else:
        for row in rows:
            print("ID: , Имя: , Возраст: , Пол: , Опыт: ".format(row[0], row[1], row[2], row[3], row[4]))

def add_enclosure(name, capacity):
    cursor.execute("INSERT INTO enclosures (name, capacity) VALUES (?, ?)", (name, capacity))
    conn.commit()
    print("Вольер успешно добавлен в базу данных")

def update_enclosure(enclosure_id, name=None, capacity=None):
    update_values = []
    if name:
        update_values.append(("name", name))
    if capacity:
        update_values.append(("capacity", capacity))
    if len(update_values) == 0:
        print("Необходимо указать хотя бы одно поле для изменения")
        return
    update_query = "UPDATE enclosures SET "
    for i in range(len(update_values)):
        update_query += "=?".format(update_values[i][0])
        if i != len(update_values) - 1:
            update_query += ", "
    update_query += " WHERE id=?"
    cursor.execute(update_query, [x[1] for x in update_values] + [enclosure_id])
    conn.commit()
    print("Информация о вольере успешно изменена")

def delete_enclosure(enclosure_id):
    cursor.execute("DELETE FROM enclosures WHERE id=?", (enclosure_id,))
    conn.commit()
    print("Вольер успешно удален из базы данных")

def filter_enclosures_by_capacity(min_capacity):
    cursor.execute("SELECT * FROM enclosures WHERE capacity>=?", (min_capacity,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Вольеры с необходимой вместимостью не найдены")
    else:
        for row in rows:
            print("ID: , Название: , Вместимость: ".format(row[0], row[1], row[2]))

def add_position(name):
    cursor.execute("INSERT INTO positions (name) VALUES (?)", (name,))
    conn.commit()
    print("Должность успешно добавлена в базу данных")

def update_position(position_id, name=None):
    update_values = []
    if name:
        update_values.append(("name", name))
    if len(update_values) == 0:
        print("Необходимо указать хотя бы одно поле для изменения")
        return
    update_query = "UPDATE positions SET "
    for i in range(len(update_values)):
        update_query += "=?".format(update_values[i][0])
        if i != len(update_values) - 1:
            update_query += ", "
    update_query += " WHERE id=?"
    cursor.execute(update_query, [x[1] for x in update_values] + [position_id])
    conn.commit()
    print("Информация о должности успешно изменена")

def delete_position(position_id):
    cursor.execute("DELETE FROM positions WHERE id=?", (position_id,))
    conn.commit()
    print("Должность успешно удалена из базы данных")

def add_employee(name, age, gender, position_id):
    cursor.execute("INSERT INTO employees (name, age, gender, position_id) VALUES (?, ?, ?, ?)", (name, age, gender, position_id))
    conn.commit()
    print("Сотрудник успешно добавлен в базу данных")

def update_employee(employee_id, name=None, age=None, gender=None, position_id=None):
    update_values = []
    if name:
        update_values.append(("name", name))
    if age:
        update_values.append(("age", age))
    if gender:
        update_values.append(("gender", gender))
    if position_id:
        update_values.append(("position_id", position_id))
    if len(update_values) == 0:
        print("Необходимо указать хотя бы одно поле для изменения")
        return
    update_query = "UPDATE employees SET "
    for i in range(len(update_values)):
        update_query += "=?".format(update_values[i][0])
        if i != len(update_values) - 1:
            update_query += ", "
    update_query += " WHERE id=?"
    cursor.execute(update_query, [x[1] for x in update_values] + [employee_id])
    conn.commit()
    print("Информация о сотруднике успешно изменена")

def delete_employee(employee_id):
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()
    print("Сотрудник успешно удален из базы данных")

def filter_employees_by_position(position_id):
    cursor.execute("SELECT * FROM employees WHERE position_id=?", (position_id,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Сотрудники данной должности не найдены")
    else:
        for row in rows:
            print("ID: , Имя: , Возраст: , Пол: , Должность: ".format(row[0], row[1], row[2], row[3], row[4]))



