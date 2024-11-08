import tkinter as tk
from tkinter import ttk
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{celsius:.2f}")
    except ValueError:
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, "Invalid Input")
def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, "Invalid Input")
root = tk.Tk()
root.title("Temperature Converter")
fahrenheit_label = ttk.Label(root, text="Fahrenheit:")
celsius_label = ttk.Label(root, text="Celsius:")
fahrenheit_entry = ttk.Entry(root, width=10)
fahrenheit_entry.insert(0, "32.0")
celsius_entry = ttk.Entry(root, width=10)
celsius_entry.insert(0, "0.0")
to_celsius_button = ttk.Button(root, text=">>>>", command=fahrenheit_to_celsius)
to_fahrenheit_button = ttk.Button(root, text="<<<<", command=celsius_to_fahrenheit)
fahrenheit_label.grid(row=0, column=0, padx=5, pady=5)
celsius_label.grid(row=0, column=1, padx=5, pady=5)
fahrenheit_entry.grid(row=1, column=0, padx=5, pady=5)
celsius_entry.grid(row=1, column=1, padx=5, pady=5)
to_celsius_button.grid(row=2, column=0, padx=5, pady=5)
to_fahrenheit_button.grid(row=2, column=1, padx=5, pady=5)
root.mainloop()
