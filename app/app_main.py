import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import app_base

# Create the main window
window = tk.Tk()
window.title("My Windows App")
window.geometry("600x400")  # Set the window size


# Function to display a message when the button is clicked
def show_message():
    selected_date = calendar.get_date()  # Get the selected date from the calendar
    messagebox.showinfo("Selected Date", f"Selected date: {selected_date}")


# Create a label
label = tk.Label(window, text="Garbage and Recycling Dates")
label.pack(pady=20)

# Create a Calendar widget
today = datetime.today()
calendar = Calendar(window, selectmode='day', year=today.year, month=today.month, day=today.day)
calendar.pack(pady=20)


# Call the function to mark the days
app_base.mark_days(calendar)


# Create a button to show the selected date
button = tk.Button(window, text="Show Selected Date", command=show_message)
button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
