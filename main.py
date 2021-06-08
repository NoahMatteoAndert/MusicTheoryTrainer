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
        print("root number: " + str(NOTES[self.rootNote]))

    def GetNotes(self):
        # only Major right now
        currentNote = self.rootNote
        for i in MAJOR_PATTERN:
            self.diatonicNotes.append(NOTES[currentNote])
            currentNote =  currentNote + i if (currentNote + i) <= 11 else (currentNote + i) - 12

def GetNoteByLetter(noteLetter):
    return NOTES.index(noteLetter)

def GetScales():
    return NOTE(random.randint(0,12)) + " " +  QUALITY[random.randint(0,1)];

if __name__ == "__main__":
    cis = Scale(GetNoteByLetter("D"),Quality.MAJOR)
    print(cis.diatonicNotes)    

