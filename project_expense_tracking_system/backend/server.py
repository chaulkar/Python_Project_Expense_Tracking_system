from fastapi import FastAPI, HTTPException
from datetime import date



import db_helper
from typing import List
from pydantic import BaseModel

app=FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date



@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from database")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expense(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message":"Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(daterange: DateRange):
    data= db_helper.fetch_expense_summary_by_category(daterange.start_date, daterange.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from database")

    total = sum([row["total"] for row in data])

    breakdown ={}

    for row in data:
        percentage = (row["total"]/total)*100 if total != 0 else 0
        breakdown[row["category"]] = {
            "total": row["total"],
            "percentage": percentage
        }

    return breakdown

@app.get("/analytics/months/{expense_year}")
def get_analytics_by_months(expense_year: int):
    data = db_helper.fetch_expense_summary_by_months(expense_year)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve month-wise expense summary from database")
    return data

