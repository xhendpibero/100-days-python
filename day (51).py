def create_dictionary():
    dicto = {}  # Membuat dictionary kosong
    
    while True:
        key = input("Masukkan key (ketik 'stop' untuk berhenti): ")
        
        if key.lower() == 'stop':
            break
            
        value = input("Masukkan value: ")
        dicto[key] = value
    
    print("Dictionary yang dibuat:", dicto)
    return dicto

# Memanggil fungsi
if __name__ == "__main__":
    hasil = create_dictionary()