from datetime import date
import time

from sqlalchemy.orm import joinedload

from models import Employee, Payment


# 11,28 сек без lazy="joined"
def employees_and_payments():
    employees_list = []
    for payment in Payment.query.filter(Payment.payment_date > date(2020, 12, 1)):
        employees_list.append(
          f"{payment.employee.company.name} - {payment.employee.name}: {payment.ammount}"
        )
    return employees_list
###########################################################################


# 2,96 сек без lazy="joined"
def employees_and_companies_joined():
    employees_list = []
    query = Payment.query.options(
        joinedload(Payment.employee).joinedload(Employee.company)
    ).filter(Payment.payment_date > date(2020, 12, 1))
    for payment in query:
        employees_list.append(
          f"{payment.employee.company.name} - {payment.employee.name}: {payment.ammount}"
        )
    return employees_list



if __name__ == '__main__':
    start = time.perf_counter()
    for _ in range(100):
        employees_and_payments()
    print(f'employees_and_payments {time.perf_counter() - start}')

    start = time.perf_counter()
    for _ in range(100):
        employees_and_companies_joined()
    print(f'employees_and_companies_joined {time.perf_counter() - start}')