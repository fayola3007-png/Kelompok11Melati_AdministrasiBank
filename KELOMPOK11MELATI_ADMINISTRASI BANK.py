# ===============================
#       SISTEM ADMIN BANK
# ===============================

# List menampung nasabah
nasabah_awal = []
# List riwayat transaksi
riwayat = []

#fungsi mencari nasabah
def cari_nasabah(no_rek):
    no_rek = str(no_rek)

    if no_rek.strip() == "":
        print("Nomor rekening tidak boleh kosong!")
        return None

    if not no_rek.isdigit():
        print("Nomor rekening harus berupa ANGKA!")
        return None

    if len(no_rek) != 13:
        print("Nomor rekening harus 13 digit!")
        return None

    for n in nasabah_awal:
        if n["no_rek"] == no_rek:
            return n

    print("Nomor rekening tidak ditemukan!")
    return None


# create
def tambah_nasabah():
    print("--- Tambah Nasabah ---")

    # Input no rekening
    while True:
        no_rek = input("Masukkan No Rekening (13 digit): ")
        if no_rek.strip() == "":
            print("Nomor rekening tidak boleh kosong!")
            continue
        if not no_rek.isdigit():
            print("Nomor rekening harus berupa ANGKA!")
            continue
        if len(no_rek) != 13:
            print("Nomor rekening harus 13 digit!")
            continue
        break

    while True:
        nama = input("Masukkan nama Nasabah: ").strip()
        if nama == "":
            print("Nama tidak boleh kosong!")
        else:
            break
    while True:
        saldo = input("Masukkan saldo awal (min 50000): ")

        if not saldo.isdigit():
            print("Saldo harus berupa angka dan tidak boleh negatif!")
            continue

        saldo = int(saldo)

        if saldo < 50000:
            print("Saldo harus minimal 50.000!")
            continue

        break

    data = {"no_rek": no_rek, "nama": nama, "saldo": saldo}
    nasabah_awal.append(data)

    riwayat.append(f"Nasabah baru: {nama}, Rek: {no_rek}, Saldo awal {saldo}")
    print("Nasabah berhasil ditambahkan!")
    


# read
def tampilkan_nasabah():
    print ("--- Daftar Nasabah ---")
    if len(nasabah_awal) == 0:
        print("Belum ada data nasabah.")
    else:
        for n in nasabah_awal:
            print(f"{n['no_rek']} | {n['nama']} | Saldo: {n['saldo']}")

# Update 
def update_saldo():
    print("--- Update saldo nasabah ---")
    while True:
        no = input("Masukkan No Rekening: ")
        if not no.isdigit():
            print("Nomor rekening harus berupa angka!")
            continue
        no = int(no)
        break

    nasabah = cari_nasabah(no)

    if not nasabah:
        ("Nasabah tidak ditemukan!")
        return
    
    print("1. Tambah saldo")
    print("2. Kurangi saldo")

    while True:
        pilih = input("Pilih: ")
        if pilih not in ["1", "2"]:
            print("pilihan hanya No 1 atau 2!")
            continue
        break
    while True:
        jumlah = input("Jumlah: ")

        if not jumlah.isdigit():
            print("Jumlah harus berupa angka dan tidak boleh negatif!")
            continue

        jumlah = int(jumlah)

        if jumlah <= 0 and jumlah >= 50000:
            print("Jumlah harus lebih dari nol(0)!")
            continue
        break

    if pilih == "1":
        nasabah["saldo"] += jumlah
        riwayat.append(f"Tambah saldo + {jumlah} ke rek {no}")
        print("Saldo Berhasil ditambahkan!")

    else:
        if nasabah["saldo"] < jumlah:
            print("Saldo tidak cukup untuk dikurangi!")
            return
        nasabah["saldo"] -= jumlah
        riwayat.append(f"kurangi saldo -{jumlah} dari rek {no}")
        print("Saldo berhasil diperbarui!")
  
