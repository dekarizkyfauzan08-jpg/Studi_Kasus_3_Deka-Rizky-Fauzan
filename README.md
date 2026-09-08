# Studi_Kasus_3_Pengelompokan Nilai Ujian Mahasiswa

# identitas

Nama: [Deka Rizky Fauzan]

NIM: [2609116052]

Kelas: [B]

---

# Deskripsi Program

Program ini dibuat untuk mengelompokkan nilai ujian mahasiswa menjadi dua kelompok, yaitu **Lulus** dan **Remedi**.
Batas nilai yang digunakan adalah 65. Jika nilai mahasiswa lebih besar atau sama dengan 65, maka nilai tersebut masuk ke kelompok Lulus. Jika nilainya kurang dari 65, maka masuk ke kelompok Remedi.
Program menggunakan **Tuple** untuk menyimpan batas nilai dan **List** untuk menyimpan nilai yang dimasukkan serta hasil pengelompokan nilai.

---

# Struktur Data yang Digunakan

# 1.Tuple

Tuple digunakan untuk menyimpan batas nilai.

python
batas_nilai = (65, 100)
# 2. List
nilai_masuk = []

lulus = []

remedi = []

nilai_masuk digunakan untuk menyimpan semua nilai yang dimasukkan.

lulus digunakan untuk menyimpan nilai yang lebih besar atau sama dengan 65.

remedi digunakan untuk menyimpan nilai yang kurang dari 65.

List menggunakan tanda kurung siku [] dan datanya dapat diubah.

# Cara Kerja Program
Program meminta pengguna untuk memasukkan nilai ujian secara berulang.

Input akan terus dilakukan sampai pengguna mengetik:

selesai

Setiap nilai yang dimasukkan akan disimpan ke dalam List nilai_masuk.

Selanjutnya program memeriksa nilai tersebut.

Jika nilai lebih besar atau sama dengan 65:

if nilai >= batas_nilai[0]:

    lulus.append(nilai)
    
maka nilai dimasukkan ke List lulus.

Jika nilai kurang dari 65:

else:
    remedi.append(nilai)
    
maka nilai dimasukkan ke List remedi.

Program juga memiliki fitur untuk menghapus satu nilai apabila terjadi kesalahan saat memasukkan nilai.

# Fitur Penghapusan Nilai
Setelah semua nilai dimasukkan, pengguna dapat memilih satu nilai yang ingin dihapus.

Program menggunakan:

nilai_masuk.remove(nilai_hapus)

Jika nilai yang dihapus termasuk nilai lulus, maka nilai tersebut juga dihapus dari List lulus.

Jika nilai tersebut termasuk nilai remedi, maka nilai tersebut dihapus dari List remedi.

Contoh Input

Nilai yang dimasukkan:

80

55

70

60

90

selesai

Kemudian nilai yang salah dimasukkan dan ingin dihapus:

55

# Hasil Program
Sebelum nilai dihapus:

Nilai masuk: [80, 55, 70, 60, 90]

Setelah nilai 55 dihapus:

Nilai Masuk: [80, 70, 60, 90]

Nilai lulus: [80, 70, 90]

Nilai remedi: [60]

# Kesimpulan
Program berhasil mengelompokkan nilai ujian mahasiswa berdasarkan batas nilai yang telah ditentukan.

Nilai yang lebih besar atau sama dengan 65 masuk ke kelompok Lulus, sedangkan nilai di bawah 65 masuk ke kelompok Remedi.

Program juga dapat menghapus satu nilai yang salah dimasukkan. Dalam program ini digunakan Tuple dan List sebagai struktur data sesuai dengan materi dasar pemrograman Python.

# ss output program
<img width="1092" height="761" alt="image" src="https://github.com/user-attachments/assets/afa949f8-06f1-4a79-bd20-9393f63e762e" />
