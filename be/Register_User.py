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
        record_to_insert = (self.name, self.family, self.filed, self.age)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

    def all_users(self):
        cursor = connection.cursor()
        sql_insert_query = """SELECT * FROM Register_User"""
        cursor.execute(sql_insert_query)
        records = cursor.fetchall()
        return records

    def delete_user(self, id):
        cursor = connection.cursor()
        sql_insert_query = """DELETE from Register_User where id = %s"""
        cursor.execute(sql_insert_query, (id,))
        connection.commit()
        cursor.close()
        return True

    def update_user(self, name, family, filde, age, id):
        cursor = connection.cursor()
        sql_insert_query = """UPDATE Register_User set name = %s, family = %s, filde = %s, age = %s where id = %s"""
        cursor.execute(sql_insert_query, (name, family, filde, age, id))
        connection.commit()
        cursor.close()
        return True

    def search_user(self, name):
        cursor = connection.cursor()
        sql_insert_query = """select * from Register_User where name = %s"""
        cursor.execute(sql_insert_query, (name,))
        records = cursor.fetchall()
        return records

