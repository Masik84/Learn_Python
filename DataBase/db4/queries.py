from sqlalchemy import func

from db import db_session
from models import Project, Company, ProjectEmployee, Employee


# Получим список сотрудников по проектам компании и узнаем, 
# сколько дней каждый из сотрудников работал над проектом
def company_projects_employees(company_name):
        query = Project.query.join(Project.company, Project.employees).filter(Company.name == company_name)
    
        for project in query:
            print('-' * 20)
            print(project.name)
            for employee in project.employees:
                print(f"{employee.employee.name} {(employee.date_end - employee.date_start).days} день")
###########################################################################
                

def projects_time_total(company_name):
    query = db_session.query(
        Project.name, func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees
    ).filter(Company.name == company_name).group_by(Project.name)

    for row in query:
        print(f'Проект "{row[0]}" -- {row[1]} дней')
###########################################################################


# Вместо обращения по индексам, удобнее использовать распаковку кортежа
def projects_time_total2(company_name):
    query = db_session.query(
        Project.name, func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees
    ).filter(Company.name == company_name).group_by(Project.name)

    for project_name, project_len in query:
        print(f'Проект "{project_name}" -- {project_len} дней')
###########################################################################


# Группировки
# Более сложный случай - суммарное время работы каждого сотрудника над проектом:
def projects_employees_time_total(company_name):
    query = db_session.query(
        Project.name, Employee.name,
        func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees, ProjectEmployee.employee
    ).filter(Company.name == company_name).group_by(Project.name, Employee.name)

    for project_name, employee_name, project_len in query:
        print(f'Проект "{project_name}", {employee_name} -- {project_len} дней')



if __name__ == '__main__':
    # company_projects_employees('Метро Кэш энд Керри (Metro Cash & Carry)')
    # projects_time_total('Метро Кэш энд Керри (Metro Cash & Carry)')
    # projects_time_total2('Метро Кэш энд Керри (Metro Cash & Carry)')
    projects_employees_time_total('Метро Кэш энд Керри (Metro Cash & Carry)')