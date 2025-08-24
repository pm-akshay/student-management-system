                                     #COMPUTER PROJECT

import mysql.connector
from prettytable import PrettyTable

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",        
        passwd="mysql",    
        database="student_db"
    )
    return connection

def add_student():
    name = input("Enter name: ")
    adm_no = int(input("Enter admission number: "))
    class_name = input("Enter class: ")
    marks = int(input("Enter marks: "))
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    gender = input("Enter gender (Male/Female/Other): ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")

    connection = connect_db()
    cursor = connection.cursor()
    
    sql = """
    INSERT INTO students (AdmNo, Name, Class, Marks, DOB, Gender, Address, Phone)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (adm_no, name, class_name, marks, dob, gender, address, phone)
    
    cursor.execute(sql, values)
    connection.commit()
    
    print(f"Student {name} added successfully.")   
    connection.close()

def view_students():
    connection = connect_db()
    cursor = connection.cursor()
    table = PrettyTable()
    table.field_names = ['AdmNo', 'Name', 'Class', 'Marks', 'DOB', 'Gender', 'Address', 'Phone']
    cursor.execute("SELECT * FROM students")
    for student in cursor.fetchall():
        table.add_row(list(student))
    print(table)
    cursor.close()
    connection.close()

def validate_input(data, datatype, field_name):
    if datatype == int:
        try:
            return int(data)
        except ValueError:
            print(f"Invalid input for {field_name}. Please enter an integer.")
            return None
    return data

def update_student():
    admno = int(input("Enter admission number of the student to update: "))
    
    connection = connect_db()
    cursor = connection.cursor()
    
    # Check if the student exists
    cursor.execute("SELECT * FROM students WHERE AdmNo = %s", (admno,))
    student = cursor.fetchone()
    
    if not student:
        print("No student found with the given admission number.")
        cursor.close()
        connection.close()
        return

    field_choice = input("Which detail do you want to update? (1) Name (2) Class (3) Marks (4) DOB (5) Gender (6) Address (7) Phone: ")

    if field_choice == '1':
        new_value = input("Enter new name: ")
        sql = "UPDATE students SET Name = %s WHERE AdmNo = %s"
        cursor.execute(sql, (new_value, admno))
    elif field_choice == '2':
        new_value = input("Enter new class: ")
        sql = "UPDATE students SET Class = %s WHERE AdmNo = %s"
        cursor.execute(sql, (new_value, admno))
    elif field_choice == '3':
        new_value = int(input("Enter new marks: "))
        sql = "UPDATE students SET Marks = %s WHERE AdmNo = %s"
        cursor.execute(sql, (new_value, admno))
    elif field_choice == '4':
        new_value = input("Enter new date of birth (YYYY-MM-DD): ")
        sql = "UPDATE students SET DOB = %s WHERE AdmNo = %s"
        cursor.execute(sql, (new_value, admno))
    elif field_choice == '5':
        new_value = input("Enter new gender (Male/Female/Other): ")
        sql = "UPDATE students SET Gender = %s WHERE AdmNo = %s"
        cursor.execute(sql, (new_value, admno))
    elif field_choice == '6':
        new_value = input("Enter new address: ")
        sql = "UPDATE students SET Address = %s WHERE AdmNo = %s"
        cursor.execute(sql, (new_value, admno))
    elif field_choice == '7':
        new_value = input("Enter new phone number: ")
        sql = "UPDATE students SET Phone = %s WHERE AdmNo = %s"
        cursor.execute(sql, (new_value, admno))
    else:
        print("Invalid choice.")
        cursor.close()
        connection.close()
        return

    connection.commit()
    print(f"Student with AdmNo {admno} updated successfully.")

    # Confirm update by printing all students
    cursor.execute("SELECT * FROM students")
    table = PrettyTable()
    table.field_names = ['AdmNo', 'Name', 'Class', 'Marks', 'DOB', 'Gender', 'Address', 'Phone']
    for student in cursor.fetchall():
        table.add_row(list(student))
    print(table)

    cursor.close()
    connection.close()

def delete_student():
    adm_no = input("Enter admission number of the student to delete: ")

    connection = connect_db()
    cursor = connection.cursor()
    
    sql = "DELETE FROM students WHERE AdmNo = %s"
    cursor.execute(sql, (adm_no,))
    connection.commit()
    
    print(f"Student with admission number {adm_no} deleted.")
    connection.close()

def search_student():
    adm_no = validate_input(input("Enter admission number to search: "), int, "admission number")
    if adm_no is None:
        return  # Return to menu if validation fails

    connection = connect_db()
    cursor = connection.cursor()
    table = PrettyTable()
    table.field_names = ['AdmNo', 'Name', 'Class', 'Marks', 'DOB', 'Gender', 'Address', 'Phone']

    cursor.execute("SELECT * FROM students WHERE AdmNo = %s", (adm_no,))
    results = cursor.fetchall()
    
    if results:
        for student in results:
            table.add_row(list(student))  # Add each student record to the table
        print(table)  # Display the table
    else:
        print("No students found.")
    
    cursor.close()
    connection.close()

def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("Exiting")
            break
        else:
            print("Invalid choice, please try again.")

        # Ask to continue
        choice = input("Do you want to continue (Y/N)? ").strip().lower()
        if choice != 'y':
            print("Exiting the system...")
            break

if __name__ == "__main__":
    main_menu()
                                                                    


