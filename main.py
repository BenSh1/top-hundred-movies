import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox

# URL to scrape
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

def fetch_movies():
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        movie_title_elements = soup.find_all('h3', class_='title')
        movie_titles = [movie.getText() for movie in movie_title_elements][::-1]
        return movie_titles
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch movie list.\n\n{e}")
        return []

def save_movies():
    try:
        with open("movies.txt", "w", encoding="utf-8") as file:
            for movie in movies:
                file.write(f"{movie}\n")
        messagebox.showinfo("Success", "Movies saved to movies.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file.\n\n{e}")

if __name__ == "__main__":

    # Fetch movie list
    movies = fetch_movies()

    # GUI Setup
    root = tk.Tk()
    root.title("Top 100 Greatest Movies")
    root.geometry("500x600")
    root.configure(padx=20, pady=20)

    # Title Label
    title_label = tk.Label(root, text="Top 100 Movies of All Time", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=(0, 10))

    # Scrollable list of movies
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
    for movie in movies:
        listbox.insert(tk.END, movie)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=listbox.yview)

    # Save Button
    save_button = ttk.Button(root, text="Save to File", command=save_movies)
    save_button.pack(pady=10)

    root.mainloop()




