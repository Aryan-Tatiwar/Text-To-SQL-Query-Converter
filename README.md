# 🧠 Text-to-SQL Data Retriever using Gemini + Streamlit

An AI-powered Streamlit application that converts natural language questions into executable SQL queries using Google's Gemini LLM and retrieves data from a SQLite database.

---

## 🚀 Project Overview

This application allows users to:

- Ask questions in plain English
- Automatically convert the question into a valid SQL query using Gemini
- Execute the query on a SQLite database
- Display the results in a clean Streamlit UI

Example questions:

- How many employees are present in the table?
- Show all employees in Engineering department
- What is the highest salary in Marketing?

---

## 🏗️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- SQLite
- python-dotenv

---

## 📂 Project Structure

.
├── app.py              # Main Streamlit application  
├── sql.py              # Database creation + sample data insertion  
├── company_data.db     # SQLite database (generated after running sql.py)  
├── requirements.txt  
├── .env.example  
├── .gitignore  
└── README.md  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Aryan-Tatiwar/Text-To-SQL-Query-Converter.git
cd Text-To-SQL-Query-Converter
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is missing:

```bash
pip install streamlit google-generativeai python-dotenv
```

### 4️⃣ Set Your Gemini API Key

Create a file named:

.env

Inside it:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

⚠️ Never push your real API key to GitHub.

### 5️⃣ Create the Database

```bash
python sql.py
```

This will:
- Create `company_data.db`
- Create `employees` table
- Insert 21 sample records

### 6️⃣ Run the Application

```bash
streamlit run app.py
```

Then open:

http://localhost:8501

---

## 🧠 How It Works

1. User enters a natural language question.
2. The app sends the question + database schema prompt to Gemini.
3. Gemini generates a raw SQL query.
4. The query is executed on SQLite.
5. Results are displayed in a Streamlit table.

---

## 🔐 Security Notes

- `.env` is ignored using `.gitignore`
- API keys are never hardcoded
- The model is instructed to return only raw SQL
- Only a single predefined table (`employees`) is accessible

---

## 📊 Database Schema

Table: `employees`

| Column        | Type    |
|--------------|---------|
| employee_id  | INTEGER (Primary Key) |
| first_name   | TEXT |
| last_name    | TEXT |
| department   | TEXT |
| hire_date    | DATE |
| salary       | REAL |

---

## 🎯 Key Features

✔ Natural Language to SQL conversion  
✔ LLM-powered query generation  
✔ SQLite database integration  
✔ Interactive Streamlit interface  
✔ Error handling for invalid SQL  

---

## 📌 Future Improvements

- Add query validation layer
- Add SQL injection protection
- Support multiple tables
- Add authentication system
- Deploy on Streamlit Cloud

---

## 👨‍💻 Author

Aryan Tatiwar  
AI & Full Stack Development Enthusiast  


