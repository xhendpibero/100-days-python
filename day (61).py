# Dictionary untuk menyimpan nama siswa dan nilai
nilai_siswa = {
    "Budi": 85,
    "Ani": 90,
    "Doni": 75,
    "Siti": 95
}

# Fungsi untuk memperbarui nilai siswa
def update_nilai(nama, nilai_baru):
    if nama in nilai_siswa:
        nilai_siswa[nama] = nilai_baru
        print(f"Nilai {nama} telah diperbarui menjadi {nilai_baru}")
    else:
        print(f"Siswa {nama} tidak ditemukan")

# Fungsi untuk menambah siswa baru
def tambah_siswa(nama, nilai):
    nilai_siswa[nama] = nilai
    print(f"Siswa baru {nama} dengan nilai {nilai} telah ditambahkan")

# Fungsi untuk menghitung rata-rata nilai
def hitung_rata_rata():
    if len(nilai_siswa) > 0:
        total = sum(nilai_siswa.values())
        rata_rata = total / len(nilai_siswa)
        return rata_rata
    return 0

# Contoh penggunaan
print("Data nilai awal:", nilai_siswa)

# Memperbarui nilai siswa
update_nilai("Budi", 88)

# Menambah siswa baru
tambah_siswa("Rini", 82)

# Menampilkan rata-rata nilai
rata_rata = hitung_rata_rata()
print(f"\nRata-rata nilai seluruh siswa: {rata_rata:.2f}")
print("\nData nilai akhir:", nilai_siswa)

