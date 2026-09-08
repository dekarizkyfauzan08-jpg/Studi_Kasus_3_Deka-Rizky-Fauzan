# Studi Kasus 3 - Pengelompokan Nilai Ujian Mahasiswa

## Identitas

Nama: [Nama Lengkap]  
NIM: [NIM]  
Kelas: [Kelas]

## Deskripsi Program

Program ini dibuat untuk mengelompokkan nilai ujian mahasiswa menjadi dua kelompok, yaitu **Lulus** dan **Remedi**.

Batas nilai yang digunakan adalah 65. Jika nilai mahasiswa lebih dari atau sama dengan 65, maka masuk ke kelompok Lulus. Jika nilai kurang dari 65, maka masuk ke kelompok Remedi.

Program dapat menerima nilai secara berulang sampai pengguna mengetik `selesai`.

## List dan Tuple yang Digunakan

Program menggunakan Tuple dan List sebagai berikut:

```python
batas_nilai = (65, 100)

nilai_masuk = []
lulus = []
remedi = []
