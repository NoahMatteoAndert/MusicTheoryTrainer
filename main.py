NOTES = [ "C" , "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
QUALITY = ["MAJOR", "MINOR"]
MODES = [""]

MAJOR_PATTERN = [2,2,1,2,2,2,1]

import random 
from enum import Enum 

class Note(Enum):
    C = 1
    Cis = 2 
    D = 3
    Dis = 4 
    E = 5
    F = 6 
    Fis = 7 
    G = 8
    Gis = 9
    A = 10
    Ais = 11
    B = 12

class Quality(Enum):
    MAJOR = 1 
    MINOR = 2 

class Scale:
    rootNote = 0
    quality = ""
    diatonicNotes = []

    def __init__(self, rootNote, quality):
        self.rootNote = rootNote
        self.quality = quality
        self.GetNotes()

    def GetNotes(self):
        # only Major right now
        currentNote = self.rootNote
        for i in MAJOR_PATTERN:
            self.diatonicNotes.append(NOTES[currentNote])
            currentNote =  currentNote + i if (currentNote + i) <= 11 else (currentNote + i) - 12

    def GetDiatonicChord(self, numeral, extension=5):
        chord = []
        numeral = numeral - 1 
        rootNote = self.diatonicNotes[numeral]
        for i in range(0, extension, 2):
            chord.append(self.diatonicNotes[numeral + i]) # OUT OF RANGE 
        return chord

    def GetParallelScale():
        # to be continued 


def GetNoteByLetter(noteLetter):
    return NOTES.index(noteLetter)

def GetRandomnScale():
    return Scale(random.randint(0,11), QUALITY[random.randint(0,1)])

if __name__ == "__main__":

    scale = GetRandomnScale()
    print("Scale Root Note: " + str(NOTES[scale.rootNote]))
    print("Diatonic Notes: " + str(scale.diatonicNotes))
    print("Diatonic Chord [II]: " + str(scale.GetDiatonicChord(3)))

    # cis = Scale(GetNoteByLetter("D"),Quality.MAJOR)
    # print(cis.diatonicNotes)    


