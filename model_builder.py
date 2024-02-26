# model_builder.py
import sys
import os
import subprocess
import pandas as pd
import hfda

def calculate_hfd_for_files(file_paths, k_max):
    # Function to calculate HFD for given files
    pass  # Implement HFD calculation logic here

def main():
    # Check if file paths are provided as arguments
    if len(sys.argv) < 2:
        print("Usage: python model_builder.py <file1.edf> <file2.edf> ...")
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
    csv_file_path = 'model_results.csv'
    df.to_csv(csv_file_path, index=False)
    print(f"Model results saved to '{csv_file_path}'.")

if __name__ == "__main__":
    main()
