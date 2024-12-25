def hitung_elemen(lst):
    # Kasus dasar: jika list kosong, return 0
    if not lst:
        return 0
    
    # Rekursi: hitung elemen pertama (1) + hitung sisa list
    return 1 + hitung_elemen(lst[1:])

# Contoh penggunaan
def main():
    # Beberapa test case
    test_list1 = [1, 2, 3, 4, 5]
    test_list2 = []
    test_list3 = ['a', 'b', 'c']
    
    print(f"Jumlah elemen dalam {test_list1}: {hitung_elemen(test_list1)}")
    print(f"Jumlah elemen dalam {test_list2}: {hitung_elemen(test_list2)}")
    print(f"Jumlah elemen dalam {test_list3}: {hitung_elemen(test_list3)}")

if __name__ == "__main__":
    main()
