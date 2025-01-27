from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, ttk
from datetime import datetime, timedelta
import math

def show_loading_screen():
    loading_window = Toplevel(root)
    loading_window.title("Loading")
    
    loading_label = Label(loading_window, text="Calculating Resin...", padx=20, pady=20)
    loading_label.pack()
    
    progress_bar = ttk.Progressbar(loading_window, orient="horizontal", length=180, mode="determinate")
    progress_bar.pack(pady=20)
    progress_bar.start(8)  # Start the indeterminate progress bar

    # Call the calculate_resin function after a short delay to simulate processing time
    root.after(1500, calculate_resin, loading_window, progress_bar)

def calculate_resin(loading_window, progress_bar):
    try:
        resin_increment = int(resin_entry.get())
        target_time = time_entry.get()
        max_resin = 200

        resin_per_increment = 8
        current_time = datetime.now()
        target_hour, target_minute = map(int, target_time.split(':'))
        target_time_today = current_time.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)

        if target_time_today < current_time:
            target_time_today += timedelta(days=1)

        minutes_to_play = (target_time_today - current_time).total_seconds() / 60
        increments_needed = minutes_to_play / resin_per_increment
        total_resin = resin_increment + increments_needed
        total_resin = max(0, min(total_resin, max_resin))

        progress_bar.stop()  # Stop the progress bar
        loading_window.destroy()  # Close the loading window

        resin_result.config(text=f"You will have {math.floor(total_resin)} resin by the time you start playing.\nHappy Grinding!")

        # Calculate the time at which resin becomes 200
        time_to_max_resin = (max_resin - resin_increment) * resin_per_increment
        time_for_max_resin = current_time + timedelta(minutes=time_to_max_resin)
        resin_result_time.config(text=f"Resin reaches 200 at: {time_for_max_resin.strftime('%H:%M:%S')}")
    except ValueError:
        progress_bar.stop()  # Stop the progress bar
        loading_window.destroy()  # Close the loading window
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# GUI setup
root = Tk()
root.title("Resin Calculator")
root.geometry("400x300")

instruction_label = Label(root, text="Enter current resin and target play time (24-hour format HH:MM):", pady=10)
instruction_label.pack()

resin_label = Label(root, text="Current Resin:")
resin_label.pack()

resin_entry = Entry(root)
resin_entry.pack()

time_label = Label(root, text="Target Play Time:")
time_label.pack()

time_entry = Entry(root)
time_entry.pack()

calculate_button = Button(root, text="Calculate Resin", command=show_loading_screen, pady=10)
calculate_button.pack(pady=10)

resin_result = Label(root, text="", font=("Arial", 12, "bold"))
resin_result.pack()

resin_result_time = Label(root, text="", font=("Arial", 12, "bold"))
resin_result_time.pack()

root.mainloop()
