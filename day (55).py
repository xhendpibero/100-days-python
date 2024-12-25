import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def hitung_luas(self):
        return math.pi * (self.radius ** 2)
    
    def hitung_keliling(self):
        return 2 * math.pi * self.radius

# Contoh penggunaan
if __name__ == "__main__":
    lingkaran = Circle(7)
    print(f"Luas lingkaran: {lingkaran.hitung_luas():.2f}")
    print(f"Keliling lingkaran: {lingkaran.hitung_keliling():.2f}")