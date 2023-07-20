# Purwadhika_JCDS_Capstone_1
Berikut merupakan program Perpustakaan sederhana yang dibuat menggunakan Python

Terdapat 7 Menu utama, yang terdiri dari :
1. Lihat Buku yang Tersedia
2. Tambah Buku
3. Update Buku
4. Hapus Buku
5. Peminjaman/Pengembalian Buku
6. Exit

Menu 1 : Lihat Buku yang Tersedia, digunakan untuk melihat buku yang ada pada Perpustakaan
kalian dapat melihat :
1. Seluruh buku yang tersedia 
2. Search berdasarkan judul
3. Search berdasarkan Book ID

Menu 2 : Tambah Buku, digunakan untuk menambahkan buku baru pada perpustakaan
3 key utama : BOOK_ID, Title, & Author ini tidak boleh sama dengan data sebelumnya
Jika 3 key utama tidak sama, maka buku berhasil ditambahkan

Menu 3 : Update Buku, digunakan untuk mengubah isi daftar buku yang sudah ada 
Caranya dengan masuk menggunakan BOOK ID, kemudian seluruh kolomnya dapat diganti

Menu 4 : Hapus Buku, digunakan untuk menghapus buku dalam daftar buku
caranya dengan masuk menggunakan BOOK ID, kemudian seluruh baris dalam BOOK ID akan terhapus

Menu 5 : Peminajan/Pengembalian Buku, digunakan untuk meminjam/ mengembalikan buku yang ada di perpustakaan
1. Menu Peminjaman Buku
	Maksimal Buku yang dapat dipinjam adalah 3 buku
	Tidak bisa memilih buku yang sama jika sudah dipinjam sebelumnya
2. Menu Pengembalian Buku
	Menu ini dapat diakses jika kalian sudah melakukan peminjaman buku
	Buku yang dapat dikembalikan hanya buku yang sudah dipinjam sebelumnya
