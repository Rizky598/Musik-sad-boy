import os
import time
import sys

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
    ║      Termux Anime Style    ║
    ╚════════════════════════════╝
        ~ Slime Rimuru Mode ~
{RESET}""")

lirik = {
    "lagu1.mp3": [
        "Aku suka kamu...",
        "Tapi kamu tak tahu...",
        "Hatiku berbunga setiap lihat kamu..."
    ],
    "lagu2.mp3": [
        "Langit malam penuh bintang...",
        "Kuingat senyummu yang tenang...",
        "Kau cahaya di gelapku..."
    ]
}

def ketik(teks, delay=0.05, suara=False):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    if suara:
        os.system(f'espeak "{teks}"')

def main():
    banner()
    ketik(f"{HIJAU}Pilih lagu yang ingin kamu dengar, Master Rimuru:{RESET}")
    print("1. Lagu Romantis")
    print("2. Lagu Malam")
    print("0. Keluar")

    pilihan = input(f"{MERAH}Masukkan pilihan: {RESET}")
    if pilihan == "1":
        putar_lagu("lagu1.mp3")
    elif pilihan == "2":
        putar_lagu("lagu2.mp3")
    elif pilihan == "0":
        ketik("Sampai jumpa, master!", suara=True)
        exit()
    else:
        ketik("Pilihan tidak valid!", suara=True)
        time.sleep(1)
        main()

def putar_lagu(nama_file):
    os.system(f"mpv {nama_file} > /dev/null 2>&1 &")
    ketik(f"{KUNING}♪ Sedang memutar: {nama_file} ♪{RESET}", suara=True)
    print(f"{BIRU}Lirik Lagu:{RESET}")
    for baris in lirik.get(nama_file, []):
        ketik(f"{HIJAU}♪ {baris}{RESET}", 0.07, suara=True)
        time.sleep(1)

    input(f"\n{MERAH}Tekan Enter untuk kembali ke menu...{RESET}")
    main()

if __name__ == "__main__":
    main()
