import tkinter as tk
from upload_window import open_upload_window

def open_selection_window():
    # Create the selection window
    selection_window = tk.Tk()
    selection_window.title("User Type Selection")
    
    # Set the initial size of the window
    selection_window.geometry("300x300")

    # Function to open the upload window for academician
    def open_academician_window():
        selection_window.destroy()
        open_upload_window()

    # Define a custom font for the buttons
    button_font = ("Helvetica", 14)

    # Button for normal user
    normal_user_button = tk.Button(selection_window, text="Normal User", command=open_upload_window, font=button_font)
    normal_user_button.pack(pady=10)

    # Button for academician
    academician_button = tk.Button(selection_window, text="Academician", command=open_academician_window, font=button_font)
    academician_button.pack(pady=10)

    # Start the Tkinter event loop for the selection window
    selection_window.mainloop()
