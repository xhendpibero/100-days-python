# Dictionary bersarang untuk menyimpan nilai siswa
student_marks = {
    "Budi": {
        "Matematika": 85,
        "Bahasa": 78,
        "IPA": 90
    },
    "Ani": {
        "Matematika": 92,
        "Bahasa": 88,
        "IPA": 85
    }
}

def get_student_mark(name, subject):
    # Memeriksa apakah nama siswa ada dalam dictionary
    if name in student_marks:
        # Memeriksa apakah mata pelajaran ada untuk siswa tersebut
        if subject in student_marks[name]:
            return student_marks[name][subject]
        else:
            return f"Mata pelajaran {subject} tidak ditemukan"
    else:
        return f"Siswa {name} tidak ditemukan"

# Program utama
def main():
    # Meminta input dari pengguna
    nama = input("Masukkan nama siswa: ")
    mapel = input("Masukkan mata pelajaran: ")
    
    # Mendapatkan dan menampilkan nilai
    hasil = get_student_mark(nama, mapel)
    print(f"Nilai {nama} untuk {mapel}: {hasil}")

if __name__ == "__main__":
    main()