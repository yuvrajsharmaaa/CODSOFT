import cv2
import pytesseract
import sympy as sp
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Text, messagebox
import sys

# Image preprocessing
def preprocess_image(image_path):
    try:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        return thresh
    except Exception as e:
        messagebox.showerror("Error", f"Failed to preprocess image: {str(e)}")
        return None

# Text extraction
def extract_text(image):
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Path to Tesseract executable on Windows
        pil_image = Image.fromarray(image)
        config = '--psm 6 -c tessedit_char_whitelist=0123456789+-*/=()'
        text = pytesseract.image_to_string(pil_image, config=config)
        return text.replace(" ", "").replace("=", "")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text: {str(e)}")
        return ""

# Expression solving
def solve_expression(expression):
    try:
        expr = sp.sympify(expression)
        solution = expr.evalf()  # Evaluate the expression numerically
        return solution
    except (sp.SympifyError, TypeError):
        return "Unable to parse expression"

# Process the extracted text and solve the expressions
def process_text(text):
    lines = text.split('\n')
    solutions = []
    for line in lines:
        if line.strip():
            solutions.append((line, solve_expression(line)))
    return solutions

# GUI Functionality
def open_file():
    filepath = filedialog.askopenfilename(
        initialdir="/", title="Select Image",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*"))
    )
    if filepath:
        image = preprocess_image(filepath)
        if image is not None:
            text = extract_text(image)
            solutions = process_text(text)
            
            result_text.delete(1.0, tk.END)
            for expr, sol in solutions:
                result_text.insert(tk.END, f"Expression: {expr}\nSolution: {sol}\n\n")

# Setup GUI
app = tk.Tk()
app.title("Simple Math Solver")

canvas = tk.Canvas(app, height=500, width=600)
canvas.pack()

frame = tk.Frame(app, bg="#ffffff")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

open_file_btn = tk.Button(frame, text="Open Image", padx=10, pady=5, fg="white", bg="#263D42", command=open_file)
open_file_btn.pack()

result_text = Text(frame)
result_text.pack()

# Run the GUI in a separate thread
def run_gui():
    app.mainloop()

# Start the GUI
import threading
threading.Thread(target=run_gui).start()

# Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def calculator():
    print("Welcome to Simple Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Evaluate an expression")
    print("6. Exit")
    
    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        elif choice == '5':
            expression = input("Enter an expression: ")
            print(f"{expression} = {evaluate_expression(expression)}")
        
        elif choice == '6':
            print("Exiting the program...")
            sys.exit()
        
        else:
            print("Invalid input. Please enter a valid choice.")

# Run the calculator function in the main thread
calculator()
