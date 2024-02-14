# from time import sleep
# from AudioTranscribe import AudioTranscribe
# from llama_cpp import Llama
# import os
# # llm = Llama(
# #       model_path="model/llama-2-7b.Q2_K.gguf",
# #       # n_gpu_layers=-1, # Uncomment to use GPU acceleration
# #       # seed=1337, # Uncomment to set a specific seed
# #       # n_ctx=2048, # Uncomment to increase the context window
# # )
# audioTranscribe = AudioTranscribe()
# Transcription = ""
# while True:
#     #print("Listening...")
#     audioText=audioTranscribe.transcribe()
#     if(audioText is not None and len(audioText)>0):
#         Transcription+=audioText
#         # print("Input:"+audioText)
#         # #print("Transcription:"+audioText)
#         # output = llm(
#         #     Transcription, # Prompt
#         #     max_tokens=1, # Generate up to 32 tokens, set to None to generate up to the end of the context window
#         #     stop=[".", "\n"], # Stop generating just before the model would generate a new question
#         #     echo=True # Echo the prompt back in the output
#         # ) # Generate a completion, can also call create_completion
#         # print("Prediction:"+output['choices'][0]['text'])
#     sleep(0.2)
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(Transcription)

from Transcribe import Transcribe
from AudioData import AudioData
from time import sleep
import os

transcribe = Transcribe()

while True:
    transcribe.audio_transcribe()
    sleep(1.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(transcribe.transcription)