import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def generate_chart(electrodes,label, stressed_hfd_df, relaxed_hfd_df):
    # Create a new window for the chart
    chart_window = tk.Toplevel()
    chart_window.title(f"Charts for Label: {label}")

    # Set the size of the window
    chart_window.geometry("800x600")

    # Create a figure for the chart
    fig = Figure(figsize=(8, 6), dpi=100)
    # Get unique electrodes from the data
    

    for i, electrode in enumerate(electrodes):
        # Create a subplot for each electrode
        ax = fig.add_subplot(3, 1, i+1)

        # Extract HFD values for the current label and electrode from both stressed and relaxed dataframes
       # stressed_hfd_values = stressed_hfd_df[(stressed_hfd_df['Label'] == label)].iloc[:, electrode]
        #relaxed_hfd_values = relaxed_hfd_df[(relaxed_hfd_df['Label'] == label)].iloc[:, electrode]
        stressed_hfd_values = stressed_hfd_df.iloc[:, electrode]
        relaxed_hfd_values = relaxed_hfd_df.iloc[:, electrode]
        # Plot stressed state data in red
        ax.plot(stressed_hfd_values, 'r', label='Stressed State')

        # Plot relaxed state data in blue
        ax.plot(relaxed_hfd_values, 'b', label='Relaxed State')

        # Set plot title and labels
        ax.set_title(f'{label} for Electrode {electrode}')
        ax.set_xlabel('Subjects')
        ax.set_ylabel(label)

        # Add legend
        ax.legend()

    # Adjust spacing between subplots
    fig.subplots_adjust(hspace=0.5)

    # Add the figure to the chart window
    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Function to open the view results window
def open_view_results_window():
    # Create the view results window
    view_results_window = tk.Toplevel()
    view_results_window.title("View Results")

    # Set the initial size of the window
    view_results_window.geometry("800x600")

    # Add title for Higuchi Fractal Dimension
    title_label = tk.Label(view_results_window, text="Available results", font=("Arial", 14, "bold"))
    title_label.pack()

    # Read the HFD values from CSV files
    stressed_hfd_df = pd.read_csv("Features/stressed_hfd_values.csv")
    relaxed_hfd_df = pd.read_csv("Features/relaxed_hfd_values.csv")
    stressed_rtp_df = pd.read_csv("Features/stressed_theta_power.csv")
    relaxed_rtp_df = pd.read_csv("Features/relaxed_theta_power.csv")

    # Get unique labels from the data
    unique_labels = ["hfd","rp","rs","rd","ss"]
    eh=[1,3,5]
    et=[1,5,6]
    # Create buttons for each unique label
    button = tk.Button(view_results_window, text="Higuchi Fractal Dimension",
                    command=lambda l="Higuchi Fractal Dimension": generate_chart(eh,l, stressed_hfd_df, relaxed_hfd_df))
    button.pack()
    button = tk.Button(view_results_window, text="Relative theta power",
                    command=lambda l="Relative theta power": generate_chart(et,l, stressed_rtp_df, relaxed_rtp_df))
    button.pack()
    
    # Start the Tkinter event loop for the view results window
    view_results_window.mainloop()

# Call the function to open the view results window

