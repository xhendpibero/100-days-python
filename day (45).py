def hitung_kemunculan(daftar):
    # Membuat dictionary kosong untuk menyimpan hasil
    hasil = {}
    
    # Menghitung kemunculan setiap elemen
    for elemen in daftar:
        if elemen in hasil:
            hasil[elemen] += 1
        else:
            hasil[elemen] = 1
            
    return hasil

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh list 1: List dengan angka
    angka = [1, 2, 3, 2, 4, 1, 5, 2, 3, 1]
    print("List angka:", angka)
    hasil_angka = hitung_kemunculan(angka)
    print("Kemunculan setiap angka:", hasil_angka)
    
    print("\n" + "="*50 + "\n")
    
    # Contoh list 2: List dengan string
    buah = ["apel", "jeruk", "apel", "mangga", "jeruk", "apel"]
    print("List buah:", buah)
    hasil_buah = hitung_kemunculan(buah)
    print("Kemunculan setiap buah:", hasil_buah)
