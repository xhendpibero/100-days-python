# Membuat dictionary kosong untuk menyimpan data buah
fruit_inventory = {}

def add_fruit(name, quantity):
    """
    Fungsi untuk menambahkan buah ke dalam inventory
    """
    if name in fruit_inventory:
        fruit_inventory[name] += quantity
    else:
        fruit_inventory[name] = quantity
    print(f"Berhasil menambahkan {quantity} {name}")

def display_inventory():
    """
    Fungsi untuk menampilkan semua buah dalam inventory
    """
    if not fruit_inventory:
        print("Inventory kosong!")
        return
    
    print("\nDaftar Buah dalam Inventory:")
    print("-" * 30)
    for fruit, qty in fruit_inventory.items():
        print(f"{fruit}: {qty} buah")
    print("-" * 30)

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah buah")
    print("2. Lihat inventory")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == "1":
        nama_buah = input("Masukkan nama buah: ")
        try:
            jumlah = int(input("Masukkan jumlah: "))
            add_fruit(nama_buah, jumlah)
        except ValueError:
            print("Jumlah harus berupa angka!")
            
    elif pilihan == "2":
        display_inventory()
        
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini!")
        break
        
    else:
        print("Pilihan tidak valid!")
