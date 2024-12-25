def is_perfect_square(numbers):
    # Menggunakan lambda untuk mengecek apakah akar kuadrat bilangan adalah integer
    # dan filter untuk menyaring bilangan yang merupakan perfect square
    return list(filter(lambda x: (x ** 0.5).is_integer(), numbers))

# Contoh penggunaan
numbers = [4, 10, 16, 25, 30, 36, 40, 49, 64, 100]
hasil = is_perfect_square(numbers)
print(f"Bilangan yang merupakan perfect square: {hasil}")