import os
import time

MERAH = '\033[91m'
HIJAU = '\033[92m'
BIRU = '\033[94m'
KUNING = '\033[93m'
RESET = '\033[0m'

def banner():
    os.system("clear")
    print(f"""{BIRU}
     (´｡• ᵕ •｡`) ♡
    ╔════════════════════════════╗
    ║     RIMURU MUSIC PLAYER    ║
    ║    (Voice Only Edition)    ║
    ╚════════════════════════════╝
{RESET}""")

lirik = {
    "oooo.mp3": [
        "Aku suka kamu...",
        "Tapi kamu tak tahu...",
        "Hatiku berbunga setiap lihat kamu..."
    ],
    "kkk.mp3": [
        "Langit malam penuh bintang...",
        "Kuingat senyummu yang tenang...",
        "Kau cahaya di gelapku..."
    ]
}

def main():
    banner()
    print(f"{HIJAU}Pilih lagu yang ingin kamu dengar:{RESET}")
    print("1. Lagu Romantis")
    print("2. Lagu Malam")
    print("0. Keluar")

    pilihan = input(f"{MERAH}Masukkan pilihan: {RESET}")
    if pilihan == "1":
        putar_lagu("oooo.mp3")
    elif pilihan == "2":
        putar_lagu("kkk.mp3")
    elif pilihan == "0":
        os.system('espeak "Sampai jumpa, Master Rimuru"')
        exit()
    else:
        os.system('espeak "Pilihan tidak valid"')
        time.sleep(1)
        main()

def putar_lagu(nama_file):
    os.system(f"mpv {nama_file} > /dev/null 2>&1 &")
    os.system(f'espeak "Memutar {nama_file.replace(".mp3", "").replace("_", " ")}"')
    time.sleep(1)

    for baris in lirik.get(nama_file, []):
        os.system(f'espeak "{baris}"')
        time.sleep(1)

    os.system('espeak "Lagu selesai. Tekan enter untuk kembali ke menu."')
    input()
    main()

if __name__ == "__main__":
    main()
