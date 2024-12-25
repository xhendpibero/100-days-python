def dict_to_list(dictionary):
    """
    Fungsi untuk mengkonversi dictionary menjadi list of tuples
    Parameter: dictionary - dictionary yang akan dikonversi
    Return: list of tuples berisi pasangan (key, value)
    """
    return list(dictionary.items())

# Contoh penggunaan
dicto = {'d': 45, 'y': 65, 'z': 789}
hasil = dict_to_list(dicto)
print(f"Dictionary awal: {dicto}")
print(f"Hasil konversi: {hasil}")

def dict_to_list_alt(dictionary):
    """
    Alternatif menggunakan list comprehension
    """
    return [(key, value) for key, value in dictionary.items()]