# delete
def hapus_nasabah():
    print("--- Hapus Nasabah ---")
    print("1. Hapus berdasarkan No Rekening")
    print("2. Hapus berdasarkan Nama")

    while True:
        pilih = input("Pilih: ")

        if pilih not in ["1", "2"]:
            print("Pilihan hanya 1 atau 2")
            continue
        break

    if pilih == "1":
        while True:
            no = input("Masukkan No Rekening: ")
            if not no.isdigit():
                print("Rekening harus berupa angka!")
            no = int(no)
            break

        nasabah = cari_nasabah(no)

        if nasabah:
            nasabah_awal.remove(nasabah)
            riwayat.append(f"Nasabah Rek {no} dihapus")
            print("Nasabah berhasil dihapus!")
        else:
            print("No rekening nasabah tidak ditemukan!")
    else:
        while True:
            nama = input("Masukkan nama nasabah: ").strip()
            if nama == "":
                print("Nama tidak boleh kosong!")
                continue
            break

        ditemukan = None

        for n in nasabah_awal:
            if n["nama"].lower() == nama.lower():
                ditemukan = n
                break

        if ditemukan is None:
            print("Nama nasabah tidak ditemukan!")
        else:
            nasabah_awal.remove(ditemukan)
            print("Nasabah berhasil dihapus!")


# saldo terbanyak
def saldo_terbanyak():
    print("--- Nasabah dengan Saldo Terbesar ---")

    if len(nasabah_awal) == 0:
        print("Belum ada nasabah.")
        return

    # cari saldo terbesar
    terbesar = max(nasabah_awal, key=lambda x: x["saldo"])

    print(f"Rek: {terbesar['no_rek']} | Nama: {terbesar['nama']} | Saldo: {terbesar['saldo']}")

# tarik tunai
   

# transfer
def transfer():
    print("---Transfer Antar Nasabah ---")
    
    # INPUT REKENING PENGIRIM
    while True:
        rek_asal = input("Rek Pengirim: ")
        if not rek_asal.isdigit():
            print("Nomor rekening harus berupa angka!")
            continue
        break
    
    # INPUT REKENING PENERIMA
    while True:
        rek_dituju = input("Rek Penerima: ")
        if not rek_dituju.isdigit():
            print("Nomor rekening harus berupa angka!")
            continue
        break

    if rek_asal == rek_dituju:
        print("Tidak bisa transfer ke rekening sendiri!")
        return

    # PENTING → Kirim string, bukan int
    A = cari_nasabah(rek_asal)
    B = cari_nasabah(rek_dituju)

    if A and B:
        while True:
            jumlah = input("Jumlah transfer: ")
            if not jumlah.isdigit():
                print("Jumlah harus berupa angka!")
                continue
            jumlah = int(jumlah)
            break

        if A["saldo"] >= jumlah:
            A["saldo"] -= jumlah
            B["saldo"] += jumlah

            riwayat.append(f"Transfer {jumlah} dari {rek_asal} ke {rek_dituju}")
            print("Transfer berhasil!")
        else:
            print("Saldo pengirim tidak cukup!")
    else:
        print("Rekening tidak ditemukan!")


# cari nasabah
def cari_data():
    print("--- Cari Nasabah ---")
    password = input("Masukkan no rekening: ")

    benar = False
    for n in nasabah_awal:
        if password == n["no_rek"]:
            print(f"{n['no_rek']} | {n['nama']} | saldo: {n['saldo']}")
            benar = True

    if not benar:
        print("Data tidak ditemukan!")


# exit
def keluar():
    print("Keluar dari sistem bank. Terima kasih!")
    return False


while True:
    print("***** MENU ADMIN BANK *****")
    print("1. Tambah Nasabah")
    print("2. Lihat semua nasabah")
    print("3. Update  saldo manual")
    print("4. Hapus nasabah")
    print("5. Nasabah dengan saldo terbanyak")
    print("6. Transfer antar nasabah lain")
    print("7. Cari Nasabah")
    print("8. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_nasabah()
    elif pilih == "2":
        tampilkan_nasabah()
    elif pilih == "3":
        update_saldo()
    elif pilih == "4":
        hapus_nasabah()
    elif pilih == "5":
        saldo_terbanyak()
    elif pilih == "6":
        transfer()
    elif pilih == "7":
        cari_data()
    elif pilih == "8":
        keluar()
        break
    else:
        print("Pilihan tidak valid!")
    