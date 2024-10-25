import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='Register',
    user='root',
    password='7804'
)


class Register_User:
    def __init__(self, name, family, filed, age):
        self.name = name
        self.family = family
        self.filed = filed
        self.age = age

    def add_user(self):
        cursor = connection.cursor()

        sql_insert_query = """INSERT INTO Register_User (name, family, filde, age) 
                                      VALUES (%s, %s, %s, %s)"""
        # داده‌های کاربر
        record_to_insert = (self.name, self.family, self.filed, self.age)

        # اجرای دستور SQL
        cursor.execute(sql_insert_query, record_to_insert)

        # تایید تغییرات در دیتابیس
        connection.commit()
