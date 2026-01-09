import numpy as np
import sounddevice as sd

class Sound():
    def __init__(self, fr, dr, fs=44100):
        self.fs = fs
        self.duration = dr
        self.frequency = fr

    def start(self):
        t = np.linspace(0, self.duration, int(self.fs * self.duration), endpoint=False)
        signal = np.sin(2 * np.pi * self.frequency * t)

        sd.play(signal, self.fs)
        sd.wait()