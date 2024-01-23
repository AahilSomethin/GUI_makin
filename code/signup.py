import tkinter
import customtkinter


username = '123'
password = '123'



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x440")
app.title('Login')

def switch_to_signup():
    login_frame.place_forget()
    signup_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def switch_to_login():
    signup_frame.place_forget()
    login_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def button_function():
    # Perform login logic here
    print("Login - Username:", entry1.get(), "Password:", entry2.get())

def signup_function():
    username = entry_signup_username.get()
    password = entry_signup_password.get()
    email = entry_signup_email.get()
    
    # Perform signup logic here
    print("Signup - Username:", username, "Password:", password, "Email:", email)

# Login Frame
login_frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
login_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=login_frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=login_frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=login_frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

l3 = customtkinter.CTkLabel(master=login_frame, text="Forget password?", font=('Century Gothic', 12))
l3.place(x=155, y=195)

button1 = customtkinter.CTkButton(master=login_frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

signup_button = customtkinter.CTkButton(master=login_frame, width=220, text="Signup", command=switch_to_signup, corner_radius=6)
signup_button.place(x=50, y=290)

# Signup Frame
signup_frame = customtkinter.CTkFrame(master=app, width=320, height=390, corner_radius=15)
signup_frame.place_forget()

l2 = customtkinter.CTkLabel(master=signup_frame, text="Signup an Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry_signup_username = customtkinter.CTkEntry(master=signup_frame, width=220, placeholder_text='Username')
entry_signup_username.place(x=50, y=110)

entry_signup_password = customtkinter.CTkEntry(master=signup_frame, width=220, placeholder_text='Password', show="*")
entry_signup_password.place(x=50, y=165)

entry_signup_email = customtkinter.CTkEntry(master=signup_frame, width=220, placeholder_text='Email')
entry_signup_email.place(x=50, y=220)

signup_button = customtkinter.CTkButton(master=signup_frame, width=220, text="Signup", command=signup_function, corner_radius=6)
signup_button.place(x=50, y=260)

login_button = customtkinter.CTkButton(master=signup_frame, width=220, text="Login", command=switch_to_login, corner_radius=6)
login_button.place(x=50, y=310)

app.mainloop()
