import tkinter as tk
from tkinter import messagebox

# ---------------- Grade Point Function ---------------- #
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

# ---------------- Global Variables ---------------- #
entries = []  # To store (credit_hours_entry, marks_entry) for each course

# ---------------- Functions ---------------- #

def create_course_entries():
    """Create entry fields for all courses after user enters number of courses"""
    global entries
    try:
        num = int(num_courses_entry.get())
        if num <= 0:
            messagebox.showerror("Error", "Enter a positive number of courses")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    # Remove previous widgets if any
    for widget in course_frame.winfo_children():
        widget.destroy()
    entries = []

    # Create labels and entries for each course
    for i in range(num):
        tk.Label(course_frame, text=f"Course {i+1}").grid(row=i, column=0, padx=5, pady=5)
        crhr_entry = tk.Entry(course_frame, width=10)
        crhr_entry.grid(row=i, column=1, padx=5, pady=5)
        marks_entry = tk.Entry(course_frame, width=10)
        marks_entry.grid(row=i, column=2, padx=5, pady=5)
        entries.append((crhr_entry, marks_entry))

    calculate_button.pack(pady=10)

def calculate_gpa():
    T_point = 0
    T_crhr = 0
    try:
        for crhr_entry, marks_entry in entries:
            crhr = float(crhr_entry.get())
            marks = float(marks_entry.get())
            T_point += point_cal(marks) * crhr
            T_crhr += crhr

        if T_crhr == 0:
            messagebox.showerror("Error", "Total credit hours cannot be zero")
            return

        gpa = T_point / T_crhr
        result_label.config(text=f"GPA: {round(gpa, 2)}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields")

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("GPA Calculator")
root.geometry("400x400")

# Step 1: Ask number of courses
tk.Label(root, text="Enter number of courses:").pack(pady=5)
num_courses_entry = tk.Entry(root)
num_courses_entry.pack(pady=5)

tk.Button(root, text="Submit", command=create_course_entries).pack(pady=10)

# Step 2: Frame to hold dynamic course entries
course_frame = tk.Frame(root)
course_frame.pack()

# Step 3: Calculate GPA button
calculate_button = tk.Button(root, text="Calculate GPA", bg="red", fg="white", command=calculate_gpa)

# Step 4: Result label
result_label = tk.Label(root, text="GPA: ")
result_label.pack(pady=15)

root.mainloop()
