import tkinter as tk
import tkinter.ttk as tkk
#from rc_car_app.backend.main import view_records
from rc_car_app.backend import main

# load data into table
def load_data():
    data = main.view_records()
    for row in data:
        table.insert("", tk.END, values=row)
# clear table
def clear_table():
    for row in table.get_children():
        table.delete(row)
# Add a button
def view_button():
    global table_visible
    if not table_visible:    
        load_data()
        table.pack(fill=tk.BOTH, expand=True)
        table_visible = True
    else:
        clear_table()
        table.pack_forget()
        table_visible = False
#add car button function
def add_car_button():
    pass
# Create the main window
root = tk.Tk()
root.title("RC Car Database v0.1")   # Window title
root.geometry("700x500")             # Width x Height
# Create table (Treeview)
table_visible = False
table = tkk.Treeview(root, columns=("ID", "Brand", "Model", "Price"), show='headings')
table.heading("ID", text="ID")
table.heading("Brand", text="Brand")
table.heading("Model", text="Model")
table.heading("Price", text="Price")
# Add Headings
label = tk.Label(root, text="Welcome!", font=("Arial", 24))
label.pack(pady=10)
label2 = tk.Label(root, text="Current Table: NULL", font=("Arial", 14))
label2.pack(pady=20)
# Add buttons
button = tk.Button(root, text="View Table", command=view_button)
button.pack()
# Add car button
# commmand binding to be added later
button2 = tk.Button(root, text="Add Car" )
button2.pack()
# Delete car button
# command binding to be added later
button3 = tk.Button(root, text="Delete Car")
button3.pack()
# Start the GUI event loop
def start_gui():
    # setup Tkinter window, widgets, etc.
    root.mainloop()

if __name__ == "__main__":
    start_gui()
