def list_to_tuple():
    while True:
        # Meminta input jumlah elemen dari user
        n = int(input("Masukkan jumlah elemen yang ingin ditambahkan: "))
        
        # Membuat list kosong untuk menyimpan elemen
        listo = []
        
        # Loop untuk mengumpulkan input elemen
        print("Masukkan elemen-elemen:")
        for i in range(n):
            elem = input(f"Elemen ke-{i+1}: ")
            listo.append(elem)
        
        # Mengkonversi list menjadi tuple
        hasil_tuple = tuple(listo)
        
        # Menampilkan hasil
        print("\nList:", listo)
        print("Tuple:", hasil_tuple)
        
        # Tanya user apakah ingin melanjutkan
        lanjut = input("\nKetik 'Y' untuk melanjutkan atau tombol lain untuk berhenti: ")
        if lanjut.upper() != 'Y':
            break

# Menjalankan fungsi
if __name__ == "__main__":
    print("Program Konversi List ke Tuple")
    list_to_tuple()
