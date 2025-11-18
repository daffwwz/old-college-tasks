# NIM/Nama : 16021178/Daffa
# Tanggal : 16 Oktober 2021
# Deskripsi :   # Menerima bilangan X dan menentukan apakah X prima atau bukan.

# KAMUS
# X = Integer
# BilPrima = Boolean

X = int(input("Masukan X : "))                                 # Input, menentukan bilangan X yang akan dipilih sesuai kehendak pengguna.
BilPrima = True                                  # Boolean, Set variabel awal berupa True

if (X > 1) :                                # If, Prasyarat bahwa sebuah bilangan prima harus berupa bilangan yang lebih dari 1.
    for i in range(2, X) :                                  # Loop, Fungsi pengulangan pada i dari 2 hingga X-1 (X tidak termasuk sehingga tidak berlaku pada pilihan angka X = 2).  
        if (X%i == 0) :                                   # If, Penentuan kondisi ketika X dapat dibagi sejumlah i dan menghasilkan bilangan bulat.
            BilPrima = False                                   # Indikator bahwa kondisi X dapat dibagi sejumlah i terpenuhi sehingga X bukan prima.
            break                                     # Loop diberhentikan.
        else :                                  # Else, ketika tidak memenuhi segala kondisi yang ditentukan.
            BilPrima = True                                    # Indikator bahwa kondisi X dapat dibagi i tidak terpenuhi.

    if (BilPrima == True or X == 2) :                      # Penentuan kondisi apabila X tidak dapat dibagi oleh semua i pada interval 2 hingga X-1 atau pilihan angka X = 2.
        print(X, "adalah bilangan prima")                      # Ouput, mencetak bahwa X bilangan prima karena memenuhi setidaknya salah satu kondisi.
    elif (BilPrima == False)  :                           # Penentuan kondisi ketika X bukan bilangan prima.
        print(X, "bukan bilangan prima")                       # Ouput, mencetak bahwa X bukan bilangan prima karena memenuhi kondisi False.                                                                     # Pemutusan fungsi pengulangan karena memenuhi kondisi.

else :                                            # Penentuan kondisi ketika X tidak lebih dari atau sama dengan 1.
    print(X, "bukan bilangan prima")                           # Ouput, mencetak bahwa X bukan ilangan prima karena memenuhi kondisi.
      


