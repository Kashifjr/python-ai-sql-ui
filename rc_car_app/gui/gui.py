import tkinter as tk
import tkinter.ttk as tkk
from rc_car_app.backend.main import get_table_data

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

# load data into table
def load_data():
    data = get_table_data()
    for row in data:
        table.insert("", tk.END, values=row)

# Add a label
label = tk.Label(root, text="Welcome!", font=("Arial", 24))
label.pack(pady=10)
label2 = tk.Label(root, text="Current Table: NULL", font=("Arial", 14))
label2.pack(pady=20)

# Add a button
def view_button():
    global table_visible
    if not table_visible:    
        load_data()
        table.pack(fill=tk.BOTH, expand=True)
        table_visible = True
    else:
        table.pack_forget()
        table_visible = False

button = tk.Button(root, text="View Table", command=view_button)
button.pack()
button2 = tk.Button(root, text="Add Car" )
button2.pack()
button3 = tk.Button(root, text="Delete Car")
button3.pack()

def start_gui():
    # setup Tkinter window, widgets, etc.
    root.mainloop()

if __name__ == "__main__":
    start_gui()
