import tkinter as tk
from tkinter import filedialog

def open_upload_window():
    # Create the main application window
    app = tk.Tk()
    app.title("File Upload GUI")
    
    # Set the initial size of the window
    app.geometry("400x300")

    def upload_files():
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            label.config(text="Files uploaded:\n" + "\n".join(file_paths))
        else:
            label.config(text="No files selected.")

    # Create a button to upload files with increased size
    upload_button = tk.Button(app, text="Upload Files", command=upload_files, width=20, height=2)
    upload_button.pack(pady=10)

    # Create a label to display file paths
    label = tk.Label(app, text="")
    label.pack()

    # Start the Tkinter event loop
    app.mainloop()
