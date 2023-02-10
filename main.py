import sqlite3
import sys

class Database():
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor =  self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            first_name TEXT(20),
            last_name TEXT(20),
            salary INT(20)
        )""")
        self.connection.commit()

    def insert(self,first_name,last_name, salary):
        self.cursor.execute(f"INSERT INTO employee (first_name,last_name,salary) VALUES ('{first_name}', '{last_name}', {salary})")
        self.connection.commit()

    def remove(self,first_name, last_name):
        self.cursor.execute(f"DELETE FROM employee WHERE first_name = '{first_name}' AND last_name = '{last_name}' ")
        self.connection.commit()

    def edit_salary(self, first_name, last_name, salary):
        self.cursor.execute(f"UPDATE employee SET salary = {salary} WHERE first_name = '{first_name}' AND  last_name = '{last_name}' ")
        self.connection.commit()

    def show(self):
        self.cursor.execute(f"SELECT first_name, last_name, salary FROM employee")
        self.a = self.cursor.fetchall()
        if len(self.a ) > 0:
            print('\nDataBase:\n')
            print('-'*82)
            for items in self.a:
                print('First Name: {:15} | Last Name: {:15} | Salary: {:<15}'.format(items[0],items[1],items[2]))
                print('-'*82)
            print()
        else:
            print('The DataBase is empty')
            
class Aplication():
    def __init__(self):
        self.status = True

    def Turn_on(self):
        self.status = True   

    def Turn_off(self):
        self.status = False


def menu_show():
    print('\nWite the number corresponding to the desired option: ')
    print('0 : Hire an employee')
    print('1 : Fire an employee')
    print('2 : Edit an employee salary')
    print('3 : Displays the employee database')
    print('4 : Exit')

def main():
    aplication = Aplication()
    db = Database()

    def menu_action(option):
        if option == 0 :
            first_name = input('Enter the first name of the employee: ')
            last_name = input('Enter the last name of the employee: ')
            salary = input('Enter the salary of the employee: ')
            db.insert(first_name.title(), last_name.title(), salary)

        elif option == 1 :
            first_name = input('Give the first name of the employee you want to fire: ')
            last_name = input('Give the last name of the employee you want to fire: ')
            db.remove(first_name.title(), last_name.title())

        elif option == 2 :
            first_name = input('Give the First Name of the employee whose salary you want to edit: ')
            last_name = input('Give the Last Name of the employee whose salary you want to edit: ')
            salary = int(input('Give the new salary: '))
            db.edit_salary(first_name,last_name,salary)
        
        elif option == 3 :
            db.show()

        elif option == 4 :
            db.connection.close()
            aplication.status = False
            print('The application has stopped')
    
    while aplication.status:
        try:
            menu_show()
            option = int(input('Enter the number: '))
            menu_action(option)
        except:
            print("There was a problem. Try again.")

main()