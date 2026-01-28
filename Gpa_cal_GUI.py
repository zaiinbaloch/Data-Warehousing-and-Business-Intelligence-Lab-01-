import tkinter as tk
from tkinter import messagebox

def point_cal(marks):
    if marks >= 85:
        return 4
    elif marks >= 80:
        return 3.7
    elif marks > 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 60:
        return 2.3
    elif marks >= 55:
        return 2.0
    elif marks >= 50:
        return 1.7
    else:
        return 0

T_point = 0
T_crhr = 0

def add_course():
    global T_point, T_crhr
    try:
        crhr = float(entry_crhr.get())
        marks = float(entry_marks.get())

        grade_point = point_cal(marks) * crhr
        T_point += grade_point
        T_crhr += crhr

        entry_crhr.delete(0, tk.END)
        entry_marks.delete(0, tk.END)

        messagebox.showinfo("Added", "Course added successfully")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def calculate_gpa():
    if T_crhr == 0:
        messagebox.showerror("Error", "No courses added")
        return

    gpa = T_point / T_crhr
    result_label.config(text=f"GPA: {round(gpa, 2)}")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("GPA Calculator")
root.geometry("350x300")

tk.Label(root, text="Credit Hours").pack(pady=5)
entry_crhr = tk.Entry(root)
entry_crhr.pack()

tk.Label(root, text="Marks").pack(pady=5)
entry_marks = tk.Entry(root)
entry_marks.pack()

tk.Button(root, text="Add Course", bg="green", fg="pink", command=add_course).pack(pady=10)
tk.Button(root, text="Calculate GPA", bg="red", fg="white", command=calculate_gpa).pack(pady=5)

result_label = tk.Label(root, text="GPA: ")
result_label.pack(pady=15)

root.mainloop()
