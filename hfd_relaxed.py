import sys
import os
import pandas as pd
import hfda
from pyedflib import highlevel

def calculate_hfd_for_files(file_paths, k_max):
    hfd_values = {}
    for file_path in file_paths:
        # Check if the file exists
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue
        
        # Check if the file name ends with "_1.edf"
        if not file_path.endswith("_1.edf"):
            print(f"Skipping file: {file_path}. File name doesn't end with '_1.edf'.")
            continue

        # Load signals from the EDF file
        signals, signal_headers, header = highlevel.read_edf(file_path)

        # Calculate HFD for each signal
        for i, signal in enumerate(signals):
            D = hfda.measure(signal, k_max)

            # Store HFD value
            file_name = os.path.basename(file_path)
            if file_name not in hfd_values:
                hfd_values[file_name] = []
            hfd_values[file_name].append(D)

    return hfd_values

def main():
    # Check if file paths are provided as arguments
    if len(sys.argv) < 2:
        print("Usage: python hfd_relaxed.py <file1.edf> <file2.edf> ...")
        sys.exit(1)

    # Get file paths from command-line arguments
    file_paths = sys.argv[1:]

    # Define maximum k value
    k_max = 250

    # Calculate HFD values for the provided files
    hfd_results = calculate_hfd_for_files(file_paths, k_max)

    # Convert dictionary to DataFrame
    df = pd.DataFrame.from_dict(hfd_results, orient='index')

    # Write DataFrame to CSV
    csv_file_path = 'relaxed_hfd_values.csv'
    df.to_csv(csv_file_path)
    print(f"HFD values calculated and saved to '{csv_file_path}'.")

if __name__ == "__main__":
    main()
