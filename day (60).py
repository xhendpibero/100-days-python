# Contoh 1: Konversi list of tuples sederhana ke dictionary
pairs = [('apel', 5000), ('jeruk', 3000), ('mangga', 7000)]
buah_dict = dict(pairs)  # Mengkonversi ke dictionary

# Contoh 2: Menggunakan dict comprehension
# Note: Cara alternatif yang lebih ekspresif
buah_dict_2 = {nama: harga for nama, harga in pairs}

# Contoh 3: List of tuples dengan data yang lebih kompleks
data = [
    ('siswa1', {'nilai': 85, 'kelas': '10A'}),
    ('siswa2', {'nilai': 90, 'kelas': '10B'}),
]
siswa_dict = dict(data)  # Data nested juga bisa dikonversi

# Contoh 4: Menggunakan zip() untuk membuat tuples dari dua list terpisah
# Note: Sangat berguna ketika data berasal dari sumber yang berbeda
nama_buah = ['apel', 'jeruk', 'mangga']
harga_buah = [5000, 3000, 7000]
buah_dict_3 = dict(zip(nama_buah, harga_buah))

# Mencetak hasil untuk verifikasi
print("Dictionary dari pairs:", buah_dict)
print("Dictionary dengan comprehension:", buah_dict_2)
print("Dictionary nested:", siswa_dict)
print("Dictionary dari zip:", buah_dict_3)