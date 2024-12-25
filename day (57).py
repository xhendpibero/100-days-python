def find_special_chars(text):
    special_chars = []
    
    for char in text:
        if not char.isalnum() and not char.isspace():
            special_chars.append(char)
            
    return special_chars

# Contoh penggunaan
text = "Hello! How are you? @#$%"
hasil = find_special_chars(text)
print("Karakter spesial yang ditemukan:", hasil)