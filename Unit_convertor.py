import tkinter as tk
from tkinter import ttk
def convert_length():
    value = float(entry_value.get())
    conv_type = optiontype.get()
    if conv_type == "Centimeter to Meter":
        result_label.config(text="{} cm is equal to {} m.".format(value, value / 100))
    elif conv_type == "Meter to Centimeter":
        result_label.config(text="{} m is equal to {} cm.".format(value, value * 100))
    elif conv_type == "Centimeter to Feet":
        result_label.config(text="{} cm is equal to {} feet.".format(value, value / 30.48))
    elif conv_type == "Feet to Inches":
        result_label.config(text="{} feet is equal to {} inches.".format(value, value * 12))
    elif conv_type == "Mile to Kilometre":
        result_label.config(text="{} mile is equal to {} KM".format(value, value * 1.609))
    elif conv_type == "Sqft to Sqmtrs":
        result_label.config(text="{} sqft is equal to {} sqmtrs".format(value,value * 0.0929))
    elif conv_type == "Sqft to Acres/Hectres":
        result_label.config(text="{} sqft is equal to {} acres and {} sqft is equal to {} hectre".format(value, value / 43560,value,value/107639.104))
        
root = tk.Tk()
root.title("Unit Converter")
label_type = ttk.Label(root, text="Conversion Type:")
label_type.grid(row=0,column=0)
types = ["Centimeter to Meter", "Meter to Centimeter","Centimeter to Feet","Feet to Inches","Mile to Kilometre","Sqft to Sqmtrs","Sqft to Acres/Hectres"]
optiontype = ttk.Combobox(root, values=types)
optiontype.grid(row=0,column=1)

# For entering the value
label_value = ttk.Label(root, text="Enter Value:")
label_value.grid(row=2,column=0,padx=10,pady=10)

entry_value = ttk.Entry(root)
entry_value.grid(row=2,column=1,padx=10,pady=10)

# Button
convert_button = ttk.Button(root, text="Convert", command=convert_length)
convert_button.grid(row=3,padx=10,pady=10)

# Result
result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=4,padx=10,pady=10)
    

root.mainloop()
