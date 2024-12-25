def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * hitung_faktorial(n-1)

def buat_dict_faktorial(n):
    dict_faktorial = {}
    for i in range(1, n+1):
        dict_faktorial[i] = hitung_faktorial(i)
    return dict_faktorial

def main():
    try:
        n = int(input("Masukkan bilangan bulat positif: "))
        if n <= 0:
            print("Mohon masukkan bilangan bulat positif!")
            return
            
        hasil = buat_dict_faktorial(n)
        print("\nHasil faktorial dari 1 sampai", n, "adalah:")
        for angka, faktorial in hasil.items():
            print(f"{angka}! = {faktorial}")
            
    except ValueError:
        print("Input tidak valid! Mohon masukkan bilangan bulat.")

if __name__ == "__main__":
    main()