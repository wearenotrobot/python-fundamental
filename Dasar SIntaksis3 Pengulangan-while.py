"""
pengulangan menggunakan while
"""
jumlah_buku = 10
print('ibu berkata: "Baca semua buku!"')

buku_yang_sudah_dibaca = 0
while buku_yang_sudah_dibaca < jumlah_buku:
    buku_yang_sudah_dibaca = buku_yang_sudah_dibaca + 1
    print(f'buku ke {buku_yang_sudah_dibaca} sudah dibaca')

print('\nlaporan kepada ibu:')
print(f'Jumlah buku yang sudah dibaca adalah {jumlah_buku}')