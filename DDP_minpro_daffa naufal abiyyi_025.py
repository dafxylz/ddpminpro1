print("Selamat Datang di koperasi Merah Putih")
jenis = ("Kecil", "Sedang", "Besar")
jumlah = (1000000, 3000000, 5000000)

pinjaman = []

while True:
    print("\nmenu pilihan")
    print("1. Pilih Pinjaman")
    print("2. Ubah Pinjaman")
    print("3. Bayar Pinjaman")
    print("4. Lihat Pinjaman")
    print("5. Keluar")

    menu = input("Pilih: ")

    if menu == "1":
        print("\n1.", jenis[0], "- Rp", jumlah[0])
        print("2.", jenis[1], "- Rp", jumlah[1])
        print("3.", jenis[2], "- Rp", jumlah[2])

        pilih = int(input("Pilih pinjaman: ")) - 1
        pinjaman.append([jenis[pilih], jumlah[pilih], 0])

        print("Pinjaman berhasil dibuat!")

    elif menu == "2":
        if pinjaman:
            baru = int(input("Masukkan jumlah pinjaman baru: "))
            pinjaman[0][1] = baru
            print("Pinjaman berhasil diubah!")
        else:
            print("Belum ada pinjaman.")

    elif menu == "3":
        if pinjaman:
            bayar = int(input("Masukkan jumlah pembayaran: "))
            pinjaman[0][2] += bayar
            print("Pembayaran berhasil!")
        else:
            print("Belum ada pinjaman.")

    elif menu == "4":
        if pinjaman:
            print("\nJenis    :", pinjaman[0][0])
            print("Pinjaman : Rp", pinjaman[0][1])
            print("Dibayar  : Rp", pinjaman[0][2])
            print("Sisa     : Rp", pinjaman[0][1] - pinjaman[0][2])
        else:
            print("Belum ada pinjaman.")

    elif menu == "5":
        print("Terimakasih telah meminjam di koperasi Merah Putih")
        break

    else:
        print("Pilihan tidak ada, silahkan pilih kembali.")

