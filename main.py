from datetime import datetime
from application import people, salary

if __name__ == '__main__':

    print(f'{datetime.now().date()}\nКалькулятор зарплаты и имени сотрудника\n')

    '''salary'''
    sal = salary.Salary(int(input('Введите вашу зарплату: ')))
    sal.calculate_salary()

    '''people'''
    pep = people.Employees(input('Введите имя сотрудника: '))
    pep.get_employees()