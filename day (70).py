class Operation:
    def __init__(self):
        pass
    
    def count_occurrences(self, data):
        """Menghitung kemunculan setiap elemen dalam list/tuple"""
        return {item: data.count(item) for item in set(data)}
    
    def is_palindrome(self, num):
        """Mengecek apakah sebuah angka adalah palindrome"""
        return str(num) == str(num)[::-1]
    
    def is_armstrong(self, num):
        """Mengecek apakah sebuah angka adalah angka Armstrong"""
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        return num == sum
    
    def is_perfect_square(self, num):
        """Mengecek apakah sebuah angka adalah perfect square"""
        if num < 0:
            return False
        root = int(num ** 0.5)
        return root * root == num
    
    def is_divisible(self, num, divisor):
        """Mengecek apakah sebuah angka bisa dibagi habis oleh divisor"""
        return num % divisor == 0
    
    def sum_up_to(self, num):
        """Menghitung jumlah semua angka dari 1 sampai num"""
        return sum(range(1, num + 1))
    
    def check_sign(self, num):
        """Mengklasifikasikan angka sebagai positif atau negatif"""
        if num > 0:
            return "Positif"
        elif num < 0:
            return "Negatif"
        return "Nol"

# Catatan penggunaan:
"""
💡 Program ini menggunakan konsep OOP untuk menggabungkan berbagai operasi matematika:

🔢 Fungsi-fungsi yang tersedia:
- count_occurrences: Menghitung frekuensi elemen dalam list/tuple
- is_palindrome: Mengecek angka palindrome (mis: 121)
- is_armstrong: Verifikasi angka Armstrong (mis: 153 = 1³ + 5³ + 3³)
- is_perfect_square: Identifikasi perfect square (mis: 16 = 4²)
- is_divisible: Cek keterbagian dengan angka tertentu
- sum_up_to: Menghitung jumlah angka sampai batas tertentu
- check_sign: Klasifikasi angka positif/negatif

Contoh penggunaan:
op = Operation()
print(op.is_palindrome(121))  # True
print(op.is_armstrong(153))   # True
print(op.is_perfect_square(16))  # True
"""

op = Operation()
print(op.is_palindrome(121))  # True
print(op.is_armstrong(153))   # True
print(op.is_perfect_square(16))  # True