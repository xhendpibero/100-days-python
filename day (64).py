import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def hitung_luas(self):
        luas = math.pi * self.radius ** 2
        return luas
    
    def hitung_keliling(self):
        keliling = 2 * math.pi * self.radius
        return keliling
    
    def tampilkan_info(self):
        print(f"Lingkaran dengan radius: {self.radius}")
        print(f"Luas: {self.hitung_luas():.2f}")
        print(f"Keliling: {self.hitung_keliling():.2f}")

# Contoh penggunaan
if __name__ == "__main__":
    lingkaran = Circle(5)
    lingkaran.tampilkan_info()