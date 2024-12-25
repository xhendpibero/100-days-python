class PythagoreanTriplet:
    def __init__(self, numbers):
        self.numbers = sorted(numbers)  # Mengurutkan angka dari kecil ke besar
    
    def is_triplet(self):
        # Memastikan ada tepat 3 angka
        if len(self.numbers) != 3:
            return False
            
        # Mengambil angka yang sudah diurutkan
        a, b, c = self.numbers
        
        # Memeriksa apakah memenuhi teorema Pythagoras
        return a*a + b*b == c*c

# Contoh penggunaan
def test_triplets():
    # Test case 1: Triplet Pythagoras yang valid (3,4,5)
    triplet1 = PythagoreanTriplet([3, 4, 5])
    print(f"[3, 4, 5] adalah triplet? {triplet1.is_triplet()}")  # True
    
    # Test case 2: Bukan triplet Pythagoras
    triplet2 = PythagoreanTriplet([5, 6, 7])
    print(f"[5, 6, 7] adalah triplet? {triplet2.is_triplet()}")  # False

if __name__ == "__main__":
    test_triplets()