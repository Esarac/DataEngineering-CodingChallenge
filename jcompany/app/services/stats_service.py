from sqlalchemy import and_, text

from app.model.employee import Employee, Department, Job
from app.utils.db import db

def count_employees_per_department_and_job_in_2021():
    return db.session.query(
            Department.name
            ,Job.name
            ,db.func.sum(db.func.IF(and_(Employee.datetime >= '2021-01-01', Employee.datetime < '2021-04-01'), 1, 0)).label('Q1')
            ,db.func.sum(db.func.IF(and_(Employee.datetime >= '2021-04-01', Employee.datetime < '2021-07-01'), 1, 0)).label('Q2')
            ,db.func.sum(db.func.IF(and_(Employee.datetime >= '2021-07-01', Employee.datetime < '2021-10-01'), 1, 0)).label('Q3')
            ,db.func.sum(db.func.IF(and_(Employee.datetime >= '2021-10-01', Employee.datetime < '2022-01-01'), 1, 0)).label('Q4')
        )\
        .join(Department)\
        .join(Job)\
        .where(and_(Employee.datetime >= '2021-01-01', Employee.datetime < '2022-01-01'))\
        .group_by(Department.name, Department.id, Job.name, Job.id)\
        .order_by(Department.name.desc(), Job.name.desc())\
        .all()

def count_employees_per_department_greater_than_mean_in_2021():
    subquery = db.session.query(
        Department.id
        ,Department.name
        ,db.func.count(Employee.id).label('hired')
    )\
    .join(Employee)\
    .where(and_(Employee.datetime >= '2021-01-01', Employee.datetime < '2022-01-01'))\
    .group_by(Department.id, Department.name)\
    .subquery()

    mean_subquery = db.session.query(
        db.func.avg(subquery.c.hired).label('mean')
    ).subquery()

    return db.session.query(
        subquery.c.id
        ,subquery.c.name
        ,subquery.c.hired
    ) \
    .join(mean_subquery, subquery.c.hired > mean_subquery.c.mean)\
    .order_by(subquery.c.hired.desc())\
    .all()

# def count_employees_per_department_and_job_in_2021():
#     query = text("""
#         SELECT d.name AS department_name, j.name AS job_name,
#             SUM(CASE WHEN e.datetime >= '2021-01-01' AND e.datetime < '2021-04-01' THEN 1 ELSE 0 END) AS Q1,
#             SUM(CASE WHEN e.datetime >= '2021-04-01' AND e.datetime < '2021-07-01' THEN 1 ELSE 0 END) AS Q2,
#             SUM(CASE WHEN e.datetime >= '2021-07-01' AND e.datetime < '2021-10-01' THEN 1 ELSE 0 END) AS Q3,
#             SUM(CASE WHEN e.datetime >= '2021-10-01' AND e.datetime < '2022-01-01' THEN 1 ELSE 0 END) AS Q4
#         FROM department d
#         JOIN employee e ON d.id = e.department_id
#         JOIN job j ON j.id = e.job_id
#         WHERE e.datetime >= '2021-01-01' AND e.datetime < '2022-01-01'
#         GROUP BY d.name, d.id, j.name, j.id
#         ORDER BY d.name DESC, j.name DESC
#     """)
#     return db.session.execute(query).fetchall()

# def count_employees_per_department_greater_than_mean_in_2021():
#     query = text("""
#         SELECT d.id, d.name, COUNT(e.id) AS hired
#         FROM department d
#         JOIN employee e ON d.id = e.department_id
#         WHERE e.datetime >= '2021-01-01' AND e.datetime < '2022-01-01'
#         GROUP BY d.id, d.name
#         HAVING COUNT(e.id) > (
#             SELECT AVG(hired)
#             FROM (
#                 SELECT COUNT(e.id) AS hired
#                 FROM department d
#                 JOIN employee e ON d.id = e.department_id
#                 WHERE e.datetime >= '2021-01-01' AND e.datetime < '2022-01-01'
#                 GROUP BY d.id, d.name
#             ) avg_subquery
#         )
#         ORDER BY hired DESC
#     """)
#     return db.session.execute(query).fetchall()