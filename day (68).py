"""
🚗 Contoh Pemrograman Berorientasi Objek di Python 🐍

Pelajaran penting tentang inheritance (pewarisan) dan penggunaan super()

Konsep utama:
1️⃣ Base Class (Vehicle): Kelas dasar yang mendefinisikan atribut dasar kendaraan
2️⃣ Derived Class (Car): Kelas turunan yang mewarisi Vehicle
3️⃣ super(): Fungsi untuk mengakses method dari kelas induk
4️⃣ Method display(): Menampilkan semua atribut objek
"""

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display(self):
        return f"Kendaraan: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)  # Memanggil constructor kelas induk
        self.year = year
    
    def display(self):
        return f"{super().display()} Tahun: {self.year}"

# Contoh penggunaan
mobil = Car("Toyota", "Avanza", 2020)
print(mobil.display())  # Output: Kendaraan: Toyota Avanza Tahun: 2020