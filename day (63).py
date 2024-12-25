class BankAccount:
    def __init__(self, nama_pemilik, saldo_awal=0):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo_awal
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            return f"Berhasil menyetor Rp{jumlah:,}. Saldo sekarang: Rp{self.saldo:,}"
        return "Jumlah setoran harus lebih dari 0"
    
    def tarik(self, jumlah):
        if jumlah > 0:
            if self.saldo >= jumlah:
                self.saldo -= jumlah
                return f"Berhasil menarik Rp{jumlah:,}. Saldo sekarang: Rp{self.saldo:,}"
            return "Saldo tidak mencukupi"
        return "Jumlah penarikan harus lebih dari 0"
    
    def cek_saldo(self):
        return f"Saldo {self.nama_pemilik}: Rp{self.saldo:,}"

# Contoh penggunaan
if __name__ == "__main__":
    rekening = BankAccount("Budi", 1000000)
    print(rekening.cek_saldo())
    print(rekening.setor(500000))
    print(rekening.tarik(300000))


# Penjelasan kode di atas:
# 1. __init__: Konstruktor untuk membuat objek rekening baru dengan nama pemilik dan saldo awal
# setor(): Method untuk menambah saldo dengan validasi jumlah harus positif
# tarik(): Method untuk menarik uang dengan validasi saldo mencukupi
# 4. cek_saldo(): Method untuk melihat saldo terkini
# Fitur-fitur yang diimplementasikan:
# ✅ Validasi input untuk setoran dan penarikan
# ✅ Pengecekan saldo sebelum penarikan
# ✅ Format angka menggunakan pemisah ribuan
# ✅ Pesan status untuk setiap transaksi
# Anda bisa mengembangkan lebih lanjut dengan menambahkan fitur seperti:
# Riwayat transaksi
# Transfer antar rekening
# Perhitungan bunga
# PIN untuk keamanan