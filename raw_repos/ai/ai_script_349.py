"""
Design an algorithm to detect the pattern of spikes in an EEG
"""

import numpy as np

def detect_spike_pattern(eeg_data):
    # Compute power spectrum of the EEG data
    power_spectra = np.abs(np.fft.rfft(eeg_data))
    # Detect spikes by finding peaks in the power spectrum
    spikes = np.where(power_spectra > np.mean(power_spectra) + np.std(power_spectra))[0]
    # Construct the spike pattern using differences between consecutive spikes
    pattern = [spikes[i+1] - spikes[i] for i in range(len(spikes)-1)]
    return pattern