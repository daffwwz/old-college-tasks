# NIM/Nama : 16021178/Daffa
# Tanggal : 4 Oktober 2021
#  
# Deskripsi :    # Judul Program : Program Kalkulator Sederhana
                 # Membuat perhitungan sederhana dengan pembulatan sebesar 5 digit

# -------------------------------------------------------
# KAMUS
# A1, A2 : float
# OP : string
# -------------------------------------------------------

A1 = float(input("Masukan angka pertama: ", )) # Input, A1 adalah angka kedua yang dimasukkan dalam program.
print("Gunakan operator yang tersedia : + untuk penjumlahan, - untuk pengurangan, / untuk pembagian, * untuk perkalian, % untuk sisa hasil bagi") 
OP = str(input("Masukan operator:", )) # Input, OP adalah variabel untuk menunjukan operator.
A2 = float(input("Masukan angka kedua: ", )) # Input, A2 adalah angka kedua yang dimasukkan dalam program.
if OP == "+" : 
# Kondisi ketika operator berupa penjumlahan.
         print("Maka hasil dari", A1, OP, A2, "adalah", round(A1 + A2, 10) ) 
         # Output, Hasil dari penjumlahan dua buah angka.
elif OP == "-" : 
# Kondisi ketika operator berupa pengurangan
         print("Maka hasil dari", A1, OP, A2,"adalah", round(A1-A2, 10))
         # Output, Hasil dari pengurangann dua buah angka.
elif OP == "/" :  
# Kondisi ketika operator berupa pembagian.
        if A2 == 0 : 
             print("tidak dapat menemukan hasil bagi dengan pembagi nol")
                # Kondisi ketika pembilang merupakan angka nol.
        elif True :
            print("Maka hasil dari pembagian", A1, OP, A2, "yang dibulatkan ke bawah adalah", int(A1/A2))
                # Output, hasil pembagian dua angka yang berupa bilangan bulat.
elif OP == "*" :
# Kondisi ketika operator berupa perkalian.
         print("Maka hasil dari",A1, OP, A2, "adalah", round(A1*A2, 10))
            # Output, hasil perkalian dua angka yang berupa bilangan bulat. 
elif OP == "%" : 
# Kondisi ketika operator berupa modulo
    if A1- int(A1) != 0 or A2 - int(A2) != 0:
        # kondisi apabila terdapat setidaknya memiliki satu bilangan desimal.
        print("Tidak bisa menemukan hasil bagi dalam bilangan desimal")
        # Output, ketika terdapat setidaknya satu bilangan desimal.
    else:
        A1 = int(A1) # mengubah A1 menjadi bilangan bulat.
        A2 = int(A2) # mengubah A2 menjadi bilangan bulat.
        if A2 == 0 : 
         print("tidak dapat menemukan hasil bagi dengan nol ")
         # Output, ketika terdapat pembilang yang berupa angka nol.
        elif True :
         print("Maka sisa pembagian dari", A1, OP, A2, "adalah", A1%A2)
        # Output, sisa bagi dua angka yang berupa bilangan bulat
else : # Kondisi ketika tidak ada operator yang memenuhi
    print("TIdak dapat menghitung hasil dengan nilai operator yang digunakan")
    # Output, ketika tidak ada operator yang memenuhi.
