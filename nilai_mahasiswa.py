batas_nilai = (65, 100)

nilai_masuk = []
lulus = []
remedi = []

print("PENGELOMPOKAN NILAI UJIAN MAHASISWA")
print("Batas lulus:", batas_nilai[0])
print("Nilai maksimal:", batas_nilai[1])

while True:
    nilai = input("Masukkan nilai atau ketik selesai: ")

    if nilai == "selesai":
        break

    nilai = int(nilai)
    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedi.append(nilai)

print("Nilai masuk:", nilai_masuk)

nilai_hapus = int(input("Masukkan nilai yang ingin dihapus: "))

nilai_masuk.remove(nilai_hapus)

if nilai_hapus >= batas_nilai[0]:
    lulus.remove(nilai_hapus)
else:
    remedi.remove(nilai_hapus)

print("Nilai masuk:", nilai_masuk)
print("Nilai lulus:", lulus)
print("Nilai remedi:", remedi)