# Student-Info-CRUD-Terminal_based
Student Database Information CRUD (Terminal-Based App)


## Tujuan
Aplikasi ini dikembangkan untuk mempermudah guru atau pihak sekolah dalam mengelola data siswa secara efisien, terintegrasi, dan akurat, serta mengurangi potensi human error akibat pengelolaan data secara manual. Dengan menggunakan aplikasi ini, proses pencatatan, pengolahan, dan pelaporan data siswa dapat dilakukan secara sistematis dan terstruktur langsung melalui terminal/command line interface.

## Struktur Program
Program ini dibangun menggunakan Python dengan pendekatan modular. Struktur utamanya terbagi menjadi 4 bagian:

### List of Dictionary (Data Source)
- Berisi kumpulan dictionary yang menyimpan semua data siswa.
- Terdapat juga dictionary kosong yang digunakan untuk proses manipulasi data sementara.

### Support Functions (Fungsi Pendukung)
- Fungsi-fungsi yang mendukung jalannya aplikasi.
- Mencakup: validasi input data, formatting tampilan, penghitungan nilai, hingga generate hasil akhir seperti rata-rata dan status kelulusan.

### Main Menu Handler Functions
- Terdiri dari 6 fungsi utama yang mewakili masing-masing fitur aplikasi.
- Fungsi ini akan dipanggil sesuai pilihan user di menu utama.

### Main Menu / Main Code
- Berisi while True loop sebagai navigasi utama aplikasi.
- User akan diarahkan untuk memilih fitur, dan program akan mengeksekusi fungsi yang sesuai.


## Fitur Aplikasi
### Penyajian Data Siswa
Menyediakan fitur untuk menampilkan data siswa, baik informasi umum maupun nilai akademik.
a. Data Diri Siswa:
    Menampilkan informasi seperti Student ID, Nama, Kelas, Kota Asal, serta nilai rata-rata UTS dan UAS.
b. Detail Nilai Siswa:
    Menampilkan nilai detail berdasarkan 4 mata pelajaran: Matematika, IPA, IPS, dan Bahasa Inggris.
    Opsi:
    - Per Individu: Menampilkan detail nilai seorang siswa berdasarkan Student ID.
    - Per Kelas: Menampilkan data seluruh siswa dalam kelas tertentu secara kolektif.

### Penambahan Data Siswa
- User dapat menambahkan data siswa baru.
- Input meliputi informasi pribadi dan nilai detail per mata pelajaran.
- Nilai agregat UTS dan UAS akan dihitung secara otomatis oleh sistem.

### Perubahan Data Siswa
- Mengubah informasi siswa berdasarkan Student ID.
- User cukup memilih field (key) yang ingin diubah.
- Jika yang diubah adalah nilai detail, maka nilai agregat (UTS, UAS) akan otomatis diperbarui oleh sistem.

### Penghapusan Data Siswa
- Menghapus data siswa berdasarkan Student ID.
- Sistem akan mencocokkan ID tersebut dengan dictionary data, lalu menghapus entry yang sesuai.

### Rangkuman Data Siswa
Menampilkan rangkuman nilai akhir dan status kelulusan siswa berdasarkan data yang telah diinput.
Opsi:
  - Rangkuman Pribadi: Berdasarkan Student ID.
  - Rangkuman Kelas: Berdasarkan nama kelas tertentu.


## Tools yang Digunakan
- Bahasa Pemrograman: Python
- Struktur Data: Dictionary
- Interface: Terminal - Based


## Author
Wildan Kharisma Putra Perdana
