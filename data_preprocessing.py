import torchaudio
from torchaudio.datasets import COMMONVOICE
import os

def load_and_preprocess_data(languages=['en', 'fi'], data_dir='./data'):
    datasets = []
    for lang in languages:
        dataset = COMMONVOICE(root=data_dir, tsv=lang, download=True)
        for waveform, sample_rate, _, _, _, _ in dataset:
            # Example preprocessing: Resampling to 16kHz
            waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)
            datasets.append((waveform, 16000))
    return datasets

if __name__ == "__main__":
    datasets = load_and_preprocess_data()
    print(f"Loaded and preprocessed {len(datasets)} audio samples.")
