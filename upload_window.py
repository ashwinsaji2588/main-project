import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess

def open_upload_window(user_type, user_selection_window):
    # Create the main application window
    app = tk.Toplevel(user_selection_window)  # Use Toplevel to create a new window
    app.title("File Upload GUI")
    
    # Set the initial size of the window
    app.geometry("400x350")

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
        # Call hfd_relaxed.py and hfd_stressed.py with uploaded file paths
        for py_file in ['hfd_relaxed.py', 'hfd_stressed.py']:
            subprocess.run(['python', py_file] + list(app.uploaded_files))
        messagebox.showinfo("Model Built", "Model has been successfully built.")

    # Create a style for themed widgets
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12))

    # Function to go back
    def go_back():
        app.withdraw()  # Hide the current window
        user_selection_window.deiconify()  # Show the user selection window again

    # Create a frame for the back button
    back_frame = ttk.Frame(app)
    back_frame.pack(anchor='nw', padx=10, pady=10)

    # Create a back button with text "Back"
    back_button = ttk.Button(back_frame, text="Back", command=go_back)
    back_button.pack(side='left')

    # Create a button to upload files
    upload_button = ttk.Button(app, text="Upload Files", command=upload_files)
    upload_button.pack(pady=10)

    # Create a label to display file paths
    label = ttk.Label(app, text="")
    label.pack()

    # Create a button to build the model (initially disabled)
    build_model_button = ttk.Button(app, text="Build Model", command=build_model, state="disabled")
    build_model_button.pack(pady=10)

    # Start the Tkinter event loop
    app.mainloop()
