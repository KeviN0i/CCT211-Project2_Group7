from tkinter import *
import tkinter as tk
import sys, math
from tkinter import ttk
import csv
import tkinter.messagebox as messagebox 
import pandas as pd
from Clients import create_hotel_mgm_csv_reader_frame
def Main_page():
    # Log out/ Quit Button with corresponding Messagebox
    def confirm_logout():
        answer = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
        if answer:
            root.destroy()
            sys.exit()  # MUST QUIT OUT THROUGH LOG OUT BUTTON OR ELSE LOOP

    def display_info(data):
        messagebox.showinfo("User Information",
                            f"Name: {data[0]}\nCheckIn: {data[1]}\nCheckOut: {data[2]}\nBirth: {data[3]}\nPhone: {data[4]}\nEmail: {data[5]}\nGender: {data[6]}\nRoom Number: {data[7]}\nAddress: {data[8]}")

    def check_data():
        CheckIn = entry_datein_left.get().strip()
        CheckOut = entry_dateout_left.get().strip()
        name = entry_name_left.get().strip()
        RoomNumber = entry_room_left.get().strip()
        PhoneNumber = entry_phone_left.get().strip()
        Email = entry_email_left.get().strip()

        with open('Hotel_MGM.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            # Showing the changes to the list if inputs
            if CheckIn:
                for row in reader:
                    if row[1] == CheckIn:
                        display_info(row)
                        return
                else:
                    messagebox.showerror("Invalid Input", "Invalid CheckIn date! Please register.")
                    return

            if CheckOut:
                for row in reader:
                    if row[2] == CheckOut:
                        display_info(row)
                        return
                else:
                    messagebox.showerror("Invalid Input", "Invalid CheckOut date! Please register.")
                    return

            if RoomNumber:
                for row in reader:
                    if row[7] == RoomNumber:
                        display_info(row)
                        return
                else:
                    messagebox.showerror("Invalid Input", "Invalid Room Number! Please register.")
                    return

            if name:
                for row in reader:
                    if row[0] == name:
                        display_info(row)
                        return
                else:
                    messagebox.showerror("Invalid Input", "Invalid Name! Please register.")
                    return

            if PhoneNumber:
                for row in reader:
                    if row[4] == PhoneNumber:
                        display_info(row)
                        return
                else:
                    messagebox.showerror("Invalid Input", "Invalid Phone Number! Please register.")
                    return

            if Email:
                for row in reader:
                    if row[5] == Email:
                        display_info(row)
                        return
                else:
                    messagebox.showerror("Invalid Input", "Invalid Email! Please register.")
                    return

     # Client info displayed as frame
    def display_client_info(client_info):

        # Create a new frame to display client info
        client_frame = tk.Frame(root, bg="white", padx=5, pady=5)
        client_frame.pack(side="top", fill="both", expand=True)

        # Add labels to display client info
        labels = [("Name", client_info[0]),
            ("Check In", client_info[1]),
            ("Check Out", client_info[2]),
            ("Date and Birth", client_info[3]),
            ("Phone Number", client_info[4]),
            ("Email", client_info[5]),
            ("Gender", client_info[6]),
            ("Room Number", client_info[7]),
            ("Address", client_info[8])]

        for label in labels:
            tk.Label(client_frame, text=label[0], font=("Arial", 16), width=15, anchor="w").pack(side="left")
            tk.Label(client_frame, text=label[1], font=("Arial", 16), width=30, anchor="w").pack(side="left")

    # Add horizontal scrollbar to the client frame
        client_scrollbar = tk.Scrollbar(client_frame, orient="horizontal")
        client_scrollbar.pack(side="bottom", fill="x")

    # Link the scrollbar to the client frame
        client_frame.config(xscrollcommand=client_scrollbar.set)
        client_scrollbar.config(command=client_frame.xview)

    # Show the new frame
        frame_right.pack(side="right", fill="both", expand=True)
                
    # show registration page
    def show_frame2():
        frame_right2.pack_forget()
        hotel_frame.pack_forget()
        frame_right.pack()

    # show client_list page
    def show_frame3 ():
        frame_right2.pack_forget()
        frame_right.pack_forget()
        hotel_frame.pack()
        pass


    def add_data():
        CheckIn = entry_checkin.get().strip()
        CheckOut = entry_checkout.get().strip()
        name = entry_name.get().strip()
        RoomNumber = entry_room.get().strip()
        PhoneNumber = entry_phone.get().strip()
        Email = entry_email.get().strip()
        gender = entry_gender.get().strip()
        address = entry_address.get().strip()
        birth = entry_birth.get().strip()

        if not CheckIn or not CheckOut or not name or not RoomNumber or not PhoneNumber or not Email or not gender or not address or not birth:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
        
        with open('Hotel_MGM.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, CheckIn, CheckOut, birth, PhoneNumber, Email, gender, RoomNumber, address])
            
        messagebox.showinfo("Success", "Data has been added to the CSV file.")
        
        entry_checkin.delete(0, END)
        entry_checkout.delete(0, END)
        entry_name.delete(0, END)
        entry_room.delete(0, END)
        entry_phone.delete(0, END)
        entry_email.delete(0, END)
        entry_birth.delete(0, END)
        entry_address.delete(0, END)
        entry_gender.delete(0, END)

    # Basic root
    root = tk.Tk()
    root.geometry("1400x900")
    root.title("Hotel booking management system")
    # Make the title visible to user
    title_label = tk.Label(root, text="Hotel booking management system", font=("Arial", 36))
    title_label.pack(pady=20)

    # Top frame 
    frame_top = tk.Frame(root, bd=5, relief="groove")
    frame_top.pack(side="top", fill="both")

    Client_List_img = PhotoImage(file="CL.png")
    Registration_img = PhotoImage(file="RE.png")
    Logout_img = PhotoImage(file="LO.png")


    # Create buttons
    button_client_list = tk.Button(frame_top, image=Client_List_img, font=("Arial", 14))
    button_registration = tk.Button(frame_top, image=Registration_img, text="registration", font=("Arial", 14))
    button_logout = tk.Button(frame_top, image=Logout_img, font=("Arial", 14))
    button_client_list.bind("<Button-1>", lambda event: show_frame3())
    button_registration.bind("<Button-1>", lambda event: show_frame2())
    button_logout.bind("<Button-1>", lambda event: confirm_logout())



    # Add buttons to Top frame
    button_client_list.grid(row=0, column=0, padx=20, pady=10)
    button_registration.grid(row=0, column=1, padx=20, pady=10)
    button_logout.grid(row=0, column=2, padx=20, pady=10)

    client_lists = tk.Label(frame_top, text = "Clients", font=("Arial", 10))
    client_lists.grid(row=0, column=0, sticky="s")

    registration = tk.Label(frame_top, text = "registration", font=("Arial", 10))
    registration.grid(row=0, column=1, sticky="s")

    logout = tk.Label(frame_top, text = "Log Out", font=("Arial", 10))
    logout.grid(row=0, column=2, sticky="s")



    frame_left= tk.Frame(root, bd=5, relief="groove")
    frame_left.pack(side="left", fill="both")

    #left frame topic
    label_left = tk.Label(frame_left, text = "Filter", font=("Arial", 20))
    label_left.pack(padx=10, pady=20)


    #data and birth input box
    label_datein_left = tk.Label(frame_left, text="Check-in Date:")
    label_datein_left.pack()

    entry_datein_left = tk.Entry(frame_left)
    entry_datein_left.pack(padx=10, pady=(5,10))


    #data and birth input box
    label_dateout_left = tk.Label(frame_left, text="Check-out Date:")
    label_dateout_left.pack()

    entry_dateout_left = tk.Entry(frame_left)
    entry_dateout_left.pack(padx=10, pady=(5,10))

    #room number input box
    label_room_left = tk.Label(frame_left, text="ROOM NUMBER:")
    label_room_left.pack()

    entry_room_left = tk.Entry(frame_left)
    entry_room_left.pack(padx=10, pady=(5,10))


    #name input box
    label_name_left = tk.Label(frame_left, text="NAME:")
    label_name_left.pack()

    entry_name_left = tk.Entry(frame_left)
    entry_name_left.pack(padx=10, pady=(5,10))


    #phone number input box
    label_phone_left = tk.Label(frame_left, text="PHONE NUMBER:")
    label_phone_left.pack()

    entry_phone_left = tk.Entry(frame_left)
    entry_phone_left.pack(padx=10, pady=(5,10))

    #email input box
    label_email_left = tk.Label(frame_left, text="EMAIL:")
    label_email_left.pack()

    entry_email_left = tk.Entry(frame_left)
    entry_email_left.pack(padx=10, pady=(5,10))

    #search button at the end
    button = tk.Button(frame_left, text="Filter", command=check_data)
    button.pack()


    # Registration page
    frame_right = tk.Frame(root, bd=5, relief="groove")
    frame_right.pack(side="right", expand=True, fill="both")

    label_right = tk.Label(frame_right, text="Registration", font=("Arial", 36))
    label_right.grid(row=0, column=2, columnspan=2, pady=20)


    # Registration page
    frame_right2 = tk.Frame(root, bd=5, relief="groove")
    frame_right2.pack(side="right", expand=True, fill="both")

    label_right2 = tk.Label(frame_right, text="Registration", font=("Arial", 36))
    label_right2.grid(row=0, column=2, columnspan=2, pady=20)


    # CSV file list frame
    hotel_frame = create_hotel_mgm_csv_reader_frame(root)
    hotel_frame.pack(side="right", expand=True, fill="both")

    # Personal Information
    label1 = tk.Label(frame_right, text="Personal Information", font=("Arial", 25))
    label1.grid(row=1, column=2, columnspan=2, pady=20)

    # Name
    label_name = tk.Label(frame_right, text="Name:", font=("Arial", 14))
    label_name.grid(row=2, column=0, sticky="w", padx=(70, 0), pady=20)

    entry_name = tk.Entry(frame_right, font=("Arial", 14))
    entry_name.grid(row=2, column=1, padx=10, pady=20)

    # DOB
    label_birth = tk.Label(frame_right, text="Date of Birth:", font=("Arial", 14))
    label_birth.grid(row=2, column=2, sticky="w", padx=10, pady=20)

    entry_birth = tk.Entry(frame_right, font=("Arial", 14))
    entry_birth.grid(row=2, column=3, padx=10, pady=20)

    # GENDER
    label_gender = tk.Label(frame_right, text="Gender:", font=("Arial", 14))
    label_gender.grid(row=2, column=4, sticky="w", padx=10, pady=20)

    entry_gender = tk.Entry(frame_right, font=("Arial", 14))
    entry_gender.grid(row=2, column=5, padx=10, pady=20)

    # CONTACT INFORMTION
    label2= tk.Label(frame_right, text="Contact Information", font=("Arial", 25))
    label2.grid(row=3, column=2, columnspan=2, pady=20)
    label2.config(anchor='center')
    # Phone Label
    label_phone = tk.Label(frame_right, text="Phone Number:", font=("Arial", 14))
    label_phone.grid(row=4, column=0, sticky="w", padx=(70, 0), pady=20)
    # Phone Label
    entry_phone = tk.Entry(frame_right, font=("Arial", 14))
    entry_phone.grid(row=4, column=1, padx=10, pady=20)
    # Address Label
    label_address = tk.Label(frame_right, text="Address:", font=("Arial", 14))
    label_address.grid(row=4, column=2, sticky="w", padx=10, pady=20)
    # Address Entry Label
    entry_address = tk.Entry(frame_right, font=("Arial", 14))
    entry_address.grid(row=4, column=3, padx=10, pady=20)
    # Email Label
    label_email = tk.Label(frame_right, text="Email:", font=("Arial", 14))
    label_email.grid(row=4, column=4, sticky="w", padx=10, pady=20)
    # Email Entry 
    entry_email = tk.Entry(frame_right, font=("Arial", 14))
    entry_email.grid(row=4, column=5, padx=10, pady=20)

    # Hotel Information
    label3 = tk.Label(frame_right, text="Hotel Information", font=("Arial", 25))
    label3.grid(row=5, column=2, columnspan=2, pady=10)
    label3.config(anchor='center')

    label_room = tk.Label(frame_right, text="Room Number", font=("Arial", 14))
    label_room.grid(row=6, column=0, sticky="w", padx=(70, 0), pady=20)

    entry_room = tk.Entry(frame_right, font=("Arial", 14))
    entry_room.grid(row=6, column=1, padx=10, pady=20)

    label_checkin = tk.Label(frame_right, text="Check-in Date", font=("Arial", 14))
    label_checkin.grid(row=6, column=2, sticky="w", padx=10, pady=20)

    entry_checkin = tk.Entry(frame_right, font=("Arial", 14))
    entry_checkin.grid(row=6, column=3, padx=10, pady=20)

    label_checkout = tk.Label(frame_right, text="Check-out Date", font=("Arial", 14))
    label_checkout.grid(row=6, column=4, sticky="w", padx=10, pady=20)

    entry_checkout = tk.Entry(frame_right, font=("Arial", 14))
    entry_checkout.grid(row=6, column=5, padx=10, pady=20)


    # Search button at the end
    button = tk.Button(frame_right, text="Book for this client", font=("Arial", 14), command=add_data)
    button.grid(row=10, column=2, columnspan=2, padx=20, pady=20)

    hotel_frame.pack_forget()
    root.mainloop()
