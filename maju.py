import random

def urutan_kelompok_acak(jumlah_kelompok, jumlah_per_sesi):
    kelompok = [f'Kelompok {i+1}' for i in range(jumlah_kelompok)]
    random.shuffle(kelompok)
    
    sesi = [kelompok[i:i + jumlah_per_sesi] for i in range(0, len(kelompok), jumlah_per_sesi)]
    return sesi

jumlah_kelompok = 12
jumlah_per_sesi = 3

sesi_acak = urutan_kelompok_acak(jumlah_kelompok, jumlah_per_sesi)

for i, sesi in enumerate(sesi_acak, start=1):
    print(f'Sesi {i}: {",".join(sesi)} yang pratik')