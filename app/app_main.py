import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import PhotoImage
from datetime import datetime, timedelta
from tkinter import font as tkfont
import app_base

# Create the main window
window = tk.Tk()
window.title("Garbage app")
window.geometry("600x600")  # Set the window size
icon = PhotoImage(file='img/top_bar2.png')
window.iconphoto(False, icon)
today = datetime.today()
title_font = tkfont.Font(family="Helvetica", size=16, weight="bold", slant="italic")


# Function to display a message when the button is clicked
def show_message():
    selected_date = calendar.get_date()  # Get the selected date from the calendar
    date_obj = datetime.strptime(selected_date, '%m/%d/%y')
    if not app_base.garbages_today(date_obj):
        messagebox.showinfo("Vežamos šiukšlės", f"{date_obj.strftime('%Y-%m-%d')} šiukšlės nevežamos")
    else:
        messagebox.showinfo("Vežamos šiukšlės",
                            f"{date_obj.strftime('%Y-%m-%d')} dieną vežamos {app_base.garbages_today(date_obj)}")


# Create a label
label = tk.Label(window, text="Kauno miesto individualių\n namų šiukšlių vežimo grafikas", font=title_font)
label.pack(pady=20)
tomorrow = today + timedelta(days=1)

if not app_base.garbages_today(tomorrow):
    garbage_sms = tk.Label(window, text=f'Rytoj ({tomorrow.year}-{tomorrow.month}-{tomorrow.day}) šiukšlės nevežamos')
else:
    garbage_sms = tk.Label(window, text=f'Rytoj ({tomorrow.year}-{tomorrow.month}-{tomorrow.day}) vežamos'
                                        f'\n {app_base.garbages_today(tomorrow)}')
garbage_sms.pack(pady=20)

# Create a Calendar widget
calendar = Calendar(window, selectmode='day', year=today.year, month=today.month, day=today.day)
calendar.pack(pady=20)

# Call the function to mark the days
app_base.mark_days(calendar)

# Create a button to show the selected date
button = tk.Button(window, text="Show Selected Date", command=show_message)
button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
