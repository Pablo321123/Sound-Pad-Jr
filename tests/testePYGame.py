import time
from pygame import mixer

mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') # Initialize it with the correct device
mixer.music.load("audio/o-sonho-do-Hexa-está-adiado.wav") # Load the mp3/wav
mixer.music.set_volume(0.6)
mixer.music.play() # Play it

while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)