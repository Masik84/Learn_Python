# Как получать данные?
# Возьмем простую задачу: найти компанию по названию и вывести 
# для нее все сотрудников. Эту задачу можно решить несколькими способами:

# Самый очевидный способ - найти Company, затем получить всех Employee по company_id
# Если вы раньше работали с базами данных, очевидный вариант - сделать join
# Использовать relationship удобный механизм, который предоставляет SQLAlchemy для получения данных из связанных таблиц


from db import db_session
from models import Company, Employee, Payment
import time


# Первый вариант (3.036 сек)
def employees_by_company(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    employee_list = []
    if company:
        for employee in Employee.query.filter(Employee.company_id == company.id):
            employee_list.append(f"{company.name} - сотрудник {employee.name}")

    return employee_list
###########################################################################

# Второй вариант (2.575 сек)
# Второй вариант быстрее первого, т.к. вместо 2-х запросов мы делаем один.
def employees_by_company_joined(company_name):
    employee_list = []
    query = db_session.query(Employee, Company).join(
        Company, Employee.company_id == Company.id
    ).filter(Company.name == company_name)

    for employee, company in query:
        employee_list.append(f"{company.name} - сотрудник {employee.name}")

    return employee_list
###########################################################################

# Третий вариант (2.489 сек)
def employee_by_company_relation(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    employee_list = []
    if company:
        for employee in company.employees:
            employee_list.append(f"{company.name} - сотрудник {employee.name}")

    return employee_list



if __name__ == '__main__':
    # Вар 1
    start = time.perf_counter()
    for _ in range(100):
        employees_by_company("Стройгазмонтаж")
    print(f'employees_by_company {time.perf_counter() - start}')

    # Вар 2
    start = time.perf_counter()
    for _ in range(100):
        employees_by_company_joined("Стройгазмонтаж")
    print(f'employees_by_company_joined {time.perf_counter() - start}')

    # Вар 3
    start = time.perf_counter()
    for _ in range(100):
        employee_by_company_relation("Стройгазмонтаж")
    print(f'employee_by_company_relation {time.perf_counter() - start}')
