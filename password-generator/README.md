# 🔐 Password Generator (Tkinter GUI)

A secure, customizable password generator built using **Python** and **Tkinter**. This desktop application lets users generate strong passwords based on their preferences, including length and character types, with a simple and user-friendly GUI.

---

## 🚀 Features

- ✅ Selectable password length (4 to 50 characters)
- 🔠 Option to include:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Symbols (!@#$%^&* etc.)
- 🔁 Guaranteed inclusion of at least one character from each selected type
- 📋 Copy the generated password directly to the clipboard
- 🎨 Modern and clean GUI built with `Tkinter` and `ttk`

---

## 🖥️ GUI Preview

![Password Generator Screenshot](https://via.placeholder.com/400x200?text=Password+Generator+Preview)

---

## 📦 Requirements

- Python 3.x
- Modules:
  - `tkinter` (standard with Python)
  - `random`, `string` (standard)
  - `pyperclip` *(for clipboard support)*

Install `pyperclip` if you don't have it:
```bash
pip install pyperclip
🧠 How It Works
Choose your desired password length.

Select the character sets to include.

Click "Generate Password".

View the password in the entry field.

Click "Copy to Clipboard" to use it anywhere securely.

🛡️ Security Note
Although this tool generates strong passwords using Python’s random and includes various character sets, it is intended for general use. For mission-critical or enterprise-level security, consider using cryptographically secure libraries like secrets.

📁 Project Structure
pgsql
Copy
Edit
password-generator/
├── password_generator.py
└── README.md
🙌 Acknowledgements
Built as part of the CodSoft Internship Program

Inspired by the need for strong password habits

📬 Contact
Shlok Solanki
