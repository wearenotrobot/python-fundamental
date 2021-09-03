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

print('\nlist yang dinamis, dimana tipe data tiap elemen berbeda-beda')
daftar_buku = [12, 3.42, 'buletin']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan semua data buku dari awal:')
daftar_buku = ['kitabushollah', 'kitabushollati wannawafil', 'kitabulahkam', 'kitabuladab', 'kitabusshoum']
daftar_buku.append('kitabul janaiz')
print('kemudian tambahkan 1 buku baru')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nganti elemen pertama')
daftar_buku = ['kitabushollah', 'kitabushollati wannawafil', 'kitabulahkam', 'kitabuladab', 'kitabusshoum']
daftar_buku[0] = "kitabulda'wat"
print(daftar_buku)

print('\nganti elemen kedua dari belakang')
daftar_buku[-2] = 'kitabul jannah wannar'
print(daftar_buku)

print('\nAmbil elemen ke dua')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['kitabushollah', 'kitabushollati wannawafil', 'kitabulahkam', 'kitabuladab', 'kitabusshoum']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['kitabushollah', 'kitabushollati wannawafil', 'kitabulahkam', 'kitabuladab', 'kitabusshoum']
del daftar_buku[0:-2] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah list comprehension yang kedua')
daftar_buku = ['kitabushollah', 'kitabushollati wannawafil', 'kitabulahkam', 'kitabuladab', 'kitabusshoum']
del daftar_buku[0::3] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])