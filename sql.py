import sqlite3
import os

# Database file name MUST match the one used in app.py
DB_NAME = "company_data.db" 

print(f"Connecting to database: {DB_NAME}")

## Connect to sqlite
try:
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # 1. Create the table using IF NOT EXISTS to prevent errors on repeated runs
    table_info = """
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        department TEXT,
        hire_date DATE,
        salary REAL
    );
    """
    cursor.execute(table_info)

    # 2. Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM employees")
    count = cursor.fetchone()[0]

    if count == 0:
        print("Inserting 21 new records...")
        # Insert 21 records
        cursor.execute("INSERT INTO employees VALUES(101, 'Alex', 'Smith', 'Marketing', '2020-05-15', 65000.00)")
        cursor.execute("INSERT INTO employees VALUES(102, 'Beca', 'Jones', 'Engineering', '2019-01-20', 92000.00)")
        cursor.execute("INSERT INTO employees VALUES(103, 'Chris', 'Lee', 'Sales', '2021-11-01', 58500.00)")
        cursor.execute("INSERT INTO employees VALUES(104, 'Dana', 'Wong', 'Engineering', '2022-07-25', 88000.00)")
        cursor.execute("INSERT INTO employees VALUES(105, 'Evan', 'Brown', 'Marketing', '2018-03-10', 71500.00)")
        cursor.execute("INSERT INTO employees VALUES(106, 'Fiona', 'Garcia', 'HR', '2017-06-05', 62000.00)")
        cursor.execute("INSERT INTO employees VALUES(107, 'George', 'Miller', 'Finance', '2023-01-12', 105000.00)")
        cursor.execute("INSERT INTO employees VALUES(108, 'Hannah', 'Davis', 'Engineering', '2020-10-10', 95000.00)")
        cursor.execute("INSERT INTO employees VALUES(109, 'Ian', 'Rodriguez', 'Sales', '2016-04-22', 75000.00)")
        cursor.execute("INSERT INTO employees VALUES(110, 'Julia', 'Wilson', 'Marketing', '2022-09-18', 68000.00)")
        cursor.execute("INSERT INTO employees VALUES(111, 'Kyle', 'Martinez', 'HR', '2019-08-30', 55000.00)")
        cursor.execute("INSERT INTO employees VALUES(112, 'Lara', 'Anderson', 'Finance', '2021-02-14', 115000.00)")
        cursor.execute("INSERT INTO employees VALUES(113, 'Mark', 'Thomas', 'Engineering', '2015-12-01', 120000.00)")
        cursor.execute("INSERT INTO employees VALUES(114, 'Nora', 'Taylor', 'Sales', '2023-05-07', 62500.00)")
        cursor.execute("INSERT INTO employees VALUES(115, 'Oscar', 'Clark', 'Marketing', '2017-11-11', 78000.00)")
        cursor.execute("INSERT INTO employees VALUES(116, 'Penny', 'Hall', 'HR', '2024-03-01', 52000.00)")
        cursor.execute("INSERT INTO employees VALUES(117, 'Quinn', 'Moore', 'Finance', '2020-07-04', 100000.00)")
        cursor.execute("INSERT INTO employees VALUES(118, 'Ryan', 'White', 'Engineering', '2018-02-28', 105500.00)")
        cursor.execute("INSERT INTO employees VALUES(119, 'Sara', 'Harris', 'Sales', '2021-04-19', 61000.00)")
        cursor.execute("INSERT INTO employees VALUES(120, 'Tom', 'Lewis', 'Marketing', '2019-11-23', 70000.00)")
        cursor.execute("INSERT INTO employees VALUES(121, 'Uma', 'Walker', 'HR', '2022-10-05', 60000.00)")
        print("21 sample records inserted.")
    else:
        print(f"Table 'employees' already contains {count} records. Skipping data insertion.")

    # 3. Display the records for confirmation
    print("\nThe first 5 records in the table:")
    data = cursor.execute('''SELECT * FROM employees LIMIT 5''')
    for row in data:
        print(row)
        
    # 4. Commit changes and close the connection
    connection.commit()
    connection.close()
    print("\nDatabase setup complete and connection closed.")

except sqlite3.Error as e:
    print(f"\nAn error occurred during database setup (This often means the file is locked or corrupt): {e}")
