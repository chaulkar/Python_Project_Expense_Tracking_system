from backend import db_helper


def test_fetch_expenses_for_date_valid():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")
    assert len(expenses) == 1

    assert expenses[0]["category"] == "Shopping"
    assert expenses[0]["amount"] == 10
    assert expenses[0]["notes"] == "Bought potatoes"

def test_fetch_expenses_for_date_invalid():
    expense=db_helper.fetch_expenses_for_date("2028-09-10")
    assert len(expense) == 0

def test_fetch_expense_summary_invalid_date():
    expenses=db_helper.fetch_expense_summary("2025-10-10","2025-12-10")
    assert len(expenses) == 0





