import tkinter as tk
from tkinter import ttk
from upload_window import open_upload_window

def open_selection_window():
    def open_upload_window_with_user(user_type):
        app.withdraw()  # Hide the current window
        open_upload_window(user_type, app)  # Pass the reference to the current window

    def exit_app():
        app.destroy()

    app = tk.Tk()
    app.title("User Selection Window")
    app.geometry("400x300")

    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12))

    back_frame = ttk.Frame(app)
    back_frame.pack(anchor='nw', padx=10, pady=10)
    exit_button = ttk.Button(back_frame, text="Exit", command=exit_app)
    exit_button.pack(side='left')

   # Create buttons for user selection
    patient_button = ttk.Button(app, text="Patient (Not Implemented)", state="disabled")
    patient_button.pack(pady=10)
   
    academician_button = ttk.Button(app, text="Academician", command=lambda: open_upload_window_with_user("Academician"))
    academician_button.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    open_selection_window()
