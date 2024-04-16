import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def generate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
           messagebox.showinfo(title='BMI', message=' You are Underweight')
        elif bmi >= 18.5 and bmi < 25:
            messagebox.showinfo(title='BMI', message='You are Normal')
        elif bmi >= 25 and bmi < 30:
            messagebox.showinfo(title='BMI', message='You are Overweight')
        elif bmi > 30:
            messagebox.showinfo(title='BMI', message='You are Obese')

    except ValueError:
             result_label.config(text="Invalid input. You are required to enter a number.")

root = tk.Tk()
root.title("Body mass index")

height_label = ttk.Label(root, text="Height (m):")
height_label.grid(row=0, column=0)

height_entry = ttk.Entry(root)
height_entry.grid(row=0, column=1)

weight_label = ttk.Label(root, text="Weight (kg):")
weight_label.grid(row=1, column=0)

weight_entry = ttk.Entry(root)
weight_entry.grid(row=1, column=1)

calculate_button = ttk.Button(root, text="Submit", command=generate_bmi)
calculate_button.grid(row=2, column=1)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=1)

root.mainloop()