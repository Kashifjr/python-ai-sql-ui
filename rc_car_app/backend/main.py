import mysql.connector
'''
The progam will allow users to connect to a MySQL database using python as a 
database connector and using the command line interface. Users will be able to 
edit, insert, delete, view and update records in the database.
Future updates: create new tables, change current table, deletion of tables
'''
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # replace with your MySQL username
    password="shika",  # replace with your MySQL password
    database="mysql"  # replace with your database name
)

# create cursor
cursor = conn.cursor()
# test connection
cursor.execute("SELECT DATABASE();")
print("Connected to:", cursor.fetchone())

# create table if not exists, rc_cars
cursor.execute("""
CREATE TABLE IF NOT EXISTS rc_cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(100),
    model VARCHAR(100),
    price DECIMAL(5,2)
)
""")

# generate menu and user options
def display_menu():
    border = "==============================="
    border2 = "-------------------------------"
    print(border)
    print("RC Car Database Menu")
    print(border2)
    print("1...Insert new RC car record")
    print("2...View all RC car records")
    print("3...Update an RC car record")
    print("4...Delete an RC car record")
    print("q...Exit")
    print(border+"\n")
# generate functions for each option
# insert record
def insert_record():
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    price = float(input("Enter car price: "))
    cursor.execute("INSERT INTO rc_cars (brand, model, price) VALUES (%s, %s, %s)", (brand, model, price))
    conn.commit()
    print("The record \""+brand+" "+model+"\" was inserted successfully.\n")
# view records
def view_records():
    cursor.execute("SELECT * FROM rc_cars")
    records = cursor.fetchall()
    print("\nRC Car Records:")
    for row in records:
        print(f"ID: {row[0]}, Brand: {row[1]}, Model: {row[2]}, Price: ${row[3]}")
    print()
    # print(row)
# update record
# search for car model by id or model and name combo?
def update_record():
    car_id = int(input("Enter the ID of the car to update: "))
    new_brand = input("Enter new brand: ")
    new_model = input("Enter new model: ")
    new_price = float(input("Enter new price: "))
    cursor.execute("UPDATE rc_cars SET brand=%s, model=%s, price=%s WHERE id=%s", (new_brand, new_model, new_price, car_id))
    conn.commit()
    print("Record updated successfully.\n")
# delete record
def delete_record():
    view_records()
    car_id = int(input("Enter the ID of the car to delete: "))
    cursor.execute("DELETE FROM rc_cars WHERE id=%s", (car_id,))
    conn.commit()
    print("Record deleted successfully.\n")
    print("Current Records after deletion:")
    view_records()
# exit program
def quit_program():
    print("Exiting program.")
    cursor.close()
    conn.close()
    exit()
# get table data for gui
def get_table_data():
    cursor.execute("SELECT * FROM rc_cars")
    table = cursor.fetchall()
    return table
# enter loop for user to select options until they choose to exit
# This block only runs if you execute main.py directly
if __name__ == "__main__":
    while True:
        # display menu options
        display_menu()
        choice = input("Choose and action to perform: ")
        if choice == '1':
            insert_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == 'q':
            get_table_data()  # debug call
            quit_program()
        else:
            print("Invalid option. Please try again.\n")
    # get user input
