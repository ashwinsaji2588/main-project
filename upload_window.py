import tkinter as tk
from tkinter import filedialog
import subprocess

def open_upload_window(user_type):
    # Create the main application window
    app = tk.Tk()
    app.title("File Upload GUI")
    
    # Set the initial size of the window
    app.geometry("400x400")

    def upload_files():
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            label.config(text="Files uploaded:\n" + "\n".join(file_paths))
            build_model_button.config(state="normal")  # Enable the build model button
            # Store the file paths for processing when building the model
            app.uploaded_files = file_paths
        else:
            label.config(text="No files selected.")
            build_model_button.config(state="disabled")  # Disable the build model button if no files are selected

    def build_model():
        # Update status label to indicate calculation is in progress
        status_label.config(text="Finding HFD values. Please wait...")
        
        # Call hfd_relaxed.py and hfd_stressed.py with uploaded file paths asynchronously
        for py_file in ['hfd_relaxed.py', 'hfd_stressed.py','psd_calc.py','relative.py']:
            subprocess.Popen(['python', py_file] + list(app.uploaded_files))
        status_label.config(text="Model calculation initiated!")  # Update status label
        
    # Create a button to upload files
    upload_button = tk.Button(app, text="Upload Files", command=upload_files, width=20, height=2)
    upload_button.pack(pady=10)

    # Create a label to display file paths
    label = tk.Label(app, text="")
    label.pack()

    # Create a button to build the model (initially disabled)
    build_model_button = tk.Button(app, text="Build Model", command=build_model, width=20, height=2, state="disabled")
    build_model_button.pack(pady=10)
    
    # Create a label to show status
    status_label = tk.Label(app, text="")
    status_label.pack()

    # Start the Tkinter event loop
    app.mainloop()