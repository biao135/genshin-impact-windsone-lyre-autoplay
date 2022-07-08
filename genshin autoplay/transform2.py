from os import system
import pynput
import time
import string
import ctypes
import keyboard
from os import system


#format text
song = open("Fly_Me_to_the_Moon_-_Neon_Genesis_Evangelion.txt", "r")
content = song.readline().replace(" ", "").replace("{","").replace("}", "").replace("\"", "").replace(",", "\n")
song.close()
song = open("Fly me to the moon.txt", "w")
song.write(content)
song.close()
#song1 = open("Flower_Dance", "r")
#song2 = open("Flower Dance.txt", "w")
#err = False
#try:
#    while True:
#        if err is True:
#            exit()
#        song2.write(song1.readline())
#        song2.write(song1.readline())
#        dump = song1.readline()
#        
#except:
#    song2.close()
#    song1.close()
#    err = True

#content = song1.readlines()
#for i in range (0, len(content), 3):
#    song2.write(content[i])
#    song2.write(content[i+1])
#song2.close()
