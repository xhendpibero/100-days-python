class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Memanggil metode fare() dari kelas induk menggunakan super()
        base_fare = super().fare()
        # Menambahkan 10% maintenance charge
        return base_fare + (base_fare * 0.1)

# Membuat instance
bus = Bus("School Volvo", 50)

# Menampilkan hasil
print(f"Vehicle Fare: {Vehicle('Regular Car', 50).fare()}")
print(f"Bus Fare: {bus.fare()}")