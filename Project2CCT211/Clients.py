import tkinter as tk
import pandas as pd

COLUMNS = ["Name", "Check In", "Check Out", "Date and Birth", "Phone Number", "Email", "Gender", "Room Number", "Address"]

def create_hotel_mgm_csv_reader_frame(parent):
    def read_csv():
        df = pd.read_csv("Hotel_MGM.csv", usecols=COLUMNS)
        listbox.delete(0, tk.END)
        headings = f"{COLUMNS[0]:<30} {COLUMNS[1]:<20} {COLUMNS[2]:<20} {COLUMNS[3]:<30} {COLUMNS[4]:<20} {COLUMNS[5]:<30} {COLUMNS[6]:<17} {COLUMNS[7]:<22} {COLUMNS[8]:<30}"
        listbox.insert(tk.END, headings)
        for _, row in df.iterrows():
            data = f"{row['Name']:<30} {row['Check In']:<20} {row['Check Out']:<20} {row['Date and Birth']:<30} {row['Phone Number']:<20} {row['Email']:<30} {row['Gender']:<20} {row['Room Number']:<15} {row['Address']:<30}"
            listbox.insert(tk.END, data)

    root2 = tk.Frame(parent)
    read_button = tk.Button(root2, text="Read CSV", command=read_csv, font=("Helvetica", 16))
    read_button.pack()

    listbox = tk.Listbox(root2, width=150, height=35, font=("Courier", 12))  # Set the size and font of the listbox
    listbox.pack()

    # Create a horizontal scrollbar and attach it to the listbox widget
    xscrollbar = tk.Scrollbar(root2, orient="horizontal", command=listbox.xview)
    xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    listbox.configure(xscrollcommand=xscrollbar.set)

    return root2
