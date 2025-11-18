# NIM/Nama : 16021178/Daffa
# Tanggal : 16 Oktober 2021
# Deskripsi :   # Memasukan bilangan N dan menampilkan bilangan 10 pangkat x terkecil yang lebih dari N.

# KAMUS
# N = Integer
# X = Integer

N = int(input("Masukan N : "))                      # Input, menentukan bilangan N yang akan dipilih sesuai kehendak pengguna.
x = 0                                    # Memulai angka dalam pangkat dengan 0
while (10**x - N) <= 0 :                       # Fungsi pengulangan untuk menentukan bahwa 10 pangkat x kurang dari atau sama dengan N, atau 10 pangkat N dikurangi N bernilai negatif.
    x += 1                               # Indikator perubahan untuk mengubah kondisi X sehingga fungsi pengulangan dapat berhenti apabila kondisi tak lagi terpenuhi.
print(10**x)                                # Ouput, Menampilkan 10 pangkat x dengan x hasil fungsi pengulangan.
