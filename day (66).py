class Book:
    def __init__(self, title):
        self.title = title
    
    def show_title(self):
        print(f"Judul buku: {self.title}")

class EBook(Book):
    def __init__(self, title, file_size):
        super().__init__(title)
        self.file_size = file_size
    
    def show_file_size(self):
        print(f"Ukuran file: {self.file_size} MB")

# Contoh penggunaan
buku_fisik = Book("Python untuk Pemula")
buku_fisik.show_title()

ebook = EBook("Python untuk Pemula 2", 5.2)
ebook.show_title()  # Mewarisi method dari class Book
ebook.show_file_size()