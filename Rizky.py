import os
import time

# Warna terminal
MERAH = '\033[91m'
HIJAU = '\033[92m'
BIRU = '\033[94m'
RESET = '\033[0m'

# Hiasan ASCII
def banner():
    print(f"""{BIRU}
   ╔═════════════════════════════╗
   ║     PYTHON MUSIC PLAYER     ║
   ║        by Termux user       ║
   ╚═════════════════════════════╝
{RESET}""")

# Lirik contoh
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

# Main menu
def main():
    os.system("clear")
    banner()
    print(f"{HIJAU}Pilih lagu yang ingin diputar:{RESET}")
    print("1. Lagu Romantis")
    print("2. Lagu Malam")
    print("0. Keluar")

    pilihan = input(f"{MERAH}Masukkan pilihan: {RESET}")
    if pilihan == "1":
        putar_lagu("oooo.mp3")
    elif pilihan == "2":
        putar_lagu("kkk.mp3")
    elif pilihan == "0":
        print("Keluar...")
        exit()
    else:
        print("Pilihan tidak valid!")
        time.sleep(1)
        main()

# Fungsi untuk memutar lagu dan lirik
def putar_lagu(nama_file):
    os.system(f"mpv {nama_file} > /dev/null 2>&1 &")
    print(f"{BIRU}Memutar {nama_file}...{RESET}")
    print(f"{HIJAU}Lirik:{RESET}")
    for baris in lirik.get(nama_file, []):
        print(f"♪ {baris}")
        time.sleep(2)  # jeda antar baris lirik

    input(f"{MERAH}\nTekan Enter untuk kembali ke menu...{RESET}")
    main()

if __name__ == "__main__":
    main()
