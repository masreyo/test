from os import system


dataUser = [
    {"Username": "admin", "Password": "admin123", "Role": "admin"},
    {"Username": "user", "Password": "user123", "Role": "user"}
]

barangList = [
    {"Nama": "Barang 1", "Harga": 10000},
    {"Nama": "Barang 2", "Harga": 20000},
    {"Nama": "Barang 3", "Harga": 30000}
]

historyPembeli = []
komplainList = []


# Fungsi untuk login
def login():
    while True:
        system('cls')
        print(("═")*64)
        print((" ")*5+"██╗      ██████╗  ██████╗ ██╗███╗   ██╗")
        print((" ")*5+"██║     ██╔═══██╗██╔════╝ ██║████╗  ██║")
        print((" ")*5+"██║     ██║   ██║██║  ███╗██║██╔██╗ ██║")
        print((" ")*5+"██║     ██║   ██║██║   ██║██║██║╚██╗██║")
        print((" ")*5+"███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║")
        print((" ")*5+"╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝")
        print((" ")*5+"                                       ")
        print((" ")*5+" █████╗ ██████╗ ██████╗ ████████╗  ██╗   ██╗   ██╗██████╗ ")
        print((" ")*5+"██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██║   ██║   ██║╚════██╗")
        print((" ")*5+"███████║██████╔╝██████╔╝   ██║     ██║   ██║   ██║ █████╔╝")
        print((" ")*5+"██╔══██║██╔═══╝ ██╔═══╝    ██║██   ██║   ╚██╗ ██╔╝██╔═══╝ ")
        print((" ")*5+"██║  ██║██║     ██║        ██║╚█████╔╝    ╚████╔╝ ███████╗")
        print((" ")*5+"╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝ ╚════╝      ╚═══╝  ╚══════╝ ")
        print(("═")*64)
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        user = None
        for data in dataUser:
            if data["Username"] == username and data["Password"] == password:
                user = data
                break
        
        if user is not None:
            return user
        else:
            print("Username atau password salah. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menampilkan daftar barang
def tampilkan_barang():
    system('cls')
    print("\n=== Daftar Barang ===")
    for i, barang in enumerate(barangList):
        print(f"ID Barang: {i+1}")
        print(f"Nama Barang: {barang['Nama']}")
        print(f"Harga Barang: {barang['Harga']}")
        print("=====================")
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menambah barang
def tambah_barang():
    system('cls')
    print("\n=== Tambah Barang ===")
    nama = input("Masukkan nama barang: ")
    harga_input = input("Masukkan harga barang: ")
    try:
        harga = int(harga_input)
        barangList.append({"Nama": nama, "Harga": harga})
        print("Barang berhasil ditambahkan.")
    except ValueError:
        print("Inputan harga barang harus berupa angka.")
    input("Tekan Enter untuk melanjutkan...")



# Fungsi untuk menghapus barang
def hapus_barang():
    system('cls')
    print("\n=== Hapus Barang ===")
    id_barang = int(input("Masukkan ID Barang yang akan dihapus: "))
    if id_barang >= 1 and id_barang <= len(barangList):
        del barangList[id_barang - 1]
        print("Barang berhasil dihapus.")
    else:
        print("ID Barang tidak valid.")
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menampilkan riwayat pembelian
def tampilkan_riwayat_pembelian():
    system('cls')
    print("\n=== Riwayat Pembelian ===")
    if len(historyPembeli) > 0:
        for pembeli in historyPembeli:
            print("Nama Pembeli:", pembeli["Nama Pembeli"])
            print("Barang yang Dibeli:")
            for barang in pembeli["Barang Dibeli"]:
                print("- Nama Barang:", barang["Nama"])
                print("- Harga Barang:", barang["Harga"])
            print("=====================")
    else:
        print("Tidak ada riwayat pembelian.")
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menampilkan komplain pengguna
def tampilkan_komplain_admin():
    system('cls')
    print("\n=== Komplain Pengguna ===")
    if len(komplainList) > 0:
        for komplain in komplainList:
            print("Nama Pembeli:", komplain["Nama Pembeli"])
            print("Komplain:", komplain["Komplain"])
            print("=====================")
    else:
        print("Tidak ada komplain dari pengguna.")
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk komplain
def komplain(user):
    system('cls')
    print("\n=== Komplain ===")
    komplain = input("Masukkan komplain Anda: ")
    user["Komplain"] = komplain
    komplainList.append({"Nama Pembeli": user["Nama Pembeli"], "Komplain": komplain})
    print("Komplain berhasil diajukan.")
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk pembelian barang
def pembelian_barang(user):
    system('cls')
    print("\n=== Pembelian Barang ===")
    tampilkan_barang()
    id_barang_input = input("Masukkan ID Barang yang ingin dibeli: ")
    try:
        id_barang = int(id_barang_input)
        if id_barang >= 1 and id_barang <= len(barangList):
            barang = barangList[id_barang - 1]
            nama_pembeli = user["Username"]
            harga = barang["Harga"]
            if "Nama Pembeli" not in user:
                user["Nama Pembeli"] = input("Masukkan nama lengkap Anda: ")
            if "Barang Dibeli" not in user:
                user["Barang Dibeli"] = []
            user["Barang Dibeli"].append({"Nama": barang["Nama"], "Harga": harga})
            historyPembeli.append({"Nama Pembeli": nama_pembeli, "Barang Dibeli": user["Barang Dibeli"]})
            print("Barang berhasil dibeli.")
        else:
            print("ID Barang tidak valid.")
    except ValueError:
        print("Inputan ID Barang harus berupa angka.")
    input("Tekan Enter untuk melanjutkan...")



# Fungsi untuk pembayaran
def pembayaran(user):
    system('cls')
    print("\n=== Pembayaran ===")
    if "Barang Dibeli" in user:
        total_harga = 0
        for barang in user["Barang Dibeli"]:
            total_harga += barang["Harga"]
        
        print("Total Harga: ", total_harga)
        print("Pembayaran berhasil.")
        user.pop("Barang Dibeli")
    else:
        print("Anda belum melakukan pembelian.")
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menu admin
def menu_admin():
    while True:
        print('')
        system('cls')
        print(("═")*50)
        print((" ")*6+"███╗   ███╗███████╗███╗   ██╗██╗   ██╗")
        print((" ")*6+"████╗ ████║██╔════╝████╗  ██║██║   ██║")
        print((" ")*6+"██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║")
        print((" ")*6+"██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║")
        print((" ")*6+"██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝")
        print((" ")*6+"╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ")
        print((" ")*5+"                                      ")
        print((" ")*5+" █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗")
        print((" ")*5+"██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║")
        print((" ")*5+"███████║██║  ██║██╔████╔██║██║██╔██╗ ██║")
        print((" ")*5+"██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║")
        print((" ")*5+"██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║")
        print((" ")*5+"╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝")
        print(("═")*50)
        print("\n=== Menu Admin ===")
        print("1. Tampilkan Barang")
        print("2. Tambah Barang")
        print("3. Hapus Barang")
        print("4. Tampilkan Riwayat Pembelian")
        print("5. Tampilkan Komplain")
        print("6. Logout")
        
        pilihan = input("Masukkan pilihan (1-6): ")
        
        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            hapus_barang()
        elif pilihan == "4":
            tampilkan_riwayat_pembelian()
        elif pilihan == "5":
            tampilkan_komplain_admin()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menu pengguna
def menu_pengguna(user):
    while True:
        system('cls')
        print("\n=== Menu Pengguna ===")
        print(("═")*50)
        print((" ")*6+"███╗   ███╗███████╗███╗   ██╗██╗   ██╗")
        print((" ")*6+"████╗ ████║██╔════╝████╗  ██║██║   ██║")
        print((" ")*6+"██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║")
        print((" ")*6+"██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║")
        print((" ")*6+"██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝")
        print((" ")*6+"╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ")
        print((" ")*5+"                                      ")
        print((" ")*8+"██╗   ██╗███████╗███████╗██████╗ ")
        print((" ")*8+"██║   ██║██╔════╝██╔════╝██╔══██╗")
        print((" ")*8+"██║   ██║███████╗█████╗  ██████╔╝")
        print((" ")*8+"██║   ██║╚════██║██╔══╝  ██╔══██╗")
        print((" ")*8+"╚██████╔╝███████║███████╗██║  ██║")
        print((" ")*8+" ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝")
        print(("═")*50)
        print("1. Tampilkan Barang")
        print("2. Pembelian Barang")
        print("3. Pembayaran")
        print("4. Komplain")
        print("5. Logout")
        
        pilihan = input("Masukkan pilihan (1-5): ")
        
        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            pembelian_barang(user)
        elif pilihan == "3":
            pembayaran(user)
        elif pilihan == "4":
            komplain(user)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")


# Main program
while True:
    system('cls')
    print("\n=== Aplikasi Penjualan ===")
    print(("═")*64)
    print((" ")*5+" █████╗ ██████╗ ██████╗ ████████╗  ██╗   ██╗   ██╗██████╗ ")
    print((" ")*5+"██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██║   ██║   ██║╚════██╗")
    print((" ")*5+"███████║██████╔╝██████╔╝   ██║     ██║   ██║   ██║ █████╔╝")
    print((" ")*5+"██╔══██║██╔═══╝ ██╔═══╝    ██║██   ██║   ╚██╗ ██╔╝██╔═══╝ ")
    print((" ")*5+"██║  ██║██║     ██║        ██║╚█████╔╝    ╚████╔╝ ███████╗")
    print((" ")*5+"╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝ ╚════╝      ╚═══╝  ╚══════╝ ")
    print(("═")*64)
    print("1. Login")
    print("2. Keluar")
    
    pilihan = input("Masukkan pilihan (1-2): ")
    
    if pilihan == "1":
        user = login()
        if user["Role"] == "admin":
            menu_admin()
        elif user["Role"] == "user":
            menu_pengguna(user)
    elif pilihan == "2":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
