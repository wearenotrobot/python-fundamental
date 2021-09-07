print('\nPerintah del dengan list comprehension')
daftar_buku = ['1 kitabushollah', '2 kitabushollati wannawafil', '3 kitabulahkam', '4 kitabuladab', '5 kitabusshoum']
del daftar_buku[:]  # start:end ini artinya semuanya di delete
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['1 kitabushollah', '2 kitabushollati wannawafil', '3 kitabulahkam', '4 kitabuladab', '5 kitabusshoum']
del daftar_buku[0:2]  # start:end, index mulai dari nol, tapi nilai mulai dr 1
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i]) # yang di del adalah no 1 dan 2

print('\nPerintah del dgn list comprehension yang kedua')
daftar_buku = ['1 kitabushollah', '2 kitabushollati wannawafil', '3 kitabulahkam', '4 kitabuladab', '5 kitabusshoum']
del daftar_buku[0:-2]  # start:end, mulai dari belakang, maka yg dihapus adalah yg dari awal sampai minus tsb.
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i]) # maka yg di delete adalah 'kitabushollah', 'kitabushollati wannawafil, 'kitabulahkam'

print('\nPerintah delete dgn list comprehension yang ketiga')
daftar_buku = ['1 kitabushollah', '2 kitabushollati wannawafil', '3 kitabulahkam', '4 kitabuladab', '5 kitabusshoum']
del daftar_buku[0::2]  # start:end:step, membuat list baru dari list yg sdh ada
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i]) # artinnya 'kitabushollati wannawafil' dan 'kitabuladab' di lewat, tidak di delete.

print('\nMembuat daftar list baru dengan comprehension: genap')
daftar_buku = ['1 kitabushollah', '2 kitabushollati wannawafil', '3 kitabulahkam', '4 kitabuladab', '5 kitabusshoum']
daftar_buku_baru = daftar_buku[1::2]  # start stop end. tujuannya untuk mengambil,
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i]) # mengambil mulai dari nilai 2, indexnya mulai dari 1.

print('\nMembuat daftar list baru dengan comprehension: ganjil')
daftar_buku = ['1 kitabushollah', '2 kitabushollati wannawafil', '3 kitabulahkam', '4 kitabuladab', '5 kitabusshoum']
daftar_buku_baru = daftar_buku[0::2]  # start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i]) # mengambil mulai dari nilai 1, indexnya mulai dari 0.