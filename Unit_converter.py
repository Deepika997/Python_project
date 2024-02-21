#!/usr/bin/env python
# coding: utf-8
import tkinter as tk

def cm_to_feet():
    try:
        cm = float(cm_entry.get())
        feet = cm / 30.48
        result_label.config(text=f"{feet:.2f} feet")
    except ValueError:
        result_label.config(text="Invalid input")

def feet_to_inches():
    try:
        feet = float(feet_entry.get())
        inches = feet * 12
        result_label.config(text=f"{inches:.2f} inches")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_sqm():
    try:
        sqft = float(sqft_entry.get())
        sqm = sqft / 10.764
        result_label.config(text=f"{sqm:.2f} square meters")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_hectare_acres():
    try:
        sqft = float(sqft_to_ha_entry.get())
        hectares = sqft / 107639.104
        acres = sqft / 43560
        result_label.config(text=f"{hectares:.2f} hectares\n{acres:.2f} acres")
    except ValueError:
        result_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Unit Conversion")

# Labels and entry widgets
tk.Label(root, text="Centimeter to Feet:").grid(row=0, column=0, padx=5, pady=5)
cm_entry = tk.Entry(root)
cm_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=cm_to_feet).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Feet to Inches:").grid(row=1, column=0, padx=5, pady=5)
feet_entry = tk.Entry(root)
feet_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=feet_to_inches).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Sqft to Sqm:").grid(row=2, column=0, padx=5, pady=5)
sqft_entry = tk.Entry(root)
sqft_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=sqft_to_sqm).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="Sqft to Hectare/Acres:").grid(row=3, column=0, padx=5, pady=5)
sqft_to_ha_entry = tk.Entry(root)
sqft_to_ha_entry.grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=sqft_to_hectare_acres).grid(row=3, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=3, padx=5, pady=5)

root.mainloop()
