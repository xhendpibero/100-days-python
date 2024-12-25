# Contoh penggunaan pop() pada dictionary Python

# Membuat dictionary dengan data mahasiswa
mahasiswa = {
    'nama': 'Budi Santoso',
    'umur': 20,
    'jurusan': 'Informatika',
    'semester': 3,
    'ipk': 3.75
}

print("Dictionary awal:", mahasiswa)

# Menggunakan pop() untuk menghapus dan mendapatkan nilai
umur = mahasiswa.pop('umur')
print("\nNilai yang dihapus (umur):", umur)
print("Dictionary setelah menghapus umur:", mahasiswa)

# Menggunakan pop() dengan nilai default
# Jika key tidak ditemukan, akan mengembalikan nilai default
nilai_hobi = mahasiswa.pop('hobi', 'Key tidak ditemukan')
print("\nMencoba pop key yang tidak ada:", nilai_hobi)

# Contoh error handling saat menggunakan pop()
try:
    nilai_error = mahasiswa.pop('alamat')  # Key yang tidak ada tanpa nilai default
except KeyError as e:
    print("\nError: Key tidak ditemukan dalam dictionary")

# Menghapus beberapa item sekaligus
mahasiswa.pop('semester')
mahasiswa.pop('ipk')
print("\nDictionary final:", mahasiswa)
