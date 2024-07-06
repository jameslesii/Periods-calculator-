import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_dates():
    try:
        last_period = datetime.strptime(entry_date.get(), "%Y-%m-%d")
        cycle_length = int(entry_cycle.get())

        next_period = last_period + timedelta(days=cycle_length)
        fertile_start = last_period + timedelta(days=10)
        fertile_end = last_period + timedelta(days=17)
        ovulation_day = last_period + timedelta(days=14)

        safe_days_before = last_period - timedelta(days=5)
        safe_days_after = next_period + timedelta(days=5)

        result = (f"Next Period Start Date: {next_period.strftime('%Y-%m-%d')}\n"
                  f"Fertile Window: {fertile_start.strftime('%Y-%m-%d')} to {fertile_end.strftime('%Y-%m-%d')}\n"
                  f"Most Likely Ovulation Day: {ovulation_day.strftime('%Y-%m-%d')}\n"
                  f"Safe Days: Before {fertile_start.strftime('%Y-%m-%d')} and After {fertile_end.strftime('%Y-%m-%d')}")

        messagebox.showinfo("Calculation Result", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Period Calculator")

# Create and place the input fields and labels
tk.Label(root, text="First Day of Last Period (YYYY-MM-DD):").grid(row=0)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1)

tk.Label(root, text="Average Cycle Length (days):").grid(row=1)
entry_cycle = tk.Entry(root)
entry_cycle.grid(row=1, column=1)

# Create and place the calculate button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_dates)
btn_calculate.grid(row=2, columnspan=2)

# Start the main loop
root.mainloop()
