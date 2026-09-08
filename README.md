# Studi_Kasus_3_Awang-Farid-Al-Buhari

Nama : Awang Farid Al Buhari
NIM  : 2609116003

<img width="1387" height="816" alt="IMG_20260908_191321_922" src="https://github.com/user-attachments/assets/d3a1f0cc-d048-4f1b-aa9b-624d0e868ff8" />

<img width="1385" height="834" alt="IMG_20260908_191321_717" src="https://github.com/user-attachments/assets/b89919d2-1d4d-43db-a563-d896b168a6bb" />

PENJELASAN

*daftar_buku dibuat sebagai tuple berisi 5 judul buku, karena data ini tidak boleh diubah selama program berjalan.

*pinjaman dibuat sebagai list kosong, untuk menampung judul buku yang berhasil dipinjam Peter.

*Program melakukan perulangan for untuk mencetak seluruh isi daftar_buku di awal program, agar Peter tahu buku apa saja yang tersedia.

*Agar Peter dapat meminjam buku lebih dari sekali, program menampilkan menu (Pinjam / Hapus / Selesai) di dalam perulangan while True yang hanya akan berhenti (break) saat Peter memilih "Selesai".

*Saat Peter memasukkan judul buku, program mengecek dengan if judul in daftar_buku.
Jika buku ditemukan → judul ditambahkan ke pinjaman dengan pinjaman.append() dan muncul pesan "Buku berhasil dipinjam!".
Jika tidak ditemukan → muncul pesan "Buku tidak tersedia.".

*Peter dapat memilih menu hapus, program menampilkan isi pinjaman lalu menghapus judul yang diminta menggunakan pinjaman.remove().

*Setelah Peter memilih "Selesai", program menampilkan seluruh isi akhir pinjaman, yaitu daftar final buku yang sedang dipinjam Peter.

HASIL

<img width="1454" height="872" alt="IMG_20260908_191322_119" src="https://github.com/user-attachments/assets/3c07849b-87a4-49b4-ba1e-63a7031e15e6" />

<img width="1409" height="548" alt="IMG_20260908_191321_641" src="https://github.com/user-attachments/assets/04c9f7a0-9e76-4390-b099-ec9b7f00766f" />

Screenshot di atas menunjukkan hasil menjalankan program: menampilkan daftar buku, proses peminjaman berhasil/gagal, proses penghapusan pinjaman, hingga daftar akhir buku yang dipinjam Peter.


