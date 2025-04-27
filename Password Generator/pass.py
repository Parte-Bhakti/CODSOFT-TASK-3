import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import qrcode
from PIL import Image, ImageTk

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x500")
        self.root.configure(bg="#E8F0FE")  # Light blue background

        # Main frame
        main_frame = tk.Frame(root, bg="#E8F0FE")
        main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Title
        tk.Label(main_frame, text="🔐 Password Generator", 
                 bg="#E8F0FE", fg="#2F4F4F", 
                 font=("Arial", 18, "bold")).pack(pady=10)

        # Password length
        length_frame = tk.Frame(main_frame, bg="#E8F0FE")
        length_frame.pack(pady=10)
        tk.Label(length_frame, text="Password Length:", 
                 bg="#E8F0FE", font=("Arial", 11)).pack(side=tk.LEFT)
        
        self.length_var = tk.IntVar(value=12)
        self.length_spin = ttk.Spinbox(length_frame, from_=8, to=32, 
                                       textvariable=self.length_var, width=5)
        self.length_spin.pack(side=tk.LEFT, padx=10)

        # Symbols checkbox
        options_frame = tk.Frame(main_frame, bg="#E8F0FE")
        options_frame.pack(pady=5)
        self.use_symbols = tk.BooleanVar(value=True)
        style = ttk.Style()
        style.configure("TCheckbutton", background="#E8F0FE", font=("Arial", 10))
        ttk.Checkbutton(options_frame, text="Include Symbols (!@#)", 
                        variable=self.use_symbols).pack()

        # Generate button
        generate_btn = tk.Button(main_frame, text="Generate Password", 
                                 command=self.generate,
                                 font=("Arial", 12, "bold"), bg="#90CAF9", 
                                 fg="black", activebackground="#42A5F5", 
                                 width=25)
        generate_btn.pack(pady=15)

        # Display password
        self.password_var = tk.StringVar()
        display_entry = tk.Entry(main_frame, textvariable=self.password_var, 
                                 font=("Arial", 13), width=30, justify='center', 
                                 state="readonly", bd=2, relief="sunken")
        display_entry.pack(pady=10)

        # QR Code
        self.qr_label = tk.Label(main_frame, bg="#E8F0FE")
        self.qr_label.pack(pady=10)

        # Copy to clipboard button
        copy_btn = tk.Button(main_frame, text="Copy to Clipboard", 
                             command=self.copy_to_clipboard,
                             font=("Arial", 11), bg="#A5D6A7", fg="black", 
                             activebackground="#66BB6A", width=20)
        copy_btn.pack(pady=5)

    def generate(self):
        chars = string.ascii_letters + string.digits
        if self.use_symbols.get():
            chars += "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(self.length_var.get()))
        self.password_var.set(password)
        self.generate_qr(password)

    def generate_qr(self, password):
        qr = qrcode.QRCode(version=1, box_size=4, border=4)
        qr.add_data(password)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        tk_img = ImageTk.PhotoImage(img)
        self.qr_label.config(image=tk_img)
        self.qr_label.image = tk_img

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
