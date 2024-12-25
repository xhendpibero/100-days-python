class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def discounted_price(self, discount_percent):
        """Menghitung harga setelah diskon"""
        if not 0 <= discount_percent <= 100:
            return "Persentase diskon harus antara 0-100"
        discount = (discount_percent / 100) * self.price
        return self.price - discount

    def display_info(self):
        """Menampilkan informasi laptop"""
        return f"Brand: {self.brand}\nModel: {self.model}\nHarga: Rp{self.price:,.2f}"

def main():
    # Membuat instance laptop
    laptop1 = Laptop("Asus", "ROG Strix", 15000000)
    laptop2 = Laptop("Lenovo", "ThinkPad", 12000000)
    
    print("=== Kalkulator Diskon Laptop ===")
    print("\nLaptop 1:")
    print(laptop1.display_info())
    print("\nLaptop 2:")
    print(laptop2.display_info())
    
    try:
        diskon = float(input("\nMasukkan persentase diskon (0-100): "))
        print("\nHarga Setelah Diskon:")
        print(f"Laptop 1: Rp{laptop1.discounted_price(diskon):,.2f}")
        print(f"Laptop 2: Rp{laptop2.discounted_price(diskon):,.2f}")
    except ValueError:
        print("Mohon masukkan angka yang valid")

if __name__ == "__main__":
    main()