class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.isbn = ""
    
    def input_data(self):
        self.title = input("Masukkan judul buku: ")
        self.author = input("Masukkan nama pengarang: ")
        self.isbn = input("Masukkan nomor ISBN: ")
    
    def tampilkan_info(self):
        print("\nInformasi Buku:")
        print(f"Judul: {self.title}")
        print(f"Pengarang: {self.author}") 
        print(f"ISBN: {self.isbn}")

# Contoh penggunaan
if __name__ == "__main__":
    buku = Book()
    buku.input_data()
    buku.tampilkan_info()