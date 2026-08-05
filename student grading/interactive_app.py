from datetime import datetime
import tkinter as tk
from tkinter import messagebox


# ----------------------------
# Calculate Result
# ----------------------------
def calculate_result():
    name = entry_name.get().strip()
    roll = entry_roll.get().strip()

    if not name or not roll:
        messagebox.showerror("Error", "Please enter Name and Roll Number.")
        return

    try:
        marks = [
            int(entry_sub1.get()),
            int(entry_sub2.get()),
            int(entry_sub3.get()),
            int(entry_sub4.get()),
            int(entry_sub5.get())
        ]

        for mark in marks:
            if mark < 0 or mark > 100:
                messagebox.showerror("Invalid Marks", "Marks should be between 0 and 100.")
                return

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric marks.")
        return

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "PASS" if percentage >= 40 else "FAIL"

    if percentage >= 90:
        remark = "Outstanding Performance!"
    elif percentage >= 75:
        remark = "Very Good!"
    elif percentage >= 60:
        remark = "Good Work!"
    elif percentage >= 40:
        remark = "Passed Successfully."
    else:
        remark = "Needs Improvement."

    result_text.set(
        f"Student Name : {name}\n"
        f"Roll Number  : {roll}\n\n"
        f"Total Marks  : {total}/500\n"
        f"Percentage   : {percentage:.2f}%\n"
        f"Grade        : {grade}\n"
        f"Result       : {status}\n"
        f"Remark       : {remark}"
    )


# ----------------------------
# Clear Fields
# ----------------------------
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)

    for entry in [
        entry_sub1,
        entry_sub2,
        entry_sub3,
        entry_sub4,
        entry_sub5
    ]:
        entry.delete(0, tk.END)

    result_text.set("")
    entry_name.focus()

def save_result():

    if result_text.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please calculate the result first."
        )
        return

    with open("student_results.txt", "a") as file:

        file.write("=" * 40 + "\n")
        file.write(result_text.get())
        file.write("\n")
        file.write(
            f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        )
        file.write("\n")
        file.write("=" * 40 + "\n\n")

    messagebox.showinfo(
        "Saved",
        "Result saved successfully."
    )

# ----------------------------
# Main Window
# ----------------------------
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("500x750")
root.resizable(False, False)
root.configure(bg="#E8F5E9")

title = tk.Label(
    root,
    text="Student Grade Calculator",
    font=("Segoe UI", 18, "bold"),
    bg="#2E7D32",
    fg="white",
    pady=10
)

title.pack(fill="x")


frame = tk.Frame(root, bg="#E8F5E9", padx=20, pady=20)
frame.pack(fill="both", expand=True)


def add_input(label_text):
    tk.Label(
        frame,
        text=label_text,
        bg="#E8F5E9",
        font=("Segoe UI", 11)
    ).pack(anchor="w")

    entry = tk.Entry(frame, font=("Segoe UI", 11))
    entry.pack(fill="x", pady=5)

    return entry


entry_name = add_input("Student Name")
entry_roll = add_input("Roll Number")

entry_sub1 = add_input("English Marks")
entry_sub2 = add_input("Mathematics Marks")
entry_sub3 = add_input("Science Marks")
entry_sub4 = add_input("Computer Marks")
entry_sub5 = add_input("History Marks")


button_frame = tk.Frame(frame, bg="#E8F5E9")
button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="Calculate",
    bg="#43A047",
    fg="white",
    width=12,
    command=calculate_result
).pack(side="left", padx=5)


tk.Button(
    button_frame,
    text="Clear",
    bg="#FB8C00",
    fg="white",
    width=12,
    command=clear_fields
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Save",
    bg="#1976D2",
    fg="white",
    width=12,
    command=save_result
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Exit",
    bg="#E53935",
    fg="white",
    width=12,
    command=root.destroy
).pack(side="left", padx=5)


result_text = tk.StringVar()

result_label = tk.Label(
    frame,
    textvariable=result_text,
    bg="white",
    relief="solid",
    justify="left",
    anchor="nw",
    font=("Segoe UI", 11),
    padx=10,
    pady=10,
    wraplength=380
)

result_label.pack(fill="both", expand=True, pady=10)

footer = tk.Label(
    root,
    text="Built with Python & Tkinter",
    bg="#2E7D32",
    fg="white",
    font=("Segoe UI", 10)
)

footer.pack(fill="x", side="bottom")

root.mainloop()