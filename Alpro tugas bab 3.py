# Harga dasar pizza
Harga_pizza = 50000

# Tampilkan topping dan pilih topping
print("Selamat Datang di Restoran Pizza\nPilih topping Pizza")
print("1. Original Frankfurter BBQ")
print("2. Meast monsta")
print("3. Super supreme")
print("4. Super supreme chiken")
print("5. Meat lovers")
print("6. Chiken lovers")
print("7. Cheese lovers")
print("8. American fauvorite")

pilihan_topping = int(input("Masukkan pilihan topping : "))

# proses pemberian harga sesuai topping yang di pilih
if pilihan_topping == 1:
    topping = "Original Frankfurter BBQ"
    Harga_topping = 10000
elif pilihan_topping == 2:
    topping = "Meast monsta"
    Harga_topping = 10000
elif pilihan_topping == 3:
    topping = "Super supreme"
    Harga_topping = 10000
elif pilihan_topping == 4:
    topping = "Super supreme chiken"
    Harga_topping = 10000
elif pilihan_topping == 5:
    topping = "Meat lovers"
    Harga_topping = 10000
elif pilihan_topping == 6:
    topping = "Chiken lovers"
    Harga_topping = 10000
elif pilihan_topping == 7:
    topping = "Cheese lovers"
    Harga_topping = 10000
elif pilihan_topping == 8:
    topping = "American fauvorite"
    Harga_topping = 10000
else:
    print("Topping tidak valid, menggunakan default topping original")
    topping = "Original Frankfurter BBQ"
    Harga_topping = 10000

# Tampilkan crust dan Pilih jenis crust
print("\nPilih jenis crust:")
print("1. Thin Crust - Rp5000")
print("2. Thick Crust - Rp7000")
crust_pilihan = input("Masukkan nomor crust yang diinginkan (1/2): ")

# Proses pemberian harga crust
if crust_pilihan == "1":
    crust = "Thin Crust"
    harga_crust = 5000
elif crust_pilihan == "2":
    crust = "Thick Crust"
    harga_crust = 7000
else:
    print("Crust tidak valid, menggunakan default thin crust")
    crust = "Thin Crust"
    harga_crust = 5000

# Tampilkan dan Pilih ukuran pizza
print("\nPilih ukuran pizza:")
print("1. Kecil - Rp5000")
print("2. Sedang - Rp10000")
print("3. Besar - Rp15000")
ukuran_pilihan = input("Masukkan nomor ukuran yang diinginkan (1/2/3): ")

# Proses pemberian harga sesuai ukuran yang di pilih
if ukuran_pilihan == "1":
    ukuran = "Kecil"
    harga_ukuran = 5000
elif ukuran_pilihan == "2":
    ukuran = "Sedang"
    harga_ukuran = 10000
elif ukuran_pilihan == "3":
    ukuran = "Besar"
    harga_ukuran = 15000
else:
    print("Ukuran tidak valid.menggunakan default ukuran sedang")
    ukuran = "Sedang"
    harga_ukuran = 10000
    

# Memilih Tambahan keju
print("\nApakah Anda ingin menambahkan keju ekstra?")
keju_pilihan = input("Tambahkan keju ekstra (ya/tidak): ").lower()

# Tambahan harga jika iya
if keju_pilihan == "ya":
    harga_keju = 5000
    keju = "Tambahan keju"

# tidak ada tambahan harga jika tidak 
else:
    harga_keju = 0
    keju = "Tidak ada tambahan keju"

# Hitung total harga pesanan
total_harga = Harga_pizza + Harga_topping + harga_crust + harga_ukuran + harga_keju

# proses transaksi
print("Total harga: Rp", total_harga)
Uang_pelanggan= int(input("masukan nominal uang yang diberikan pelanggan : "))
kembalian= Uang_pelanggan-total_harga

#Tampilkan struk pembelian
print("=============================================")
print(" Toko Pizza MI enakk")
print(" jl. ketintang barat daya, No. 3 ")
print("=============================================")
print("\nRingkasan Pesanan Anda:")
print("Topping: ", topping)
print("Crust: ", crust)
print("Ukuran: ", ukuran)
print("Keju: ", keju)
print("=============================================")
print("Total harga: Rp", total_harga)
print("Nominal Uang pelanggan: Rp", Uang_pelanggan)
print("Nominal Kembalian : Rp", kembalian)
print("=============================================")
print("Terima kasih atas orderannya, selamat menikmati")




