def print_unique_tuples():
    # Contoh list dengan tuple yang memiliki beberapa duplikat
    tuple_list = [
        (1, 2, 3),
        (4, 5, 6),
        (1, 2, 3),
        (7, 8, 9),
        (4, 5, 6),
        (10, 11, 12)
    ]
    
    # Menggunakan set() untuk menghilangkan duplikat
    # Set hanya akan menyimpan nilai unik
    unique_tuples = list(set(tuple_list))
    
    # Mencetak hasil
    print("List asli:")
    print(tuple_list)
    print("\nTuple unik setelah menghapus duplikat:")
    print(unique_tuples)

# Memanggil fungsi
if __name__ == "__main__":
    print_unique_tuples()
