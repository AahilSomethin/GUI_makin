import tkinter as tk
from tkinter import ttk

class MovieListingsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Movie Listings")

        # Add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add a canvas widget
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                                yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.update_idletasks()

        # Configure the scrollbar
        self.scrollbar.config(command=self.canvas.yview)
        self.scrollbar.pack_forget()

        # Create the widgets for each movie listing
        for movie in movies:
            movie_frame = MovieListingFrame(self.canvas, movie)
            self.canvas.create_window(0, movie_frame.winfo_reqheight(), window=movie_frame, anchor=tk.NW)
            self.canvas.update_idletasks()

        # Display the listings
        self.show_frame(0)

    def show_frame(self, page_num):
        for i in range(len(movies)):
            if i == page_num:
                self.canvas.itemconfig(i, state=tk.NORMAL)
            else:
                self.canvas.itemconfig(i, state=tk.HIDDEN)

    def on_scroll(self, *args):
        self.canvas.yview(*args)

class MovieListingFrame(tk.Frame):
    def __init__(self, parent, movie):
        super().__init__(parent)

        # Load the movie image
        self.image = tk.PhotoImage(file=f"{movie['image']}")

        # Create and configure the widgets
        self.title_label = ttk.Label(self, text=movie["title"], font=("Helvetica", 14, "bold"))
        self.title_label.pack(pady=5)

        self.image_label = ttk.Label(self, image=self.image)
        self.image_label.image = self.image
        self.image_label.pack(pady=5)

        self.rating_label = ttk.Label(self, text=f"IMDb Rating: {movie['rating']}", font=("Helvetica", 12))
        self.rating_label.pack(pady=2)

        self.genre_label = ttk.Label(self, text=f"Genre: {movie['genre']}", font=("Helvetica", 12))
        self.genre_label.pack(pady=2)

        self.year_label = ttk.Label(self, text=f"Year: {movie['year']}", font=("Helvetica", 12))
        self.year_label.pack(pady=2)

        self.duration_label = ttk.Label(self, text=f"Duration: {movie['duration']}", font=("Helvetica", 12))
        self.duration_label.pack(pady=2)

        # Bind the mousewheel event to scroll
        self.bind_all("<MouseWheel>", parent.on_scroll)

    if __name__ == "__main__":
        app = MovieListingsApp()
        app.mainloop()