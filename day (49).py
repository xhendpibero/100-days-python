def add_dictionaries(dict1, dict2):
    """
    Menjumlahkan nilai dari dua dictionary dengan key yang sama
    """
    result = {}
    
    # Mengambil semua key unik dari kedua dictionary
    all_keys = set(dict1.keys()) | set(dict2.keys())
    
    # Menjumlahkan nilai untuk setiap key
    for key in all_keys:
        result[key] = dict1.get(key, 0) + dict2.get(key, 0)
    
    return result

# Contoh penggunaan
if __name__ == "__main__":
    # Dictionary pertama
    dict1 = {
        'a': 100,
        'b': 200,
        'c': 300
    }
    
    # Dictionary kedua
    dict2 = {
        'a': 300,
        'b': 200,
        'd': 400
    }
    
    # Menjalankan fungsi
    hasil = add_dictionaries(dict1, dict2)
    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)
    print("Hasil Penjumlahan:", hasil)

