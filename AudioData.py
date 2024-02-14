from queue import Queue
import speech_recognition as sr

class AudioData:
    def __init__(self):
        self.audio_data_queue = Queue()
        self.source = sr.Microphone(sample_rate=16000)
        self.recorder = sr.Recognizer()
        self.energy_threshold = 1000
        self.recorder.energy_threshold = self.energy_threshold
        self.recorder.dynamic_energy_threshold = False
        with self.source:
            self.recorder.adjust_for_ambient_noise(self.source)
        self.recorder.listen_in_background(self.source, self.record_callback, phrase_time_limit=5)        
    
    def record_callback(self,_, audio:sr.AudioData) -> None:
        #put the data in to the queue
        data = audio.get_raw_data()
        self.audio_data_queue.put(data)

    