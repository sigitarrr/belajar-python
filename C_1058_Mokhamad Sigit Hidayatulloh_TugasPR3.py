#toko suka slipknot
produk = {
    "Gitar Stratocaster Red": 13000,
    "Ampli Marshall": 20000,
    "Kak Zaidan Gaming": 7000,
    "Paket Umroh Bersama Mas Adya": 25000,
}

keranjang = []

print("=== SELAMAT DATANG DI TOKO SUKA SLIPKNOT ===")
print("Daftar Produk:")

i = 1
for nama, harga in produk.items():
    print(f"{i}. {nama}, Rp{harga}")
    i += 1

while True:
    print("\nPilihan menu:")
    print("1. Tambah barang ke keranjang")
    print("2. Selesaikan pembelian / Checkout")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        print("\nPilih barang yang ingin dibeli:")
        i = 1
        for nama, harga in produk.items():
            print(f"{i}. {nama}, Rp{harga}")
            i += 1
            
        nomor_produk = int(input("Masukkan nomor barang: "))
       
        nama_barang = ""
        posisi = 1
        for nama in produk:
            if posisi == nomor_produk:
                nama_barang = nama
                break
            posisi += 1
            
        jumlah = int(input(f"Masukkan jumlah {nama_barang}: "))
        
        harga_satuan = produk[nama_barang]
        subtotal_item = harga_satuan * jumlah
        
        keranjang.append({
            "nama": nama_barang,
            "harga": harga_satuan,
            "jumlah": jumlah,
            "subtotal_item": subtotal_item
        })
        print(f"-> {nama_barang} (x{jumlah}) berhasil ditambahkan!")
            
    elif pilihan == "2":
        break

subtotal = 0
for item in keranjang:
    subtotal += item["subtotal_item"]

ppn = int(subtotal * 0.11)
biaya_layanan = 15000
total_bayar = subtotal + ppn + biaya_layanan

print("\n===== STRUK BELANJA =====")
for item in keranjang:
    print(f"{item['nama']} x {item['jumlah']} = Rp{item['subtotal_item']}")

print("-----------------------------")
print(f"Subtotal   : Rp{subtotal}")
print(f"PPN (11%)  : Rp{ppn}")
print(f"Ongkir     : Rp{biaya_layanan}")
print("-----------------------------")
print(f"Total Bayar: Rp{total_bayar}")
print("Terima kasih telah berbelanja di toko Ejak")


#Two Sum 
nums = [5, 11, 7, 15, 21,]
target = 20

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"index yang cocok dengan {target} adalah index ke- {i} dan index ke-{j}")
            break
        

#Monitoring Latihan Gym Tajamok
jumlah_hari = int(input("Masukkan jumlah hari latihan: "))

for hari in range(1, jumlah_hari + 1):
    for sesi in range(1, 6):
        print(f"Hari ke-{hari}, Sesi ke-{sesi}")

    print(f"Hari ke-{hari} selesai!")

    if hari == 7:
        print("Sudah setengah jalan!")

    if hari == 14:
        print("Selesai!")