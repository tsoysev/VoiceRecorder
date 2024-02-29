
import sounddevice as sd
from scipy.io.wavfile import write


print("\nWELCOME TO MY VOICE RECORDER \n\n")

freqStep = 0
freq = 0

while not 0<freqStep<4:
    try:
        freqStep = int(input("Select Quality \n-Enter 3 for Digital Quality \n-Enter 2 for FM Radio Quality \n-Enter 1 for AM Radio Quality \n--Enter Here: "))
        if freqStep == 3:
            freq = 44100
            print("Digital Quality Selected.")
        elif freqStep == 2:
            freq = 22050
            print("FM Radio Quality Selected.")
        elif freqStep == 1:
            freq = 11025
            print("AM Radio Quality Selected.")
        else:
            print("\nInvalid Value\n")
    except ValueError:
        print("\nPlease Enter Integer\n")
        ferqStep = 0

duration = int(input("Set Length of the Record as Seconds: "))
fileName = input("Type your File Name: ")
fileName_wav = f"{fileName}.wav"

recording = sd.rec(int(duration*freq),samplerate=freq,channels=2)
sd.wait()
write(fileName_wav,freq,recording)