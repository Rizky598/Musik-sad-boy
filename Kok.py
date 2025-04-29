import pygame
import time
import os

# Ganti dengan path lagu kamu (format .mp3 atau .wav)
music_file = "oooo.mp3"

# Cek apakah file ada
if not os.path.exists(music_file):
    print(f"File '{music_file}' tidak ditemukan.")
    exit()

# Inisialisasi mixer
pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

print("Memutar musik... Tekan CTRL+C untuk berhenti.")

try:
    while pygame.mixer.music.get_busy():
        time.sleep(1)
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print("\nPemutaran dihentikan.")
