import time
import csv
from db import db_session
from db2.models import Salary


# !НЕ БЫСТРЫЙ СПОСОБ!
# можно использовать, если для загрузки около 10 строк. 
def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city_name', 'street_address', 'large_company',
                  'job', 'phone_number', 'free_email', 'date_of_birth',
                  'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            save_salary_data(row)


def save_salary_data(row):
    salary = Salary(name=row['name'], city=row['city_name'],
            address=row['street_address'],
            company=row['large_company'], job=row['job'],
            phone_number=row['phone_number'],
            email=row['free_email'], date_of_birth=row['date_of_birth'],
            salary=row['salary'])
    db_session.add(salary)
    db_session.commit()


#############################################################################

# ! БЫСТРЫЙ СПОСОБ ! 
# можно использовать, когда для загрузки много строк
# на 1000 строк занимает времени 0,5 сек вместо 8,3 сек
def read_csv2(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city', 'address', 'company',
                'job', 'phone_number', 'email', 'date_of_birth', 'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        salary_data = []
        for row in reader:
            salary_data.append(row)
        save_salary_data2(salary_data)


def save_salary_data2(salary_data):
    db_session.bulk_insert_mappings(Salary, salary_data)
    db_session.commit()



if __name__ == '__main__':
    # start = time.time()
    # read_csv('salary.csv')
    # print('Данные загружены за ', time.time() - start)

    start = time.time()
    read_csv2('salary.csv')
    print('Данные загружены за ', time.time() - start)