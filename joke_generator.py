import requests
import tkinter as tk
from tkinter import ttk

# Function to get joke from JokeAPI
def get_joke(category="Any"):
    url = f"https://v2.jokeapi.dev/joke/{category}?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

    try:
        response = requests.get(url)
        data = response.json()

        if data["type"] == "single":
            return data["joke"]
        else:
            return f"{data['setup']}\n\n{data['delivery']}"

    except Exception as e:
        return f"Error fetching joke: {e}"

# Function to update joke text
def display_joke():
    category = category_var.get()
    joke = get_joke(category)
    joke_text.delete("1.0", tk.END)
    joke_text.insert(tk.END, joke)

# GUI window
app = tk.Tk()
app.title("Joke Generator App")
app.geometry("600x400")
app.configure(bg="#f0f0f0")

# Title
tk.Label(app, text="😂 Joke Generator 😂", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)

# Dropdown
category_var = tk.StringVar(value="Any")
categories = ["Any", "Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"]
ttk.Combobox(app, textvariable=category_var, values=categories, state="readonly", width=30).pack(pady=5)

# Button
tk.Button(app, text="Get Joke", command=display_joke, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

# Joke output box
joke_text = tk.Text(app, height=10, width=65, wrap="word", font=("Arial", 12))
joke_text.pack(padx=10, pady=10)

# Start GUI
app.mainloop()
