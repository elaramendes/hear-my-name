import pyaudio
import json
import vosk
import threading
import pygame


class AudioRecorder:
    def __init__(self, name):
        self.name = name  # Atributo que armazena o nome da pessoa

    def audio_recorder(self, callback, is_recording_func):
        mic = pyaudio.PyAudio()

        # Load model
        model = vosk.Model("model")

        print("Devices:")
        for i in range(mic.get_device_count()):
            info = mic.get_device_info_by_index(i)
            print(f"Device {i}: {info['name']} - Type: {'Input' if info['maxInputChannels'] > 0 else 'Output'}")

        device_index = 1
        stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024,
                          input_device_index=device_index)
        stream.start_stream()
        recognizer = vosk.KaldiRecognizer(model, 16000)

        # name = input(str("What's your name? "))
        print("It's time to speak!")
        print(f"Your name is {self.name}")

        with open('text.txt', 'w'):
            pass

        processed_lines = 0
        while is_recording_func():
            data = stream.read(4096)
            if len(data) == 0:
                break

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print("You said:", result['text'])
                with open('text.txt', 'a') as text:
                    text.write(f"{result['text']}\n")

                    with open('text.txt', 'r') as name_file:
                        names = name_file.readlines()
                        for index, line in enumerate(names[processed_lines:], start=processed_lines):
                            if self.name.lower() in line.lower():
                                callback("They're looking for you!")
                                threading.Timer(2, lambda: callback("")).start()

                    processed_lines = len(names)

            else:
                partial_result = recognizer.PartialResult()
                partial_json = json.loads(partial_result)

                if self.name.lower() in partial_json['partial'].lower():
                    callback("They're looking for you (partial)!")
                    threading.Timer(2, lambda: callback("")).start()

        stream.stop_stream()
        stream.close()
        mic.terminate()

class PlaySong:
    def __init__(self):
        pygame.mixer.init()

    def play_song(self, file):
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()

    def stop_song(self):
            pygame.mixer.music.stop()



