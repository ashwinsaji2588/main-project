import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def open_view_results_window():
    # Create the view results window
    view_results_window = tk.Toplevel()
    view_results_window.title("View Results")
    
    # Set the initial size of the window
    view_results_window.geometry("800x600")
    
    # Add title for Higuchi Fractal Dimension
    title_label = tk.Label(view_results_window, text="Higuchi Fractal Dimension", font=("Arial", 14, "bold"))
    title_label.pack()
    
    # Read the HFD values from CSV files
    stressed_hfd_df = pd.read_csv("Features/stressed_hfd_values.csv")
    relaxed_hfd_df = pd.read_csv("Features/relaxed_hfd_values.csv")
    
    # Extract HFD values for electrodes 1, 3, and 5 (columns 1, 3, and 5)
    electrodes = [1, 3, 5]
    
    fig = Figure(figsize=(8, 6), dpi=100)
    
    for i, electrode in enumerate(electrodes):
        # Create a subplot for each electrode
        ax = fig.add_subplot(3, 1, i+1)
        
        # Extract HFD values for the current electrode from both stressed and relaxed dataframes
        stressed_hfd_values = stressed_hfd_df.iloc[:, electrode]
        relaxed_hfd_values = relaxed_hfd_df.iloc[:, electrode]
        
        # Plot stressed state data in red
        ax.plot(stressed_hfd_values, 'r', label='Stressed State')
        
        # Plot relaxed state data in blue
        ax.plot(relaxed_hfd_values, 'b', label='Relaxed State')
        
        # Set plot title and labels
        ax.set_title(f'Higuchi Fractal Dimension for Electrode {electrode}')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Higuchi Fractal Dimension')
        
        # Add legend
        ax.legend()
    
    # Adjust spacing between subplots
    fig.subplots_adjust(hspace=0.5)

    # Add the figure to the view results window
    canvas = FigureCanvasTkAgg(fig, master=view_results_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Start the Tkinter event loop for the view results window
    view_results_window.mainloop()

