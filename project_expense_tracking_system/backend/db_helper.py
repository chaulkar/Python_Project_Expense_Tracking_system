import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch expenses for date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s",(expense_date,))
        expenses=cursor.fetchall()
        return expenses


def insert_expense(expense_date,amount,category,notes):
    logger.info(f"insert expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("insert into expenses(expense_date,amount,category,notes) values(%s,%s,%s,%s)",
                       (expense_date,amount,category,notes))

def delete_expense(expense_date):
    logger.info(f"delete expenses for date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date = %s",(expense_date,))

def fetch_expense_summary_by_category(start_date,end_date):
    logger.info(f"fetch expense summary called with start_date: {start_date}, end_date: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''select category,sum(amount) as total
               from expenses 
               where expense_date between %s and %s
               group by category''',
            (start_date,end_date)
        )
        data=cursor.fetchall()
        return data

def fetch_expense_summary_by_months(expense_year):
    logger.info(f"fetch expense summary by months")
    with get_db_cursor() as cursor:
        cursor.execute(
            """with cte as
	           (select concat(left(monthname(expense_date),3),"-",right(year(expense_date),2)) as month_name,
	           YEAR(expense_date) AS yr,MONTH(expense_date) AS mon,amount from expenses)
               select month_name,sum(amount) as total from cte where yr = %s
               group by mon,month_name
                order by mon asc """,
            (expense_year,)
        )
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    # expense=fetch_expenses_for_date("2024-08-03")
    # print(expense)
    # summary = fetch_expense_summary("2024-08-01","2024-08-05")
    # for expense in summary:
    #     print(expense)
    summary=fetch_expense_summary_by_months("2024")
    for expense in summary:
        print(expense)








