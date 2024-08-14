import tkinter as tk
import webbrowser
from tkinter import messagebox

# Function to open LinkedIn
def open_linkedin(event=None):
    url = 'https://www.linkedin.com/in/deeksha-s-n'
    open_url(url)

# Function to open GitHub
def open_github(event=None):
    url = 'https://github.com/Deekshasnrev'
    open_url(url)

# Helper function to open URLs
def open_url(url):
    if not url.startswith('http'):
        url = 'https://' + url
    try:
        webbrowser.open_new_tab(url)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open URL: {e}")

# Function to create the main window
def create_window():
    window = tk.Tk()
    window.geometry("300x200")
    window.title("Social Media Bookmark App")

    label = tk.Label(window, text="My Social Media")
    label.grid(column=0, row=0, padx=10, pady=10)

    button_linkedin = tk.Button(window, text="LinkedIn", bg="orange")
    button_linkedin.grid(column=1, row=1, padx=10, pady=10)
    button_github = tk.Button(window, text="GitHub", bg="pink")
    button_github.grid(column=2, row=1, padx=10, pady=10)

    # Binding buttons to their respective functions
    button_linkedin.bind("<Button-1>", open_linkedin)
    button_github.bind("<Button-1>", open_github)

    window.mainloop()

# Run the application
if __name__ == "__main__":
    create_window()
