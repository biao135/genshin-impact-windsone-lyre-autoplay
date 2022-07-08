import pynput
import time
import string
import ctypes
import keyboard
from os import system

# compile on cmd with admin privilege
# change these
filename = [
    "summertime.txt",
    "Yoru ni kakeru.txt",
    "Senbonzakura.txt",
    "Flower Dance.txt"
    ]
#stop changing starting from here
#-----------------------------------------------------
press = pynput.keyboard.Controller().press
release = pynput.keyboard.Controller().release
z = pynput.keyboard.KeyCode.from_vk(0x5A)
x = pynput.keyboard.KeyCode.from_vk(0x58)
c = pynput.keyboard.KeyCode.from_vk(0x43)
v = pynput.keyboard.KeyCode.from_vk(0x56)
b = pynput.keyboard.KeyCode.from_vk(0x42)
n = pynput.keyboard.KeyCode.from_vk(0x4E)
m = pynput.keyboard.KeyCode.from_vk(0x4D)
a = pynput.keyboard.KeyCode.from_vk(0x41)
s = pynput.keyboard.KeyCode.from_vk(0x53)
d = pynput.keyboard.KeyCode.from_vk(0x44)
f = pynput.keyboard.KeyCode.from_vk(0x46)
g = pynput.keyboard.KeyCode.from_vk(0x47)
h = pynput.keyboard.KeyCode.from_vk(0x48)
j = pynput.keyboard.KeyCode.from_vk(0x4A)
q = pynput.keyboard.KeyCode.from_vk(0x51)
w = pynput.keyboard.KeyCode.from_vk(0x57)
e = pynput.keyboard.KeyCode.from_vk(0x45)
r = pynput.keyboard.KeyCode.from_vk(0x52)
t = pynput.keyboard.KeyCode.from_vk(0x54)
y = pynput.keyboard.KeyCode.from_vk(0x59)
u = pynput.keyboard.KeyCode.from_vk(0x55)
space = pynput.keyboard.Key.space

while True:
    err = False
    song = 9999
    while not 0 < song <= len(filename):
        try:
            system("cls")
            print("-- HOLD P TO END THE AUTOPLAY --")
            print("-- INPUT 0 TO END THE PROGRAM --")
            print("Song List:")
            for i in range(len(filename)):
                print(i+1, ":", filename[i][:-4])
            if err:
                print("\nInvalid input!")
            err = True
            song = int(input("\nPick a song: "))
            if song == 0:
                exit()

        except:
            if song == 0:
                exit()

    for i in range (5, 0 ,-1):
        print("Autoplay starts in", i, "second(s)..." )
        time.sleep(1)
    song = open(filename[song-1], "r")
    pitch = int(song.readline()[6:])
    prev = 0
    while not keyboard.is_pressed('p'):
        try:
            curr = int(song.readline()[5:])
            if curr != 0:
                time.sleep((curr-prev)/1000)
                prev = curr
            key = int(song.readline()[8:]) + pitch
            if key == 0:
                key = z
            elif key == 1:
                key = x
            elif key == 2:
                key = c
            elif key == 3:
                key = v
            elif key == 4:
                key = b
            elif key == 5:
                key = n
            elif key == 6:
                key = m
            elif key == 7:
                key = a
            elif key == 8:
                key = s
            elif key == 9:
                key = d
            elif key == 10:
                key = f
            elif key == 11:
                key = g
            elif key == 12:
                key = h
            elif key == 13:
                key = j
            elif key == 14:
                key = q
            elif key == 15:
                key = w
            elif key == 16:
                key = e
            elif key == 17:
                key = r
            elif key == 18:
                key = t
            elif key == 19:
                key = y
            else:
                key = u
            press(key)
            release(key)
            
        except:
            song.close()
            break















    
