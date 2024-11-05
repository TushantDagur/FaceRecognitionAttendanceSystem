import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def upload_photo():
    file_path = filedialog.askopenfilename(title="Select a photo", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        photo_label.config(text=f"Selected: {file_path}")

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    # Process the data (you can add your own logic here)
    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}")

# Create the main window
root = tk.Tk()
root.title("User Information Form")

# Name Label and Entry
tk.Label(root, text="Name:").grid(row=0, column=0, padx=20, pady=20)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Email Label and Entry
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Phone Label and Entry
tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=10, pady=10)

# Address Label and Entry
tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=10)

# Photo Uploader Button
photo_button = tk.Button(root, text="Upload Photo", command=upload_photo)
photo_button.grid(row=4, column=0, padx=10, pady=10)

# Photo Label
photo_label = tk.Label(root, text="No photo selected")
photo_label.grid(row=4, column=1, padx=10, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Start the main event loop
root.mainloop()
