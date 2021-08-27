"""
semua sintaksis dasar bahasa pemrograman terdiri dari 3 langkah ini :
1. Sekuensial : langkah berurutan
2. Percabangan: langkah melompat jika terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali sapai kondisi terpenuhi
"""

# Sekuensial
print('ibu bilang: "pergi ke toko, belikan telor"')  # print itu perintah menulis teks
print('Budi menjawab: "baik bu, apa yang harus saya beli?"')
print('Ibu berkata: beli susu 1 Liter, jika ada telur beli 6"')
print('Maka Budi berangkat ke toko')
print('dan mulai berbelanja')

# Percabangan
milk_bottle_count = 17
egg_count = 53
print(f'\njumlah susu {milk_bottle_count} botol')
print(f'jumlah telur {egg_count} butir')
if milk_bottle_count > 0:
    print('\nBudi mengecek harganya, ternyata uangnya cukup')
    print('maka Budi membeli 1 botol susu')
    if egg_count > 0:
        print("dan membeli 6 telur")
    else:
        print('Budi hanya membeli 1 botol susu')
else:
    print('\nBudi tidak jadi membeli 1 botol susu')

print('\nBudi pulang kerumah dan menyerahkan susunya kepada ibu')