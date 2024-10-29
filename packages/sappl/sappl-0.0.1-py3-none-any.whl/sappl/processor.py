# sappl/processor.py

import numpy as np
from sappl import io, transform, utils, feature_extraction

try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False


class AudioProcessor:
    """
    Central class for handling audio loading, saving, transformations, and utility operations.
    This class acts as a wrapper around sappl functions, adapting dynamically to library updates.
    """

    def __init__(self, sample_rate=16000, max_length=None, padding_value=0.0, target_db=-20.0):
        """
        Initializes the AudioProcessor with default configurations.

        Args:
            sample_rate (int): Sample rate for loading and saving audio. Default is 16000.
            max_length (float): Max length in seconds for padding/truncation. Default is None (no padding/truncation).
            padding_value (float): Value used for padding. Default is 0.0.
            target_db (float): Target dB level for RMS normalization. Default is -20.0 dB.
        """
        self.sample_rate = sample_rate
        self.max_length = max_length
        self.padding_value = padding_value
        self.target_db = target_db

    # --- I/O Operations ---
    def load_audio(self, file_path, mono=True):
        return io.load_audio(file_path, sample_rate=self.sample_rate, mono=mono)

    def save_audio(self, file_path, audio):
        io.save_audio(file_path, audio, sample_rate=self.sample_rate)

    # --- Transformations ---
    def stft(self, audio, n_fft=2048, hop_length=512, win_length=None):
        return transform.stft(audio, n_fft=n_fft, hop_length=hop_length, win_length=win_length)

    def istft(self, stft_matrix, hop_length=512, win_length=None):
        return transform.istft(stft_matrix, hop_length=hop_length, win_length=win_length)

    def magphase(self, stft_matrix):
        return transform.magphase(stft_matrix)

    def compute_mel_spectrogram(self, audio, n_fft=2048, hop_length=512, n_mels=128, f_min=0.0, f_max=None):
        return transform.compute_mel_spectrogram(audio, sample_rate=self.sample_rate, n_fft=n_fft,
                                                 hop_length=hop_length, n_mels=n_mels, f_min=f_min, f_max=f_max)

    # --- Utility Functions ---
    def convert_to_mono(self, audio):
        return utils.convert_to_mono(audio)

    def pad_audio(self, audio):
        if self.max_length:
            return utils.pad_audio(audio, max_length=self.max_length, sample_rate=self.sample_rate, padding_value=self.padding_value)
        return audio

    def truncate_audio(self, audio):
        if self.max_length:
            return utils.truncate_audio(audio, max_length=self.max_length, sample_rate=self.sample_rate)
        return audio

    def normalize(self, audio, method="min_max"):
        return utils.normalize(audio, method=method)

    def rms_normalize(self, audio):
        return utils.rms_normalize(audio, target_db=self.target_db)
    
    # --- Feature Extraction ---
    def extract_mfcc(self, audio, n_mfcc=13, n_fft=2048, hop_length=512):
        return feature_extraction.extract_mfcc(audio, sample_rate=self.sample_rate, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

    def extract_chroma(self, audio, n_fft=2048, hop_length=512):
        return feature_extraction.extract_chroma(audio, sample_rate=self.sample_rate, n_fft=n_fft, hop_length=hop_length)

    def extract_tonnetz(self, audio):
        return feature_extraction.extract_tonnetz(audio, sample_rate=self.sample_rate)

    def extract_zero_crossing_rate(self, audio, frame_length=2048, hop_length=512):
        return feature_extraction.extract_zero_crossing_rate(audio, frame_length=frame_length, hop_length=hop_length)

    def extract_spectral_contrast(self, audio, n_fft=2048, hop_length=512, n_bands=6):
        return feature_extraction.extract_spectral_contrast(audio, sample_rate=self.sample_rate, n_fft=n_fft, hop_length=hop_length, n_bands=n_bands)

    # --- Dynamic Adaptation ---
    def add_custom_function(self, func, func_name=None):
        """
        Adds a custom function to the AudioProcessor instance, allowing dynamic extension.

        Args:
            func (callable): Function to add to the AudioProcessor.
            func_name (str): Name under which the function should be accessible. 
                             If None, the function's name attribute is used.
        """
        if not callable(func):
            raise ValueError("Provided function is not callable.")
        setattr(self, func_name or func.__name__, func)


if __name__ == "__main__":
    # Example usage
    processor = AudioProcessor(sample_rate=16000, max_length=5.0)

    # Load audio
    audio = processor.load_audio("../samples/music_sample.wav")
    print("Loaded audio:", audio.shape)

    # Convert to mono and normalize
    audio_mono = processor.convert_to_mono(audio)
    normalized_audio = processor.normalize(audio_mono, method="peak")

    # Apply STFT and compute Mel spectrogram
    stft_matrix = processor.stft(normalized_audio)
    mel_spec = processor.compute_mel_spectrogram(normalized_audio)
    print("STFT shape:", stft_matrix.shape)
    print("Mel Spectrogram shape:", mel_spec.shape)

    # Add custom function dynamically
    def example_custom_function(audio):
        return audio * 2  # A simple custom operation for illustration
    
    processor.add_custom_function(example_custom_function)
    doubled_audio = processor.example_custom_function(audio)
    print("Doubled audio:", doubled_audio.shape)
