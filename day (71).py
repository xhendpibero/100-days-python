def filter_numbers(mixed_list):
    # Filter hanya nilai numerik (int dan float)
    numbers = [x for x in mixed_list if isinstance(x, (int, float))]
    return numbers

# Contoh penggunaan
test_list = [1, 'abc', 3.14, 'xyz', 5, True, 2.5]
hasil = filter_numbers(test_list)
print("Nilai numerik:", hasil)

# Penjelasan kode:
# Fungsi filter_numbers menerima list campuran sebagai input
# Menggunakan list comprehension dengan isinstance() untuk memeriksa tipe data
# isinstance(x, (int, float)) memeriksa apakah item adalah integer atau float
# Mengembalikan list baru yang hanya berisi nilai numerik
# Anda juga bisa menambahkan penanganan untuk nilai boolean (karena True = 1 dan False = 0 dalam Python) dengan memodifikasi kondisi pengecekan jika diperlukan.
# Contoh output:
# 💡 Tips: Gunakan isinstance() daripada type() untuk pengecekan tipe data karena lebih fleksibel dalam menangani subclass dan multiple types.

# Nilai numerik: [1, 3.14, 5, 2.5]