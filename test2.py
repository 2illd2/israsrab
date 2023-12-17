import sqlite3

conn = sqlite3.connect("magazin_db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS cashiers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0
)''')

class Users():
    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age

    def save_to_db(self):
        cursor.execute("INSERT INTO users (id, name, email, age) VALUES (?, ?, ?, ?)", (self.id, self.name, self.email, self.age))
        conn.commit()

    @classmethod
    def get_by_id(cls, id):
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        row = cursor.fetchone()
        return cls(*row)

class Cashiers():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


    def save_to_db(self):
        cursor.execute("INSERT INTO cashiers (id, name, age) VALUES (?, ?, ?)", (self.id, self.name, self.age))
        conn.commit()


class Products:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    def save_to_db(self):
        cursor.execute("INSERT INTO products (id, name, quantity) VALUES (?, ?, ?)", (self.id, self.name, self.quantity))
        conn.commit()

class Authentication:
    def login(self, email, password):
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user_data = cursor.fetchone()
        if user_data:
            print("Вход выполнен успешно")
        else:
            print("Неверный email или пароль")
            
class CashiersAuthentication:
    def login(self, email, password):
        cursor.execute("SELECT * FROM cashiers WHERE email = ? AND password = ?", (email, password))
        cashier_data = cursor.fetchone()
        if cashier_data:
            print("Вход выполнен успешно")
        else:
            print("Неверный email или пароль")

class UsersRegistration:
    def register(self, name, email, age, password): 
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            print("Пользователь с таким адресом электронной почты уже зарегистрирован")
        else:
            cursor.execute("INSERT INTO users (name, email, age, password) VALUES (?, ?, ?, ?)", (name, email, age, password))
            conn.commit()
            print("Регистрация прошла успешно")


class Orders:
    def place_order(self, user_id, product_id, quantity):
        cursor.execute("INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, quantity))
        conn.commit()
        print("Заказ размещен успешно")

    def view_orders(self, user_id):
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        user_orders = cursor.fetchall()
        if user_orders:
            for order in user_orders:
                print("Заказ ID:", order, "Продукт ID:", order, "Количество:", order, "Дата заказа:", order)
        else:
            print("У пользователя пока нет заказов")


def main():
    auth = Authentication()
    cash_auth = CashiersAuthentication()
    orders = Orders()

    while True:
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("3. Разместить заказ")
        print("4. Просмотреть заказы")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            email = input("Введите ваш email: ")
            password = input("Введите ваш пароль: ")
            user_id = auth.login(email, password)
        elif choice == "2":
            name = input("Введите ваше имя: ")
            email = input("Введите ваш email: ")
            age = input("Введите ваш возраст: ")
            password = input("Введите ваш пароль: ")
            user_id = auth.register(name, email, age, password)
        elif choice == "3":
            if user_id:
                product_id = input("Введите ID продукта: ")
                quantity = input("Введите количество: ")
                orders.place_order(user_id, product_id, quantity)
            else:
                print("Сначала войдите в систему")
        elif choice == "4":
            if user_id:
                orders.view_orders(user_id)
            else:
                print("Сначала войдите в систему")

        elif choice == "5":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова")

if __name__ == "__main__":
    main()
