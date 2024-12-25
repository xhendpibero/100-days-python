def is_armstrong_number(num, power=None):
    # Jika power belum ditentukan, hitung jumlah digit
    if power is None:
        power = len(str(num))
    
    # Base case: jika num = 0, return 0
    if num == 0:
        return 0
    
    # Ambil digit terakhir dan pangkatkan
    last_digit = num % 10
    
    # Rekursi: panggil fungsi untuk sisa digit
    # dan tambahkan dengan digit terakhir yang dipangkatkan
    return (last_digit ** power) + is_armstrong_number(num // 10, power)

def check_armstrong(num):
    # Bandingkan hasil perhitungan dengan angka asli
    return num == is_armstrong_number(num)

# Contoh penggunaan
if __name__ == "__main__":
    test_numbers = [153, 370, 371, 407]
    
    for num in test_numbers:
        if check_armstrong(num):
            print(f"{num} adalah angka Armstrong")
        else:
            print(f"{num} bukan angka Armstrong")