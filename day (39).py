def extract_alphabets(input_string):
    # Menggunakan list comprehension untuk mengambil hanya karakter alfabet
    result = ''.join(char for char in input_string if char.isalpha())
    return result

# Test program
def main():
    # Meminta input dari pengguna
    input_string = input("Masukkan string: ")
    
    # Memanggil fungsi untuk mengekstrak alfabet
    result = extract_alphabets(input_string)
    
    # Menampilkan hasil
    print("String yang hanya berisi alfabet:", result)

if __name__ == "__main__":
    main()