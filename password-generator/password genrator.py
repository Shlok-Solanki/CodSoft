import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip  # For copying to clipboard

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Variables
        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(main_frame, text="Password Generator", font=('Helvetica', 16, 'bold')).grid(
            row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Length control
        ttk.Label(main_frame, text="Password Length:").grid(row=1, column=0, sticky=tk.W, pady=5)
        length_spin = ttk.Spinbox(main_frame, from_=4, to=50, textvariable=self.length_var, width=5)
        length_spin.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Character sets checkboxes
        ttk.Label(main_frame, text="Include:").grid(row=2, column=0, sticky=tk.W, pady=5)
        
        check_frame = ttk.Frame(main_frame)
        check_frame.grid(row=2, column=1, sticky=tk.W)
        
        ttk.Checkbutton(check_frame, text="Lowercase (a-z)", variable=self.lower_var).pack(anchor=tk.W)
        ttk.Checkbutton(check_frame, text="Uppercase (A-Z)", variable=self.upper_var).pack(anchor=tk.W)
        ttk.Checkbutton(check_frame, text="Digits (0-9)", variable=self.digits_var).pack(anchor=tk.W)
        ttk.Checkbutton(check_frame, text="Symbols (!@#...)", variable=self.symbols_var).pack(anchor=tk.W)
        
        # Generate button
        ttk.Button(main_frame, text="Generate Password", command=self.generate_password).grid(
            row=3, column=0, columnspan=2, pady=15)
        
        # Password display
        ttk.Label(main_frame, text="Generated Password:").grid(row=4, column=0, sticky=tk.W, pady=5)
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, font=('Courier', 12), width=25)
        password_entry.grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Copy button
        ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(
            row=5, column=0, columnspan=2, pady=10)
    
    def generate_password(self):
        # Check if at least one character set is selected
        if not (self.lower_var.get() or self.upper_var.get() or 
                self.digits_var.get() or self.symbols_var.get()):
            messagebox.showerror("Error", "Please select at least one character set")
            return
        
        # Define character sets based on selections
        chars = []
        if self.lower_var.get():
            chars.extend(string.ascii_lowercase)
        if self.upper_var.get():
            chars.extend(string.ascii_uppercase)
        if self.digits_var.get():
            chars.extend(string.digits)
        if self.symbols_var.get():
            chars.extend(string.punctuation)
        
        # Generate password
        password = []
        length = self.length_var.get()
        
        # Ensure at least one character from each selected set
        if self.lower_var.get():
            password.append(random.choice(string.ascii_lowercase))
        if self.upper_var.get():
            password.append(random.choice(string.ascii_uppercase))
        if self.digits_var.get():
            password.append(random.choice(string.digits))
        if self.symbols_var.get():
            password.append(random.choice(string.punctuation))
        
        # Fill the rest with random characters
        for _ in range(length - len(password)):
            password.append(random.choice(chars))
        
        # Shuffle and set the password
        random.shuffle(password)
        self.password_var.set(''.join(password))
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated yet")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
