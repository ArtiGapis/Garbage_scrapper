import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("My Windows App")
window.geometry("300x200")  # Set the window size

# Function to display a message when the button is clicked
def show_message():
    messagebox.showinfo("Message", "Hello, welcome to my Windows App!")

# Create a label
label = tk.Label(window, text="Click the button below")
label.pack(pady=20)

# Create a button that will call the show_message function when clicked
button = tk.Button(window, text="Click Me", command=show_message)
button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
