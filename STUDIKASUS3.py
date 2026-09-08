daftar_buku = (
    "cara lulus sisfor dalam waktu 2 tahun",
    "algoritma dan pemrograman",
    "struktur data",
    "cara cepat memahami matematika diskrit",
    "tutorial lulus dengan ipk 4"
)

pinjaman = []

print("=====DAFTAR BUKU PERPUSTAKAAN FAKULTAS TEKNIK=====")
for i in range(len(daftar_buku)):
    print(str(i + 1) + ". " + daftar_buku[i])

while True:
    print("\n---MENU---")
    print("1. Pinjam Buku")
    print("2. Hapus Buku dari daftar pinjaman")
    print("3. SELESAI")

    pilihan = input("Pilih menu (1/2/3): ")
    if pilihan == "1":
        judul = input("Masukkan judul buku yang ingin dipinjam: ")
        if judul in daftar_buku:
            pinjaman.append(judul)
            print(f"Buku '{judul}' berhasil dipinjam.")

        else:
            print(f"Buku '{judul}' tidak tersedia di daftar buku.")

    elif pilihan == "2":
        if len(pinjaman) == 0:
            print("Tidak ada buku yang dipinjam.")
        else:
            print("Daftar buku yang dipinjam:")
            for i in range(len(pinjaman)):
                print(str(i + 1) + ". " + pinjaman[i])

            judul_hapus = input("Masukkan judul buku yang ingin dihapus dari daftar pinjaman: ")

            if judul_hapus in pinjaman:
                pinjaman.remove(judul_hapus)
                print(f"Buku '{judul_hapus}' berhasil dihapus dari daftar pinjaman.")
            else:
                print(f"Buku '{judul_hapus}' tidak ada dalam daftar pinjaman.")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan layanan perpustakaan.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


print("\n==== Daftar buku yang dipinjam Peter ====")
if len(pinjaman) == 0:
    print("Tidak ada buku yang dipinjam.")
else:
    for i in range(len(pinjaman)):
        print(str(i + 1) + ". " + pinjaman[i])