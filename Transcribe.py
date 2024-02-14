from AudioData import AudioData
import time
import whisper
import torch
import numpy as np

class Transcribe:
    def __init__(self):
        self.transcription = ''
        self.audio_data = AudioData()
        self.start_time = time.time()
        self.current_time = None
        self.trans_index = 0
        self.audio_model = whisper.load_model("medium.en")

    def audio_transcribe(self):
        self.current_time = time.time()
        duration = int(self.current_time - self.start_time)
        #self.trans_index = duration // 5
        if(duration % 2 == 0):
            print(duration)
            audio_data = b''.join(self.audio_data.audio_data_queue.queue)
            audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
            result = self.audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
            text = result['text'].strip()  
            self.transcription+=text 
            self.audio_data.audio_data_queue.queue.clear()




