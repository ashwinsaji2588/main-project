import os
import pandas as pd
import numpy as np
import hfda
from pyedflib import highlevel

def calculate_hfd_for_files_in_folder(folder_path, k_max):
    hfd_values = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith("_2.edf"):  # Filter relaxed state files
            file_path = os.path.join(folder_path, file_name)
            signals, signal_headers, header = highlevel.read_edf(file_path)
            
            # Assuming you want to calculate HFD for all signals in the EDF file
            for i, signal in enumerate(signals):
                # Calculate HFD
                D = hfda.measure(signal, k_max)
                
                # Store result
                if file_name not in hfd_values:
                    hfd_values[file_name] = []
                hfd_values[file_name].append(D)
    return hfd_values

# Define folder path and maximum k value
folder_path = 'F:/Project/eeg-during-mental-arithmetic-tasks/eeg-during-mental-arithmetic-tasks/EDF/EDF/'
k_max = 250

# Calculate HFD values for relaxed state files in the folder
hfd_results = calculate_hfd_for_files_in_folder(folder_path, k_max)

# Convert dictionary to DataFrame
df = pd.DataFrame.from_dict(hfd_results, orient='index')

# Write DataFrame to Excel
excel_file_path = 'stressed_state_hfd_values.xlsx'
df.to_excel(excel_file_path)
