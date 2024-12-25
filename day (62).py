class A:
    def __init__(self, name, age, alpha):
        # Atribut publik
        self.name = name    # Bisa diakses langsung dari luar kelas
        self.age = age      # Bisa diakses langsung dari luar kelas
        
        # Atribut private 
        self.__alpha = alpha  # Hanya bisa diakses dari dalam kelas
    
    # Getter method untuk mengakses atribut private
    def get_alpha(self):
        return self.__alpha
    
    # Setter method untuk mengubah atribut private
    def set_alpha(self, new_alpha):
        self.__alpha = new_alpha

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek dari kelas A
    obj = A("Budi", 25, 100)
    
    # Mengakses atribut publik
    print(f"Nama: {obj.name}")  # Output: Nama: Budi
    print(f"Umur: {obj.age}")   # Output: Umur: 25
    
    # Mengakses atribut private menggunakan getter
    print(f"Alpha: {obj.get_alpha()}")  # Output: Alpha: 100
    
    # Mengubah nilai atribut private menggunakan setter
    obj.set_alpha(200)
    print(f"Alpha baru: {obj.get_alpha()}")  # Output: Alpha baru: 200