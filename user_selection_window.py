import tkinter as tk
from tkinter import messagebox
from upload_window import open_upload_window

def open_selection_window():
    # Create the main application window
    app = tk.Tk()
    app.title("User Selection Window")
    
    # Set the initial size of the window
    app.geometry("400x300")

    def open_upload_window_with_user(user_type):
        app.destroy()  # Close the user selection window
        open_upload_window(user_type)

    # Create buttons for user selection
    patient_button = tk.Button(app, text="Patient (Not Implemented)", state="disabled")
    patient_button.pack(pady=10)
    academician_button = tk.Button(app, text="Academician", command=lambda: open_upload_window_with_user("Academician"))
    academician_button.pack(pady=10)

    # Start the Tkinter event loop
    app.mainloop()
