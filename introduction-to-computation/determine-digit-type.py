# NIM/Nama : 16021178/Daffa
# Tanggal : 4 Oktober 2021
# Deskripsi : # Menentukan jenis angka pada bilangan
# -------------------------------------------------------
# KAMUS
# Angka = float
# -------------------------------------------------------
Angka = float(input("Masukkan nilai:", )) # Input, memasukan bilangan yang akan ditentukan jenisnya.
if Angka > 0 and Angka%2 == 0 and Angka - int(Angka) == 0 : 
    # Kondisi ketika Angka positif dan genap.
    print(Angka, "merupakan bilangan genap positif")
    # Ouput, ketika Angka positif dan genap.
elif Angka > 0 and Angka%2 != 0 and Angka - int(Angka) == 0 :
    # Kondisi ketika Angka positif dan ganjil.
    print(Angka, "merupakan bilangan ganjil positif")
    # Ouput, ketika Angka positif dan ganjil.
elif Angka > 0  and Angka - int(Angka) != 0 :
    # Kondisi ketika Angka merupakan bilangan positif dan merupakan desimal sehingga tidak dapat ditentukan ganjil genapnya.
    print(Angka, " merupakan bilangan positif")
elif Angka < 0 :
    # Kondisi ketika Angka negatif.
    print(Angka, "merupakan bilangan negatif")
    # Ouput, ketika Angka negatif.
elif Angka == 0 :
    # Kondisi ketika Angka nol.
    print(Angka, "merupakan bilangan nol")
    # Output,ketika Angka nol.