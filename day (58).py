class Hy:
    def __init__(self, *args):
        # Menyimpan argumen dalam tuple
        self.numbers = args
    
    def display(self):
        # Menginisialisasi variabel untuk menyimpan hasil penjumlahan
        total = 0
        # Iterasi setiap argumen
        for num in self.numbers:
            # Mengkonversi ke integer dan menambahkan ke total
            total += int(num)
        return total

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek dengan beberapa angka
    numbers = Hy(1, 2, 3, 4, 5)
    # Menampilkan hasil penjumlahan
    print(f"Jumlah: {numbers.display()}")  # Output: Jumlah: 15