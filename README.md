# Student Management System

A menu-driven **Python + MySQL** application to manage student records in a school.
This project allows adding, viewing, updating, deleting, and searching student details using a simple command-line interface.

---

## 📌 Features

* ➕ Add new students
* 📋 View all students in a formatted table
* ✏️ Update student information (name, class, marks, etc.)
* ❌ Delete student records
* 🔍 Search for students by admission number (extendable to name/class)

---

## 🛠 Requirements

* Python 3.8+
* MySQL Server
* Python libraries:

  * `mysql-connector-python`
  * `prettytable`

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Database Setup

1. Open MySQL and create a database:

   ```sql
   CREATE DATABASE student_db;
   ```

2. Create the `students` table (or let your program’s `init_db()` handle it if added):

   ```sql
   CREATE TABLE students (
       AdmNo INT PRIMARY KEY,
       Name VARCHAR(100),
       Class VARCHAR(20),
       Marks INT,
       DOB DATE,
       Gender VARCHAR(10),
       Address VARCHAR(255),
       Phone VARCHAR(15)
   );
   ```

---

## ▶️ Usage

Run the program with:

```bash
python student_mgmt.py
```

You’ll see a menu like:

```
Student Management System
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit
```

Follow the prompts to manage student records.

---

## 📂 Project Structure

```
student-management-system/
│── student_mgmt.py        # Main program file
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── .gitignore             # Ignored files for Git
```

---

## 🚀 Future Enhancements

* Search students by name, class, or partial matches
* Show class toppers / average marks
* Export records to CSV/Excel
* Add login system for teachers/admins

---

## 👨‍💻 Author

*Developed as a Computer Science project for managing school student records.*
