# Expense Tracking System

[LinkedIn post demonstrating application working](https://www.linkedin.com/posts/shreyas-chaulkar-337669190_python-fastapi-streamlit-activity-7337924158460149761-cxtV?utm_source=share&utm_medium=member_desktop&rcm=ACoAACzyrJsBnNWK3_fC1nmWurykPc4QtEv_TaU)

This Expense Tracking System project consists streamlit
frontend application and FASTAPI backend server.



## Project Structure

- **frontend/**: contain streamlit application code.
- **backend/**: contains FASTAPI backend server code.
- **tests/**: contains test cases for backend.
- **requirements.txt**: List the required python packages
- **README.md**: Gives overview and instructions for project.

## Setup Instructions

1. **MySQL Database setup**:

- Create a database named `expense_manager`.
- Inside it, create a table named `expenses` 
with the following structure:
```sql
CREATE DATABASE expense_manager;

USE expense_manager;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount FLOAT NOT NULL,
    category VARCHAR(255) NOT NULL,
    notes TEXT
);
```

2. **Changes to do in `db_helper.py`**:
``` python
def get_db_cursor(commit=False):
    connection=mysql.connector.connect(
        host="add your hostname",
        user="add your username",
        password="add your password",
        database="expense_manager"
    )
```



3. **Install dependencies**:
```commandline
pip install -r requirements.txt
```

4. **Run the fastapi server**:
```commandline
cd backend
uvicorn server:app --reload --port 9000
```

5. **Run the streamlit app**:
```commandline
cd frontend
streamlit run .\app.py
```





