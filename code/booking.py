import tkinter as tk
from tkinter import ttk
from customtkinter import CTk
from PIL import Image, ImageTk

def show_image():
    img_path = "path_to_your_image"  # Update with the correct path
    img = Image.open(img_path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

def add_padding(element, x=0, y=0):
    return tk.Frame(master=element, height=y, width=x)

def select_film(event):
    selected_film = film_combobox.get()
    print(f"Selected Film: {selected_film}")

def select_showing(event):
    selected_showing = showing_combobox.get()
    print(f"Selected Showing: {selected_showing}")

def select_ticket_type(event):
    selected_ticket_type = ticket_type_combobox.get()
    print(f"Selected Ticket Type: {selected_ticket_type}")

def select_tickets(event):
    selected_tickets = tickets_spinbox.get()
    print(f"Selected # of Tickets: {selected_tickets}")

def check_availability():
    pass

def submit_booking():
    pass

# Set up main window
root = CTk()
root.geometry("800x600")
root.title("Horizon Cinemas")

# Add elements to the window
# Frame
frame = tk.Frame(root, bg="#1f1f1f")
frame.pack(fill="both", expand=True)

# Main label
main_label = ttk.Label(frame, text="Booking", font=("Helvetica", 24))
main_label.pack(pady=20)

# Image label
image_label = ttk.Label(frame)
image_label.pack(pady=20)
show_image()

# Film dropdown
film_label = ttk.Label(frame, text="Select Film")
film_label.pack(pady=10)
film_combobox = ttk.Combobox(frame, values=["Film 1", "Film 2", "Film 3"])
film_combobox.pack(pady=10)
film_combobox.bind("<<ComboboxSelected>>", select_film)

# Showing dropdown
showing_label = ttk.Label(frame, text="Select Showing")
showing_label.pack(pady=10)
showing_combobox = ttk.Combobox(frame, values=["Showing 1", "Showing 2", "Showing 3"])
showing_combobox.pack(pady=10)
showing_combobox.bind("<<ComboboxSelected>>", select_showing)

# Ticket type dropdown
ticket_type_label = ttk.Label(frame, text="Select Ticket Type")
ticket_type_label.pack(pady=10)
ticket_type_combobox = ttk.Combobox(frame, values=["Standard", "VIP"])
ticket_type_combobox.pack(pady=10)
ticket_type_combobox.bind("<<ComboboxSelected>>", select_ticket_type)

# Number of tickets
tickets_label = ttk.Label(frame, text="Select # of tickets")
tickets_label.pack(pady=10)
tickets_spinbox = ttk.Spinbox(frame, from_=1, to=10)
tickets_spinbox.pack(pady=10)
tickets_spinbox.bind("<ButtonRelease>", select_tickets)

# Check availability and price button
check_availability_button = ttk.Button(frame, text="Check Availability and Price", command=check_availability)
check_availability_button.pack(pady=20)

# Booking receipt frame
booking_receipt_frame = tk.Frame(frame, bg="#1f1f1f")
booking_receipt_frame.pack(fill="both", expand=True)

# Submit booking button
submit_booking_button = ttk.Button(booking_receipt_frame, text="Submit Booking", command=submit_booking)
submit_booking_button.pack(pady=20)

# Add padding to the frame
frame.pack_propagate(0)
frame.pack_configure(padx=50, pady=50)

root.mainloop()
