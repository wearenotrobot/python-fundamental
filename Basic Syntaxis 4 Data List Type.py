"""
ini adalah tipe data list
"""

daftar_buku = ['kitabushollah', 'kitabushollati wannawafil', 'kitabulahkam', 'kitabuladab', 'kitabusshoum']
print('tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nproses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\ntampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nlist yang dinamis')
