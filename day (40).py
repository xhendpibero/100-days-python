# Cara 1: Menggunakan del statement
def hapus_dari_dict_cara1():
    # Membuat dictionary contoh
    dict_saya = {
        "nama": "Budi",
        "umur": 25,
        "kota": "Jakarta"
    }
    
    print("Dictionary awal:", dict_saya)
    
    # Menghapus key "nama"
    del dict_saya["nama"]
    
    print("Setelah menghapus key 'nama':", dict_saya)

# Cara 2: Menggunakan method pop()
def hapus_dari_dict_cara2():
    dict_saya = {
        "nama": "Budi",
        "umur": 25,
        "kota": "Jakarta"
    }
    
    print("Dictionary awal:", dict_saya)
    
    # Menghapus key "umur" dan mendapatkan nilainya
    nilai_yang_dihapus = dict_saya.pop("umur")
    
    print("Nilai yang dihapus:", nilai_yang_dihapus)
    print("Setelah menghapus key 'umur':", dict_saya)

# Cara 3: Menggunakan method popitem() (menghapus item terakhir)
def hapus_dari_dict_cara3():
    dict_saya = {
        "nama": "Budi",
        "umur": 25,
        "kota": "Jakarta"
    }
    
    print("Dictionary awal:", dict_saya)
    
    # Menghapus dan mendapatkan pasangan key-value terakhir
    item_terakhir = dict_saya.popitem()
    
    print("Item terakhir yang dihapus:", item_terakhir)
    print("Setelah menghapus item terakhir:", dict_saya)

# Menjalankan semua contoh
if __name__ == "__main__":
    print("Cara 1: Menggunakan del statement")
    hapus_dari_dict_cara1()
    print("\nCara 2: Menggunakan pop()")
    hapus_dari_dict_cara2()
    print("\nCara 3: Menggunakan popitem()")
    hapus_dari_dict_cara3()