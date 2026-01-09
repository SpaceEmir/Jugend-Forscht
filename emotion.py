from sounding import Sound
from PyQt5.QtWidgets import *

gefuehle = {
    "aufregung": "11101",
    "glück": "10110",
    "ruhe": "10011",
    "traurigkeit": "00101",
    "angst": "01100",
    "wut": "01111"
}

def g():
    return gefuehle

def umwandeln(gefuehl):
    if gefuehl.lower() not in gefuehle.keys():
        return 200
        
    zahl = gefuehle[gefuehl]
    return 200 + int(zahl, 2) * 10

class EmotionWindow():
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle("Gefühl anhören")
        self.window.resize(400, 200)

        self.eingabe = QLineEdit()
        self.eingabe.setPlaceholderText("Ein Gefühl eingeben...")

        self.button = QPushButton("Anhören")

        self.ly1 = QHBoxLayout()
        self.ly2 = QHBoxLayout()
        self.ly3 = QVBoxLayout()

        self.ly1.addWidget(self.eingabe)
        self.ly2.addWidget(self.button)

        self.ly3.addLayout(self.ly1)
        self.ly3.addLayout(self.ly2)

        self.window.setLayout(self.ly3)

        self.button.clicked.connect(self.abspielen)

    def abspielen(self):
        emotion = Emotion(self.eingabe.text())
        emotion.hoeren()

    def beginn(self):
        self.window.show()
        self.app.exec_()


class Emotion:
    def __init__(self, gefuehl):
        self.gefuehl = gefuehl.lower()
        self.wert = self.umwandeln()

    def umwandeln(self):
        if self.gefuehl not in gefuehle.keys():
            return 200
        
        zahl = gefuehle[self.gefuehl]
        return 200 + int(zahl, 2) * 10
    
    def hoeren(self, zeit=1.0):
        sound = Sound(self.wert, zeit)
        sound.start()

if __name__ == "__main__":
    window = EmotionWindow()
    window.beginn()