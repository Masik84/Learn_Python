from sqlalchemy import desc
from sqlalchemy.sql import func

from db import db_session
from db2.models import Salary


# Несколько самых больших зарплат
# Отсортируем зарплаты по убыванию с помощью order_by 
# и выведем несколько первых с помощью limit

def top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)

    for salary in top_salary:
        print(f'З/п {salary.salary}')
#######################################################################

# Cписок зарплат для города
# Отфильтровать нужные нам данные с помощью filter

def salary_by_city(city_name):
    top_salary = Salary.query.filter(Salary.city == city_name).order_by(Salary.salary.desc())
    print(city_name)

    for salary in top_salary:
        print(f'З/п {salary.salary}')
########################################################################

# Топ зарплат по домену email
# filter позволяет искать данные по подстроке, # используя like и знак % 
# обозначающий "любые символы"

def top_salary_by_domain(domain, num_rows):
    top_salary = Salary.query.filter(Salary.email.ilike(f'%{domain}')).order_by(Salary.salary).limit(num_rows)

    print(domain)
    for salary in top_salary:
        print(f'З/п {salary.salary}')
#########################################################################

# Посчитать среднее
# Здесь func.avg говорит базе, что нам нужно посчитать среднее, 
# а scalar возвращает единственное значение вместо строки
def average_salary():
    result = db_session.query(func.avg(Salary.salary)).scalar()
    print(f"Средняя зарплата {result:.2f}")
#########################################################################

# Количество уникальных городов
# Здесь мы выбираем только одно поле Salary.city, а group_by группирует города, чтобы count их посчитал:

def distinct_cities():
    cities_count = db_session.query(Salary.city).group_by(Salary.city).count()
    print(f"В базе {cities_count} городов")
#########################################################################

# Где самая большая средняя зарплата
def top_average_salary_by_city(num_rows):
    avg_salary = db_session.query(
        Salary.city,func.avg(Salary.salary).label('avg_salary')
    ).group_by(Salary.city).order_by(desc('avg_salary')).limit(num_rows)

    for city, salary in avg_salary:
        print(f"Город: {city}, средняя з/п: {salary:.0f}")



if __name__ == '__main__':
    top_salary(5)
    salary_by_city('Адыгейск')
    top_salary_by_domain('@yandex.ru', 5)
    average_salary()
    distinct_cities()
    top_average_salary_by_city(10)