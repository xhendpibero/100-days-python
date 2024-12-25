import math

def eksplorasi_matematika():
    print("🔢 Program Eksplorasi Fungsi Matematika 🔢")
    
    # Meminta input dari pengguna
    try:
        angka = float(input("Masukkan sebuah angka: "))
        
        # Menghitung berbagai fungsi matematika
        print("\nHasil perhitungan:")
        print(f"✨ Nilai absolut: {abs(angka)}")
        print(f"✨ Pembulatan ke atas: {math.ceil(angka)}")
        print(f"✨ Pembulatan ke bawah: {math.floor(angka)}")
        print(f"✨ Akar kuadrat: {math.sqrt(abs(angka))}")
        print(f"✨ Pangkat dua: {pow(angka, 2)}")
        print(f"✨ Pangkat tiga: {pow(angka, 3)}")
        
        if angka > 0:
            print(f"✨ Logaritma natural: {math.log(angka)}")
            print(f"✨ Logaritma basis 10: {math.log10(angka)}")
        
        print(f"✨ Sinus: {math.sin(math.radians(angka))}")
        print(f"✨ Cosinus: {math.cos(math.radians(angka))}")
        print(f"✨ Tangen: {math.tan(math.radians(angka))}")
    except ValueError:
        print("Masukkan angka yang valid.")

eksplorasi_matematika()
