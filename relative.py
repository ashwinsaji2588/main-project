import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt
from scipy.signal import welch
import os
import mne
import sys


def calculate_absolute_power_theta(eeg_data_first_91000, fs=500,frame_size=500):
    """
    Calculate the absolute power of theta wave (4~8Hz) from EEG data.

    Parameters:
    - eeg_data: 1D numpy array, EEG data for a single channel.
    - fs: Sampling frequency of the EEG data.

    Returns:
    - absolute_power_theta: Absolute power of theta wave.
    """

    # Calculate power spectral density using Welch method
    f, Pxx = welch(eeg_data_first_91000, fs=fs, nperseg=frame_size)

    # Find the indices corresponding to the theta frequency range (4~8Hz)
    theta_indices = np.where((f >= 4) & (f <= 8))[0]

    # Calculate the absolute power in the theta range
    absolute_power_theta = np.trapz(Pxx[theta_indices])

    return absolute_power_theta

def calculate_relative_power(theta_power, alpha_power, beta_power, gamma_power):
    """
    Calculate relative power of the theta wave.

    Parameters:
    - theta_power: Absolute power of the theta wave.
    - alpha_power: Absolute power of the alpha wave.
    - beta_power: Absolute power of the beta wave.
    - gamma_power: Absolute power of the gamma wave.

    Returns:
    - rp_theta: Relative power of the theta wave.
    """

    # Calculate total power
    total_power = theta_power + alpha_power + beta_power + gamma_power

    # Calculate relative power of the theta wave
    rp_theta = theta_power / total_power

    return rp_theta

def calculate_absolute_power_gamma(eeg_data_first_91000, fs=500, frame_size=500):
    """
    Calculate the absolute power of gamma wave (30~40Hz) from EEG data.

    Parameters:
    - eeg_data: 1D numpy array, EEG data for a single channel.
    - fs: Sampling frequency of the EEG data.
    - frame_size: Size of each segment for computing the power spectral density.

    Returns:
    - absolute_power_gamma: Absolute power of gamma wave.
    """

    # Calculate power spectral density using Welch method
    f, Pxx = welch(eeg_data_first_91000, fs=fs, nperseg=frame_size)

    # Find the indices corresponding to the gamma frequency range (30~40Hz)
    gamma_indices = np.where((f >= 30) & (f <= 40))[0]

    # Calculate the absolute power in the gamma range
    absolute_power_gamma = np.trapz(Pxx[gamma_indices])

    return absolute_power_gamma

def calculate_absolute_power_beta(eeg_data_first_91000, fs=500, frame_size=500):
    """
    Calculate the absolute power of beta wave (13~30Hz) from EEG data.

    Parameters:
    - eeg_data: 1D numpy array, EEG data for a single channel.
    - fs: Sampling frequency of the EEG data.
    - frame_size: Size of each segment for computing the power spectral density.

    Returns:
    - absolute_power_beta: Absolute power of beta wave.
    """

    # Calculate power spectral density using Welch method
    f, Pxx = welch(eeg_data_first_91000, fs=fs, nperseg=frame_size)

    # Find the indices corresponding to the beta frequency range (13~30Hz)
    beta_indices = np.where((f >= 13) & (f <= 30))[0]

    # Calculate the absolute power in the beta range
    absolute_power_beta = np.trapz(Pxx[beta_indices])

    return absolute_power_beta

def calculate_absolute_power_alpha(eeg_data_first_91000, fs=500, frame_size=500):
    """
    Calculate the absolute power of alpha wave (8~13Hz) from EEG data.

    Parameters:
    - eeg_data: 1D numpy array, EEG data for a single channel.
    - fs: Sampling frequency of the EEG data.
    - frame_size: Size of each segment for computing the power spectral density.

    Returns:
    - absolute_power_alpha: Absolute power of alpha wave.
    """

    # Calculate power spectral density using Welch method
    f, Pxx = welch(eeg_data_first_91000, fs=fs, nperseg=frame_size)

    # Find the indices corresponding to the alpha frequency range (8~13Hz)
    alpha_indices = np.where((f >= 8) & (f <= 13))[0]

    # Calculate the absolute power in the alpha range
    absolute_power_alpha = np.trapz(Pxx[alpha_indices])

    return absolute_power_alpha

def read_edf_file(file_path):
    raw_data = mne.io.read_raw_edf(file_path, preload=True)
    return raw_data.get_data()


def main():
    if len(sys.argv) < 2:
        print("Usage: python psd_calculation.py <file1.edf> <file2.edf> ...")
        sys.exit(1)

    # Get file paths from command-line arguments
    file_paths = sys.argv[1:]

    fs = 500
    num_electrodes = 21

    

    results_df1 = pd.DataFrame(columns=['Patient_ID'] + [f'RP_Theta_{i}' for i in range(1, num_electrodes + 1)])
    results_df2 = pd.DataFrame(columns=['Patient_ID'] + [f'RP_Theta_{i}' for i in range(1, num_electrodes + 1)])

    for file_path in file_paths:
        # Check if the file name ends with "_1.edf" or "_2.edf"
        if file_path.endswith("_1.edf"):
            eeg_data_set1 = read_edf_file(file_path)
            rp_theta_list = []
            # Process dataset 1
            for electrode in range(0, num_electrodes):
                eeg_data = eeg_data_set1[electrode,:]
                absolute_power_theta = calculate_absolute_power_theta(eeg_data, fs=fs)
                absolute_power_alpha = calculate_absolute_power_alpha(eeg_data, fs=fs)
                absolute_power_beta = calculate_absolute_power_beta(eeg_data, fs=fs)
                absolute_power_gamma = calculate_absolute_power_gamma(eeg_data, fs=fs)
                rp_theta = calculate_relative_power(absolute_power_theta, absolute_power_alpha, absolute_power_beta,
                                                    absolute_power_gamma)
                rp_theta_list.append(rp_theta)
            row_data = {'Patient_ID': file_path, **{f'RP_Theta_{i}': val for i, val in enumerate(rp_theta_list, start=1)}}
            results_df1 = results_df1._append(row_data, ignore_index=True)

        elif file_path.endswith("_2.edf"):
            eeg_data_set2 = read_edf_file(file_path)
            rp_theta_list = []
            # Process dataset 2
            for electrode in range(0, num_electrodes):
                eeg_data = eeg_data_set2[electrode,:]
                absolute_power_theta = calculate_absolute_power_theta(eeg_data, fs=fs)
                absolute_power_alpha = calculate_absolute_power_alpha(eeg_data, fs=fs)
                absolute_power_beta = calculate_absolute_power_beta(eeg_data, fs=fs)
                absolute_power_gamma = calculate_absolute_power_gamma(eeg_data, fs=fs)
                rp_theta = calculate_relative_power(absolute_power_theta, absolute_power_alpha, absolute_power_beta,
                                                    absolute_power_gamma)
                rp_theta_list.append(rp_theta)
            row_data = {'Patient_ID': file_path, **{f'RP_Theta_{i}': val for i, val in enumerate(rp_theta_list, start=1)}}
            results_df2 = results_df2._append(row_data, ignore_index=True)

    results_df1.to_csv('rp_theta_relaxed.csv', index=False)  # Update this with the path to your local results folder
    results_df2.to_csv('rp_theta_stressed.csv', index=False)  # Update this with the path to your local results folder

if __name__ == "__main__":
    main()
