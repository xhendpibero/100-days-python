"""
Menjelajahi Inheritance (Pewarisan) di Python!

Di Python, inheritance adalah konsep yang powerful yang memungkinkan kita membuat 
hubungan antar class. Berikut contoh yang mendemonstrasikan inheritance dengan
class Person sebagai base class dan Student class yang memperluas fungsionalitasnya.

💡 Poin-poin Penting:
1️⃣ super(): Method ini digunakan untuk memanggil method __init__() dari parent class,
   memastikan atribut dari base class diinisialisasi dengan benar.
2️⃣ Reusability: Student class mewarisi properti dari Person class, membuat kode
   lebih bersih dan dapat digunakan kembali.
3️⃣ Extensibility: Anda dapat mengembangkan Student class lebih lanjut untuk menambahkan
   atribut atau method khusus student tanpa memodifikasi Person class.
"""

# Base/Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Nama: {self.name}, Umur: {self.age}"

# Child class yang mewarisi dari Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Memanggil constructor parent class
        self.student_id = student_id
    
    def display_info(self):
        return f"{super().display_info()}, NIM: {self.student_id}"

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat instance Person
    person = Person("Budi", 30)
    print(person.display_info())
    
    # Membuat instance Student
    student = Student("Ani", 20, "12345")
    print(student.display_info())