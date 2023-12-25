import tkinter as tk
from tkinter import filedialog
from email.mime import image
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("HC.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="The Horizon Cinemas",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Login", command=self.login)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Signup", command=self.signup)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.logout)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # create empty frame for the right sidebar
        self.right_sidebar_frame = customtkinter.CTkFrame(self)
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="What do you wish to find")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,
                                                      text_color=("gray10", "#DCE4EE"), command=self.search)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=350)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        # set default values
        self.sidebar_button_1.configure(state="enabled", text="Login")
        self.sidebar_button_2.configure(state="enabled", text="Register")
        self.sidebar_button_3.configure(state="disabled", text="Logout")
        # if self.sidebar_button_logged in state enable
        self.main_button_1.configure(state="enabled", text="Search")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.progressbar_1.configure(mode="indeterminate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "Movies\n\n" + "Shrek is awesome\n\n")
        self.seg_button_1.configure(values=["All", "New", "cartoon", "Action", "Comedy", "Drama"])
        self.seg_button_1.set("All")

    def search(self):
        # Get the search query from the entry
        search_query = self.entry.get()

        # Perform the search (you can customize this part based on your application logic)
        # For now, let's just print the search query
        print("Search Query:", search_query)

        # Update the display or perform other actions based on the search query

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def login(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "login and signup.py")])
    
        if file_path:
            with open("signup.py", 'r') as file:
                content = file.read()
                # You can do something with the content, like displaying it in a text widget
                print(content)


    def signup(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "login and signup.py")])
        
        if file_path:
            with open("signup.py", 'r') as file:
                content = file.read()
                # You can do something with the content, like displaying it in a text widget
                print(content)

    def logout(self):
        # Add your logout logic here

        # Example: Clear the entry and textbox content
        self.entry.delete(0, tk.END)
        self.textbox.delete("1.0", tk.END)

        # Example: Enable buttons that should be enabled when logged out
        self.sidebar_button_1.configure(state="enabled")
        self.sidebar_button_2.configure(state="enabled")
        self.sidebar_button_3.configure(state="disabled")

        # Example: Change the appearance mode to default (System)
        customtkinter.set_appearance_mode("System")

        # Example: Reset the UI scaling to default (100%)
        customtkinter.set_widget_scaling(1.0)

        # Example: Stop and reset the progress bar
        self.progressbar_1.stop()
        self.progressbar_1.configure(mode="indeterminate")

        # Example: Set default values for appearance mode and scaling optionmenus
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")

        print("Logout button clicked")


if __name__ == "__main__":
    app = Main()
    app.mainloop()
