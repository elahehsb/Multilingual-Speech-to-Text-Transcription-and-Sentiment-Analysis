import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torchaudio

class ASRModel:
    def __init__(self, model_name="facebook/wav2vec2-large-xlsr-53"):
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)

    def transcribe(self, audio):
        input_values = self.processor(audio, return_tensors="pt", padding=True).input_values
        logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.batch_decode(predicted_ids)
        return transcription

if __name__ == "__main__":
    asr = ASRModel()
    transcription = asr.transcribe("path_to_audio.wav")
    print("Transcription:", transcription)
