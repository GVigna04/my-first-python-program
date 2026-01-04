import tkinter as tk
import random

# --------------------
# Score
# --------------------
score = 0

# --------------------
# Functions
# --------------------
def new_question():
    """Create a new random math question."""
    global num1, num2, operation, correct_answer
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(["+", "-", "*", "/"])
    
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    elif operation == "*":
        correct_answer = num1 * num2
    else:
        num2 = random.randint(1, 10)  # avoid dividing by zero
        correct_answer = round(num1 / num2, 2)
    
    question_label.config(text=f"What is {num1} {operation} {num2}?")
    result_label.config(text="")
    answer_entry.delete(0, tk.END)

def check_answer():
    """Check the user's answer and update score."""
    global score
    try:
        user_ans = float(answer_entry.get())
        if round(user_ans, 2) == correct_answer:
            result_label.config(text="✅ Correct!")
            score += 1
        else:
            result_label.config(text=f"❌ Wrong! The answer was {correct_answer}")
    except ValueError:
        result_label.config(text="❌ Enter a valid number!")
    
    score_label.config(text=f"Score: {score}")
    new_question()

# --------------------
# GUI Setup
# --------------------
root = tk.Tk()
root.title("Math Quiz Game")
root.geometry("400x250")

# Question Label
question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=10)

# Answer Entry
answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack()

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=check_answer)
submit_btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Score Label
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
score_label.pack(pady=5)

# Quit Button
quit_btn = tk.Button(root, text="Quit", command=root.destroy)
quit_btn.pack(pady=5)

# Start first question
new_question()

# Run the GUI loop
root.mainloop()
