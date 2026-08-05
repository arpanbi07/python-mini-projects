import tkinter as tk
from tkinter import ttk, messagebox

import styles

# -----------------------------
# Window
# -----------------------------

root = tk.Tk()
root.title("BMI Health Tracker")
root.geometry("650x650")
root.configure(bg=styles.BACKGROUND)
root.resizable(False, False)


# -----------------------------
# Center Window
# -----------------------------

window_width = 650
window_height = 650

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# -----------------------------
# BMI Functions
# -----------------------------

def calculate_bmi():

    try:

        height = float(height_entry.get())
        weight = float(weight_entry.get())

        if height <= 0 or weight <= 0:
            raise ValueError

        bmi = weight / ((height / 100) ** 2)

        bmi = round(bmi, 1)

        bmi_value.config(text=f"{bmi}")

        if bmi < 18.5:

            category.config(
                text="Underweight",
                fg=styles.WARNING
            )

            message.config(
                text="You are below the recommended weight. Consider eating a balanced, nutritious diet."
            )

        elif bmi < 25:

            category.config(
                text="Normal Weight",
                fg=styles.SUCCESS
            )

            message.config(
                text="Great! Your BMI falls within the healthy range. Keep maintaining your lifestyle."
            )

        elif bmi < 30:

            category.config(
                text="Overweight",
                fg=styles.WARNING
            )

            message.config(
                text="Regular exercise and healthier eating habits can help improve your BMI."
            )

        else:

            category.config(
                text="Obese",
                fg=styles.DANGER
            )

            message.config(
                text="Consider consulting a healthcare professional for personalized advice."
            )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid positive numbers."
        )


def reset():

    height_entry.delete(0, tk.END)

    weight_entry.delete(0, tk.END)

    bmi_value.config(
        text="--",
        fg=styles.PRIMARY
    )

    category.config(
        text="Waiting for calculation...",
        fg=styles.SUBTEXT
    )

    message.config(
        text="Enter your height and weight above."
    )

# -----------------------------
# Header
# -----------------------------

header = tk.Frame(
    root,
    bg=styles.PRIMARY,
    height=100
)

header.pack(fill="x")

title = tk.Label(
    header,
    text="BMI Health Tracker",
    bg=styles.PRIMARY,
    fg="white",
    font=styles.TITLE_FONT
)

title.pack(pady=(18,0))

subtitle = tk.Label(
    header,
    text="Know your Body Mass Index instantly",
    bg=styles.PRIMARY,
    fg="white",
    font=styles.SUBTITLE_FONT
)

subtitle.pack()

# -----------------------------
# Main Container
# -----------------------------

container = tk.Frame(
    root,
    bg=styles.BACKGROUND
)

container.pack(fill="both", expand=True, padx=25, pady=20)

# =============================
# INPUT CARD
# =============================

input_card = tk.Frame(
    container,
    bg=styles.CARD,
    highlightbackground=styles.BORDER,
    highlightthickness=1
)

input_card.pack(fill="x", pady=(0,20))

input_title = tk.Label(
    input_card,
    text="Enter Your Details",
    bg=styles.CARD,
    fg=styles.TEXT,
    font=("Segoe UI",16,"bold")
)

input_title.grid(row=0,column=0,columnspan=2,pady=(20,15))

# Height

height_label = tk.Label(
    input_card,
    text="Height (cm)",
    bg=styles.CARD,
    fg=styles.TEXT,
    font=styles.LABEL_FONT
)

height_label.grid(row=1,column=0,padx=20,pady=10,sticky="w")

height_entry = ttk.Entry(
    input_card,
    width=30,
    font=styles.ENTRY_FONT
)

height_entry.grid(row=1,column=1,padx=20,pady=10)

# Weight

weight_label = tk.Label(
    input_card,
    text="Weight (kg)",
    bg=styles.CARD,
    fg=styles.TEXT,
    font=styles.LABEL_FONT
)

weight_label.grid(row=2,column=0,padx=20,pady=10,sticky="w")

weight_entry = ttk.Entry(
    input_card,
    width=30,
    font=styles.ENTRY_FONT
)

weight_entry.grid(row=2,column=1,padx=20,pady=10)

# Buttons

button_frame = tk.Frame(
    input_card,
    bg=styles.CARD
)

button_frame.grid(row=3,column=0,columnspan=2,pady=20)

calculate_btn = tk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate_bmi,
    bg=styles.PRIMARY,
    fg="white",
    activebackground=styles.PRIMARY_HOVER,
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2",
    font=styles.BUTTON_FONT
)

calculate_btn.grid(row=0,column=0,padx=10)

reset_btn = tk.Button(
    button_frame,
    text="Reset",
    command=reset,
    bg="#E5E7EB",
    fg=styles.TEXT,
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2",
    font=styles.BUTTON_FONT
)

reset_btn.grid(row=0,column=1,padx=10)

# =============================
# RESULT CARD
# =============================

result_card = tk.Frame(
    container,
    bg=styles.CARD,
    highlightbackground=styles.BORDER,
    highlightthickness=1
)

result_card.pack(fill="both", expand=True)

result_title = tk.Label(
    result_card,
    text="Your Result",
    bg=styles.CARD,
    fg=styles.TEXT,
    font=("Segoe UI",16,"bold")
)

result_title.pack(pady=(20,15))

bmi_value = tk.Label(
    result_card,
    text="--",
    bg=styles.CARD,
    fg=styles.PRIMARY,
    font=styles.RESULT_FONT
)

bmi_value.pack()

category = tk.Label(
    result_card,
    text="Waiting for calculation...",
    bg=styles.CARD,
    fg=styles.SUBTEXT,
    font=styles.CATEGORY_FONT
)

category.pack(pady=10)

message = tk.Label(
    result_card,
    text="Enter your height and weight above.",
    bg=styles.CARD,
    fg=styles.SUBTEXT,
    wraplength=450,
    justify="center",
    font=styles.MESSAGE_FONT
)

message.pack(padx=25,pady=20)

root.mainloop()