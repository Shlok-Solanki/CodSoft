import tkinter as tk
from tkinter import font as tkfont
from math import sqrt, pow

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        
        # Custom font
        self.button_font = tkfont.Font(family='Helvetica', size=12, weight='bold')
        self.display_font = tkfont.Font(family='Helvetica', size=20)
        
        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.display = tk.Entry(
            root, textvariable=self.display_var, font=self.display_font,
            bd=0, insertwidth=1, width=14, borderwidth=0, justify='right',
            bg='#ffffff', fg='#333333', readonlybackground='#ffffff'
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 10), ipady=15)
        self.display.config(state='readonly')
        
        # Button layout
        buttons = [
            ('C', '⌫', '√', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('±', '0', '.', '=')
        ]
        
        # Create buttons
        for row_idx, row in enumerate(buttons, start=1):
            for col_idx, btn_text in enumerate(row):
                btn = tk.Button(
                    root, text=btn_text, font=self.button_font,
                    command=lambda t=btn_text: self.button_click(t),
                    bg=self.get_button_color(btn_text),
                    fg=self.get_text_color(btn_text),
                    activebackground=self.get_active_color(btn_text),
                    bd=0, highlightthickness=0, padx=10, pady=10
                )
                btn.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.get_hover_color(b['text'])))
                btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.get_button_color(b['text'])))
        
        # Configure grid weights
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        
        # Initialize calculator state
        self.current_value = ""
        self.operation = None
        self.previous_value = None
        self.reset_on_next_input = False
    
    def get_button_color(self, text):
        if text in {'C', '⌫'}:
            return '#ff6b6b'
        elif text in {'+', '-', '*', '/', '=', '√', '±'}:
            return '#4d96ff'
        else:
            return '#e0e0e0'
    
    def get_text_color(self, text):
        return '#ffffff' if text in {'C', '⌫', '+', '-', '*', '/', '=', '√', '±'} else '#333333'
    
    def get_hover_color(self, text):
        if text in {'C', '⌫'}:
            return '#ff8e8e'
        elif text in {'+', '-', '*', '/', '=', '√', '±'}:
            return '#6babff'
        else:
            return '#f0f0f0'
    
    def get_active_color(self, text):
        if text in {'C', '⌫'}:
            return '#ff5252'
        elif text in {'+', '-', '*', '/', '=', '√', '±'}:
            return '#3a7bd5'
        else:
            return '#d0d0d0'
    
    def button_click(self, button):
        current_display = self.display_var.get()
        
        if button.isdigit():
            if self.reset_on_next_input:
                self.current_value = ""
                self.reset_on_next_input = False
            if current_display == "0":
                self.current_value = button
            else:
                self.current_value += button
            self.display_var.set(self.current_value)
        
        elif button == '.':
            if '.' not in current_display:
                self.current_value += button
                self.display_var.set(self.current_value)
        
        elif button == '±':
            if current_display and current_display != "0":
                if current_display[0] == '-':
                    self.current_value = current_display[1:]
                else:
                    self.current_value = '-' + current_display
                self.display_var.set(self.current_value)
        
        elif button == '√':
            try:
                result = sqrt(float(current_display))
                self.display_var.set(str(result))
                self.current_value = str(result)
                self.reset_on_next_input = True
            except:
                self.display_error()
        
        elif button in {'+', '-', '*', '/'}:
            if self.previous_value is None:
                self.previous_value = current_display
            else:
                self.calculate()
            self.operation = button
            self.current_value = ""
            self.reset_on_next_input = True
        
        elif button == '=':
            if self.previous_value is not None and self.operation is not None:
                self.calculate()
                self.operation = None
                self.reset_on_next_input = True
        
        elif button == 'C':
            self.current_value = ""
            self.previous_value = None
            self.operation = None
            self.display_var.set("0")
        
        elif button == '⌫':
            if len(current_display) > 1:
                self.current_value = current_display[:-1]
                self.display_var.set(self.current_value)
            else:
                self.current_value = ""
                self.display_var.set("0")
    
    def calculate(self):
        try:
            num1 = float(self.previous_value)
            num2 = float(self.current_value)
            
            if self.operation == '+':
                result = num1 + num2
            elif self.operation == '-':
                result = num1 - num2
            elif self.operation == '*':
                result = num1 * num2
            elif self.operation == '/':
                result = num1 / num2
            
            self.display_var.set(str(result))
            self.previous_value = str(result)
            self.current_value = str(result)
        except:
            self.display_error()
    
    def display_error(self):
        self.display_var.set("Error")
        self.current_value = ""
        self.previous_value = None
        self.operation = None
        self.reset_on_next_input = True

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
