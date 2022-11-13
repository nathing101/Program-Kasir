#opening
print('===================================================')
print('||                                               ||')
print('||       SELAMAT DATANG DI TOKO BOOKMEDIA        ||')
print('||                                               ||')
print('===================================================')

#mendeklarasikan nilai awal dengan array
barang = []
buku = [['NOVEL ='], ['KAMUS ='], ['MOTIVASI =']]
harga = []
total = 0

#membuat fungsi dengan logika perulangan
def barang1 ():
    for data0 in barang:
        print(data0)
        
def jenis_buku():
    for data1 in buku:
        print(data1)

def harga_barang():
    for data2 in harga:
        print(data2)

#logika perulangan, percabangan, perbandingan dan aritmatika
while True:
    print("""
                >>> Daftar Buku <<<\n
1. Matahari Minor               \t Rp  87.500
2. Kamus Al-Munawwir            \t Rp 191.000
3. Sagaras                      \t Rp  75.500
4. Berani Tidak Disukai         \t Rp  75.000
5. Selena                       \t Rp  85.000
6. Filosofi Teras               \t Rp  83.000
7. Kamus Bahasa Jepang          \t Rp 117.000
8. Laskar Pelangi               \t Rp  84.000
9. Atomic Habit                 \t Rp  81.000
10. Kamus Bahasa Prancis        \t Rp 102.000
    """)

    kode = (input('Masukkan pilihan buku anda : '))
    if kode == '1':
        barang.append('Matahari Minor')
        harga.append(87500)
        buku[0].append('Matahari Minor')
        total += 87500
    elif kode == '2':
        barang.append('Kamus Al-Munawwir')
        harga.append(191000)
        buku[1].append('Kamus Al-Munawwir')
        total += 191000
    elif kode == '3':
        barang.append('Sagaras')
        harga.append(75500)
        buku[0].append('Sagaras')
        total += 75500
    elif kode == '4':
        barang.append('Berani Tidak Disukai')
        harga.append(73500)
        buku[2].append('Berani Tidak Disukai')
        total += 73500
    elif kode == '5':
        barang.append('Selena')
        harga.append(85000)
        buku[0].append('Selena')
        total += 85000
    elif kode == '6':
        barang.append('Filosofi Teras')
        harga.append(83000)
        buku[2].append('Filosofi Teras')
        total += 83000
    elif kode == '7':
        barang.append('Kamus Bahasa Jepang')
        harga.append(117000)
        buku[1].append('Kamus Bahasa Jepang')
        total += 117000
    elif kode == '8':
        barang.append('Laskar Pelangi')
        harga.append(84000)
        buku[0].append('Laskar Pelangi')
        total += 84000
    elif kode == '9':
        barang.append('Atomic Habit')
        harga.append(81000)
        buku[2].append('Atomic Habit')
        total += 81000
    elif kode == '10':
        barang.append('Kamus Bahasa Prancis')
        harga.append(102000)
        buku[1].append('Kamus Bahasa Prancis')
        total += 102000
    else:
        print('Pilihan anda tidak valid!')

    lanjut = input('Lanjut Belanja ? (y/n) \t   : ')
    if lanjut == 'y':
        continue
    elif lanjut == 'n':
        print()
        break
    else:
        lanjut1 = input('Silahkan pilih (y/n) \t   : ')
        if lanjut1 == 'y':
            continue
        elif lanjut1 == 'n':
            break
        else:
            print('Pilihan anda tidak valid!')
            break

#pemanggilan fungsi
print()
print('# Barang yang anda beli : ')
barang1()
print()
print('# Jenis buku yang anda beli : ')
jenis_buku()
print()
print('# Harga barang : ')
harga_barang()
print()
print('# Total yang harus anda bayar \t: Rp', total, '\n')
print()

#logika kasir sederhana
uang = int(input('Masukkan uang pembayaran \t: Rp '))
if uang > total:
    print('Kembalian anda    \t\t: Rp', uang - total)
elif uang == total:
    print('Uang pas')
else:
    print('Uang anda kurang    \t\t: Rp', uang - total)
    print('Silahkan bayarkan lagi sejumlah : Rp', uang - total)

#outing
print()
print('===================================================')
print('||                                               ||')
print('||        TERIMAKASIH ATAS KUNJUNGAN ANDA        ||')
print('||   >>> KAMI TUNGGU KEDATANGANYA KEMBALI! <<<   ||')
print('||                                               ||')
print('===================================================')
print()
