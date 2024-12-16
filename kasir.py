# Fungsi untuk menghitung total harga
def hitung_total(barang):
    total = 0
    for item in barang:
        total += item['harga'] * item['jumlah']
    return total

# Fungsi untuk menampilkan daftar belanja
def tampilkan_daftar(barang):
    print("\nDaftar Belanja:")
    print("{:<15} {:<10} {:<10} {:<10}".format('Nama Barang', 'Harga', 'Jumlah', 'Subtotal'))
    print("-" * 45)
    for item in barang:
        subtotal = item['harga'] * item['jumlah']
        print("{:<15} {:<10} {:<10} {:<10}".format(item['nama'], item['harga'], item['jumlah'], subtotal))

# Fungsi utama untuk menjalankan kasir
def main():
    barang = []
    while True:
        nama_barang = input("Masukkan nama barang (atau ketik 'selesai' untuk keluar): ")
        
        if nama_barang.lower() == 'selesai':
            break
        
        try:
            harga_barang = float(input("Masukkan harga barang: Rp. "))
            jumlah_barang = int(input("Masukkan jumlah barang: "))
        except ValueError:
            print("Masukkan harga dan jumlah dengan benar!")
            continue
        
        barang.append({
            'nama': nama_barang,
            'harga': harga_barang,
            'jumlah': jumlah_barang
        })
    
    # Menampilkan daftar belanja
    tampilkan_daftar(barang)
    
    # Menghitung dan menampilkan total harga
    total = hitung_total(barang)
    print("\nTotal Pembayaran: Rp. {:.2f}".format(total))

    # Menanyakan apakah ada diskon atau tidak
    diskon = input("Apakah ada diskon? (y/n): ").lower()
    if diskon == 'y':
        persen_diskon = float(input("Masukkan persentase diskon: "))
        total_diskon = total * (persen_diskon / 100)
        total -= total_diskon
        print("Diskon: Rp. {:.2f}".format(total_diskon))
    
    print("Total yang harus dibayar: Rp. {:.2f}".format(total))

# Menjalankan program kasir
if __name__ == "__main__":
    main()