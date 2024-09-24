import random
import string
import pyperclip

def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generates a random password based on user criteria."""
    char_set = ""
    
    if use_upper:
        char_set += string.ascii_uppercase
    if use_lower:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    
    if not char_set:
        raise ValueError("No character set selected. Please select at least one character type.")
    
    # Random password generation
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password

def copy_to_clipboard(password):
    """Copies the generated password to the clipboard."""
    pyperclip.copy(password)
    print("Password copied to clipboard!")





# def cli_interface():
    # print("Welcome to the Password Generator!")
    
    # try:
    #     length = int(input("Enter password length (default is 8): ") or 8)
    #     use_upper = input("Include uppercase letters? (y/n, default is y): ").lower() == 'y'
    #     use_lower = input("Include lowercase letters? (y/n, default is y): ").lower() == 'y'
    #     use_digits = input("Include digits? (y/n, default is y): ").lower() == 'y'
    #     use_symbols = input("Include symbols? (y/n, default is y): ").lower() == 'y'
        
    #     # Generate password based on user input
    #     password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        
    #     print(f"Generated Password: {password}")
        
    #     # Option to copy to clipboard
    #     copy_choice = input("Copy to clipboard? (y/n): ").lower()
    #     if copy_choice == 'y':
    #         copy_to_clipboard(password)
            
    # except ValueError as e:
    #     print(f"Error: {e}")







import tkinter as tk
from tkinter import messagebox

def generate_password_gui():
    try:
        length = int(length_var.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digit_var.get()
        use_symbols = symbol_var.get()
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_password_gui():
    password = result_var.get()
    if password:
        copy_to_clipboard(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showinfo("Failed", "Password Not Generated!")

# Create main window
root = tk.Tk()
root.title("Password Generator Tool")
root.geometry("350x400")

# Variables for storing input values
length_var = tk.StringVar(value="8")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# UI Layout
tk.Label(root, text="Password Length:").pack(pady=15)
tk.Entry(root, textvariable=length_var).pack(pady=8)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack(pady=8)
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack(pady=8)
tk.Checkbutton(root, text="Include Digits", variable=digit_var).pack(pady=8)
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack(pady=8)

tk.Button(root, text="Generate Password", command=generate_password_gui).pack(pady=20)
tk.Entry(root, textvariable=result_var, state="readonly").pack(pady=15)


# Start the GUI event loop
root.mainloop()


generate_password_gui()
copy_password_gui()


# if __name__ == "__main__":
#     cli_interface()