import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def generate_chart(label, stressed_hfd_df, relaxed_hfd_df):
    # Create a new window for the chart
    chart_window = tk.Toplevel()
    chart_window.title(f"Charts for Label: {label}")

    # Set the size of the window
    chart_window.geometry("800x600")

    # Create a figure for the chart
    fig = Figure(figsize=(8, 6), dpi=100)
    print("we")
    # Get unique electrodes from the data
    electrodes = [1, 3, 5]

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
        ax.set_title(f'Higuchi Fractal Dimension for Electrode {electrode}')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Higuchi Fractal Dimension')

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
    title_label = tk.Label(view_results_window, text="Higuchi Fractal Dimension", font=("Arial", 14, "bold"))
    title_label.pack()

    # Read the HFD values from CSV files
    stressed_hfd_df = pd.read_csv("Features/stressed_hfd_values.csv")
    relaxed_hfd_df = pd.read_csv("Features/relaxed_hfd_values.csv")

    # Get unique labels from the data
    unique_labels = ["hfd","rp","rs","rd","ss"]

    # Create buttons for each unique label
    for label in unique_labels:
        button = tk.Button(view_results_window, text=f"Label {label}",
                           command=lambda l=label: generate_chart(l, stressed_hfd_df, relaxed_hfd_df))
        button.pack()

    # Start the Tkinter event loop for the view results window
    view_results_window.mainloop()

# Call the function to open the view results window