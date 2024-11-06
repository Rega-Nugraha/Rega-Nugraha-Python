import random

# Daftar siswa
siswa = ['Adam', 'Aditya F', 'Aditya R', 'Agus', 'Alifia', 'Aliza', 'Annisa', 'Antonio', 'Aulia', 'Azka', 'Dafa', 'Farrel',
         'Fauzy', 'George', 'Hana', 'Hanifa', 'Helmi', 'Ibrah','Iqhwan','Miladdin', 'M Aliviyansyah', 'M Alvin', 'M Arka','M Rafael','M Seva', 'Mutya',
         'Natasya','Noval', 'Rasyah', 'Risqi', 'Rona', 'Salman','Shandika','Syalwa','Wahyu', 'Zulaika']

# Jumlah kelompok yang diinginkan
jumlah_kelompok = 12

# Acak daftar siswa
random.shuffle(siswa)

# Bagi siswa menjadi kelompok
kelompok = [siswa[i::jumlah_kelompok] for i in range(jumlah_kelompok)]

# Cetak hasil pembagian kelompok
for i, k in enumerate(kelompok, 1):
    print(f"Kelompok {i}: {', '.join(k)}")