import csv
import os

# Nama file CSV untuk menyimpan data
FILE_NAME = "catatan_pengeluaran.csv"

# Fungsi untuk membuat file CSV jika belum ada
def buat_file_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Deskripsi", "Jumlah"])
        print(f"File '{FILE_NAME}' berhasil dibuat.")

# Fungsi untuk menambahkan pengeluaran
def tambah_pengeluaran():
    tanggal = input("Masukkan tanggal (format: YYYY-MM-DD): ")
    deskripsi = input("Masukkan deskripsi pengeluaran: ")
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, deskripsi, jumlah])

    print("Pengeluaran berhasil ditambahkan!")

# Fungsi untuk menampilkan semua pengeluaran
def tampilkan_pengeluaran():
    if not os.path.exists(FILE_NAME):
        print("Belum ada catatan pengeluaran.")
        return
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Lewati header
        total = 0
        print("\nDaftar Pengeluaran:")
        print("-" * 40)
        for row in reader:
            print(f"Tanggal: {row[0]}, Deskripsi: {row[1]}, Jumlah: Rp {float(row[2]):,.2f}")
            total += float(row[2])
        print("-" * 40)
        print(f"Total Pengeluaran: Rp {total:,.2f}\n")

# Fungsi untuk menghitung total pengeluaran
def hitung_total_pengeluaran():
    if not os.path.exists(FILE_NAME):
        print("Belum ada catatan pengeluaran.")
        return
    
    total = 0
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Lewati header
        for row in reader:
            total += float(row[2])

    print(f"Total Pengeluaran Anda: Rp {total:,.2f}")

# Fungsi untuk menghapus pengeluaran berdasarkan tanggal atau deskripsi
def hapus_pengeluaran():
    if not os.path.exists(FILE_NAME):
        print("Belum ada catatan pengeluaran.")
        return

    print("\nPilih cara penghapusan pengeluaran:")
    print("1. Berdasarkan Tanggal")
    print("2. Berdasarkan Deskripsi")
    pilihan = input("Pilih menu (1/2): ")
    
    rows = []
    found = False
    
    if pilihan == '1':  # Hapus berdasarkan tanggal
        tanggal_hapus = input("Masukkan tanggal pengeluaran yang ingin dihapus (format: YYYY-MM-DD): ")
        
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Menyimpan header
            rows.append(header)
            for row in reader:
                if row[0] != tanggal_hapus:
                    rows.append(row)
                else:
                    found = True
        
        if found:
            with open(FILE_NAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Pengeluaran dengan tanggal {tanggal_hapus} berhasil dihapus.")
        else:
            print(f"Tidak ada pengeluaran dengan tanggal {tanggal_hapus}.")
    
    elif pilihan == '2':  # Hapus berdasarkan deskripsi
        deskripsi_hapus = input("Masukkan deskripsi pengeluaran yang ingin dihapus: ")
        
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Menyimpan header
            rows.append(header)
            for row in reader:
                if row[1] != deskripsi_hapus:
                    rows.append(row)
                else:
                    found = True
        
        if found:
            with open(FILE_NAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Pengeluaran dengan deskripsi '{deskripsi_hapus}' berhasil dihapus.")
        else:
            print(f"Tidak ada pengeluaran dengan deskripsi '{deskripsi_hapus}'.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== Aplikasi Catatan Pengeluaran ===")
    print("1. Tambah Pengeluaran")
    print("2. Tampilkan Pengeluaran")
    print("3. Hitung Total Pengeluaran")
    print("4. Hapus Pengeluaran")
    print("5. Keluar")

def main():
    buat_file_csv()
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            tambah_pengeluaran()
        elif pilihan == '2':
            tampilkan_pengeluaran()
        elif pilihan == '3':
            hitung_total_pengeluaran()
        elif pilihan == '4':
            hapus_pengeluaran()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
