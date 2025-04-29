import pygame
import time
import os

# Daftar lagu
musik = {
    "1": ("Lagu Anime", "oooo.mp3"),
    "2": ("Lagu Chill", "kkk.mp3")
}

# Tampilkan menu
print("=== [PILIH MUSIK YANG INGIN DIPUTAR] ===")
for key, (judul, _) in musik.items():
    print(f"{key}. {judul}")

pilihan = input("Masukkan pilihan (1/2): ").strip()

if pilihan not in musik:
    print("Pilihan tidak valid.")
    exit()

judul, file_musik = musik[pilihan]

if not os.path.exists(file_musik):
    print(f"File '{file_musik}' tidak ditemukan.")
    exit()

# Inisialisasi mixer dan putar musik
pygame.mixer.init()
pygame.mixer.music.load(file_musik)
pygame.mixer.music.play()

print(f"Memutar: {judul}... Tekan CTRL+C untuk berhenti.")

try:
    while pygame.mixer.music.get_busy():
        time.sleep(1)
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print("\nPemutaran dihentikan.")
