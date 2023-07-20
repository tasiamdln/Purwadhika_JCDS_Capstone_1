# Tampungan seluruh buku
all_buku = [
        {"Book_ID":1001,
        "Title":"Sang Alkemis",
        "Genre":"Fiction",
        "Author":"Paulo Coelho",
        "Publisher":"Gramedia",
        "Tahun_Terbit":2018,
        "Stock":5
        },
        {"Book_ID":1002,
        "Title":"Summer In Seoul",
        "Genre":"Romance",
        "Author":"Ilana Tan",
        "Publisher":"Gramedia",
        "Tahun_Terbit":2014,
        "Stock":10
        },
        {"Book_ID":1003,
        "Title":"Origin",
        "Genre":"Fiction",
        "Author":"Dan Brown",
        "Publisher":"Doubleday",
        "Tahun_Terbit":2017,
        "Stock":3
         },
        {"Book_ID":1004,
        "Title":"Outliers",
        "Genre":"Psychology",
        "Author":"Malcolm Gladwell",
        "Publisher":"Penguin",
        "Tahun_Terbit":2018,
        "Stock":1
         }
]

# Menampilkan seluruh menu
def menu():
    print('''
Selamat datang di Anastasia Library System!
    Menu :
        1. Lihat Buku yang Tersedia
        2. Tambah Buku
        3. Update Buku
        4. Hapus Buku
        5. Peminjaman/Pengembalian Buku
        6. Exit''')


# Print Header Table Buku
def header ():
    print('Book_ID'.ljust(9," "),
          'Title'.ljust(20," "),
          'Genre'.ljust(15," "),
          'Author'.ljust(20," "),
          'Publisher'.ljust(15," "),
          'Tahun_Terbit'.ljust(15," "),
          'Stock'.ljust(10," "))

    
# Menampikan menu 1 : Read Menu

def read_list():
    for i in range(len(all_buku)) :
        print(str(all_buku[i]['Book_ID']).ljust(9," "),
              str(all_buku[i]['Title']).ljust(20," "),
              str(all_buku[i]['Genre']).ljust(15," "),
              str(all_buku[i]['Author']).ljust(20," "),
              str(all_buku[i]['Publisher']).ljust(15," "),
              str(all_buku[i]['Tahun_Terbit']).ljust(15," "),
              str(all_buku[i]['Stock']).ljust(10," ")
              )

def read_menu():
    while True:
        print()
        print('''Menu:
        1. Semua Buku
        2. Berdasarkan Judul Buku
        3. Berdasarkan BOOK ID
        4. Back''')
        pilihread = input("Masukkan menu yang kamu pilih: ")
        if pilihread == '1':
            if len(all_buku) == 0:
                print("Stock Buku Tidak Tersedia")
            else:
                print("Berikut adalah daftar Buku yang ada di Anastasia Library System!")
                header()
                read_list()

        elif pilihread == '2':
            injudul = input("Masukkan judul buku yang ingin kamu cari : ").title()
            is_read_title = 0
            for i in all_buku:
                if i["Title"] == injudul:
                    is_read_title = 1
                    print("Berikut adalah daftar Buku yang ada di Anastasia Library System!")  
                    header ()
                    print(str(i['Book_ID']).ljust(9," "),
                        str(i['Title']).ljust(20," "),
                        str(i['Genre']).ljust(15," "),
                        str(i['Author']).ljust(20," "),
                        str(i['Publisher']).ljust(15," "),
                        str(i['Tahun_Terbit']).ljust(15," "),
                        str(i['Stock']).ljust(10," ")
                        )
                    break
                else:
                    is_read_title = 0
            
            if is_read_title == 0:
                    print(f"Buku dengan judul:{injudul} tidak ditemukan")
                    
                    
        elif pilihread == '3':
            inBookID = int(input("Masukkan BOOK_ID yang ingin kamu cari : "))
            is_read_bookid = 0
            for i in all_buku:
                if i["Book_ID"] == inBookID:
                    is_read_bookid = 1
                    print("Berikut adalah daftar Buku yang ada di Anastasia Library System!")  
                    header ()
                    print(str(i['Book_ID']).ljust(9," "),
                        str(i['Title']).ljust(20," "),
                        str(i['Genre']).ljust(15," "),
                        str(i['Author']).ljust(20," "),
                        str(i['Publisher']).ljust(15," "),
                        str(i['Tahun_Terbit']).ljust(15," "),
                        str(i['Stock']).ljust(10," ")
                        )
                    break

                elif i["Book_ID"] != inBookID:
                    is_read_bookid = 0

            if is_read_bookid == 0:
                print("BOOK_ID tidak ditemukan")
        
        elif pilihread == '4':
            break
        
        else:
            print("Mohon masukkan angka menu dengan benar")


#fungsi cek duplikat
def cek_duplicate(buku,judul,penulis):
    for i in all_buku:
        if i["Book_ID"] == buku or i["Title"] == judul and i["Author"] == penulis:
            return "yes"


# Menampilkan menu 2 : Tambah Buku
def tambah_buku ():
    while True:
        print()
        print('''Menu
    1. Tambah Buku
    2. Back''')
        pilihtambah = input("Masukkan menu yang kamu pilih: ")
    
        if pilihtambah == '1':
            # Input penambahan buku
            inbook = int(input("Masukkan BOOK ID :"))
            intitle = input("Masukkan Title Buku :").title()
            inauthor = input("Masukkan Nama Penulis Buku :").title()
            if cek_duplicate(inbook,intitle,inauthor) == "yes":
                print("Data sudah ada")
                continue

            ingenre = input("Masukkan Genre Buku :").title()
            inpublisher = input("Masukkan Penerbit Buku :").title()
            intahun_terbit = int(input("Masukkan Tahun Terbit Buku :"))
            instock = int(input("Masukkan Stock Buku :"))

            # Jadi/ tidak disimpan
            print()
            header ()
            print(str(inbook).ljust(9," "),
                str(intitle).ljust(20," "),
                str(ingenre).ljust(15," "),
                str(inauthor).ljust(20," "),
                str(inpublisher).ljust(15," "),
                str(intahun_terbit).ljust(15," "),
                str(instock).ljust(10," ")
                )
            validasi_tambah = input("Apakah Anda yakin akan menyimpan (Y/N) ? ").upper()
            if validasi_tambah == "Y":
                # Penggabungan hasil inputan menjadi dict baru
                all_buku.append({
                    'Book_ID' : inbook,
                    'Title' : intitle,
                    'Genre' : ingenre,
                    'Author' : inauthor,
                    'Publisher' : inpublisher,
                    'Tahun_Terbit' : intahun_terbit,
                    'Stock' : instock})
                print("Buku telah berhasil ditambahkan")
                header()
                read_list()
                
            elif validasi_tambah == "N":
                print("Data tidak jadi disimpan")
                

        elif pilihtambah == '2':
            break

        else:
            print("Mohon masukkan angka menu dengan benar")


# Menampilkan menu 3 : Update Buku
def update_buku():
    while True:
        print(''' 
Menu
    1. Update Buku
    2. Back''')
        pilihupdate = input("Masukkan menu yang kamu pilih: ")

        if pilihupdate == '1':
            header()
            read_list()
            upbuku = int(input("Masukkan BOOK ID yang akan kamu ubah : "))
            print()
            is_upbuku = 0
            for i in all_buku:

                if i["Book_ID"] == upbuku :
                    is_upbuku = 1
                    while True:
                        header ()
                        print(str(i['Book_ID']).ljust(9," "),
                            str(i['Title']).ljust(20," "),
                            str(i['Genre']).ljust(15," "),
                            str(i['Author']).ljust(20," "),
                            str(i['Publisher']).ljust(15," "),
                            str(i['Tahun_Terbit']).ljust(15," "),
                            str(i['Stock']).ljust(10," "))
                        print('''
Menu Data Perubahan Buku
    1. Title
    2. Genre
    3. Author
    4. Publisher
    5. Tahun Terbit
    6. Stock
    7. Back''')
                        upinmenu = int(input("Masukkan Menu yang kamu pilih : "))
                        up_sementara = i

                        if upinmenu == 1:
                            uptilte = input("Masukkan Title Baru: ").title()
                            up_sementara['Title'] = uptilte
                        elif upinmenu == 2:
                            upgenre = input("Masukkan Genre Baru: ").title()
                            up_sementara['Genre'] = upgenre
                        elif upinmenu == 3:
                            upauthor = input("Masukkan Author Baru: ").title()
                            up_sementara['Author'] = upauthor
                        elif upinmenu == 4:
                            uppubliser = input("Masukkan Publisher Baru: ").title()
                            up_sementara['Publisher'] = uppubliser
                        elif upinmenu == 5:
                            uptahun_terbit = int(input("Masukkan Tahun Terbit Baru: "))
                            up_sementara['Tahun_Terbit'] = uptahun_terbit
                        elif upinmenu == 6:
                            upstock = int(input("Masukkan Stock Baru: "))
                            up_sementara['Stock'] = upstock
                        elif upinmenu == 7:
                            break


                        tambah_update = input(f"Apakah ada data lain yang ingin diubah pada BOOK_ID {upbuku}? (Y/N)").upper()
                        if tambah_update == "Y":
                            pass
                        elif tambah_update == "N":
                            header ()
                            up_sementara
                            print(str(upbuku).ljust(9," "),
                                str(up_sementara['Title']).ljust(20," "),
                                str(up_sementara['Genre']).ljust(15," "),
                                str(up_sementara['Author']).ljust(20," "),
                                str(up_sementara['Publisher']).ljust(15," "),
                                str(up_sementara['Tahun_Terbit']).ljust(15," "),
                                str(up_sementara['Stock']).ljust(10," "))
                            validasi_update = input("Apakah Anda yakin akan menyimpan data di atas (Y/N) ? ").upper()
                            if validasi_update == "Y":
                                i == up_sementara
                                print(f"Perubahan pada BOOK_ID{upbuku} berhsil disimpan")
                                header()
                                read_list()
                                break
                            elif validasi_update == "N":
                                continue
                                

                elif i["Book_ID"] != upbuku :
                    is_upbuku = 0
                    
            if is_upbuku == 0:
                print("Buku Tidak Ditemukan")

       
        elif pilihupdate == '2':
            break

        else:
            print("Mohon masukkan angka menu dengan benar")


# Menampilkan menu 4 : Hapus Buku 
def hapus_buku():
    while True:
        print(''' 
Menu
    1. Hapus Buku
    2. Back''')
        pilihhapus = input("Masukkan menu yang kamu pilih: ")


        if pilihhapus == '1':
            header()
            read_list()
            delbuku = int(input("Masukkan BOOK ID yang akan kamu hapus : "))
            print()
            is_delbuku_tersedia = 0
            for i in all_buku:


                if i["Book_ID"] == delbuku:
                    is_delbuku_tersedia = 1
                    header()
                    print(str(i['Book_ID']).ljust(9," "),
                            str(i['Title']).ljust(20," "),
                            str(i['Genre']).ljust(15," "),
                            str(i['Author']).ljust(20," "),
                            str(i['Publisher']).ljust(15," "),
                            str(i['Tahun_Terbit']).ljust(15," "),
                            str(i['Stock']).ljust(10," "))
                    validasi_delete = input("Apakah Anda yakin menghapus buku di atas? (Y/N)").upper()
                    if validasi_delete == "Y":
                        all_buku.remove(i)
                        print(f"Buku dengan Book ID:{delbuku} berhasil di hapus")
                        print()
                        print("Berikut Daftar Buku Terkini")
                        header()
                        read_list()   
                        break
                    elif validasi_delete == "N":
                        break


                elif i["Book_ID"] != delbuku:
                    is_delbuku_tersedia = 0

            if is_delbuku_tersedia == 0:
                print(f"Buku dengan Book ID {delbuku} tidak ditemukan")


        elif pilihhapus == '2':
            break

        else:
            print("Mohon masukkan angka menu dengan benar")


# Menampilkan menu 5 : Pinjam Buku

# validasi buku sudah dipinjam
def val_exist_in_chart(chart_list,book_id):
    is_exist=False
    if len(chart_list)==0:
        is_exist=False
    else:
        for i in chart_list:
            if i['Book_ID']==book_id:
                is_exist=True
                break
            else:
                is_exist=False
    return is_exist

#fungsi utama pinjam& pengembalian buku
def pinjam_buku ():
    while True :
        print('''
Menu Peminjaman/Pengembalian Buku
    1. Peminjaman Buku
    2. Pengembalian Buku
    3. Back
              ''')
        menu_pinjam = input("Masukkan menu yang kamu pilih: ")
        print()
        # Menu Peminjaman Buku
        if menu_pinjam == '1':
            jatah_pinjam = 0
            chart_pinjam = [] # {buku,title,dsb..,durasi,index_pinjam}
            while True:
                header()
                read_list()
                inpinjam = int(input("Masukkan BOOK ID yang ingin dipinjam : "))
                if val_exist_in_chart(chart_pinjam,inpinjam):
                    print(f"BOOK_ID {inpinjam} sudah masuk ke list pinjam")
                    continue
                else:
                    # ----
                    index_pinjam_counter = 0
                    is_buku_tersedia = 0
                    is_stock_tersedia = 1
                    for i in all_buku:
                        if i["Stock"] <= 0:
                            is_stock_tersedia = 0
                            break
                        
                        elif i['Book_ID'] == inpinjam  :
                            is_buku_tersedia = 1
                            chart_pinjam.append(i)
                            chart_pinjam[jatah_pinjam]["Index_Pinjam"] = index_pinjam_counter
                            break
                                
                        elif i['Book_ID'] != inpinjam : 
                            is_buku_tersedia = 0
                        index_pinjam_counter += 1
                    if is_stock_tersedia==0:
                        print("Stock Tidak Cukup")
                    elif is_buku_tersedia == 0:
                        print("Book ID tidak ditemukan") 

                    else:
                        print('''
    Durasi Peminjaman Buku :
        1 : 3 hari
        2 : 7 hari
        3 : 14 hari
                            ''')
                        indurasi_pinjam = int(input("Pilih durasi peminjaman buku (1/2/3): "))
                        if indurasi_pinjam == 1:
                            durasi_pinjam = "3 hari"
                        elif indurasi_pinjam == 2:
                            durasi_pinjam = "7 hari"
                        elif indurasi_pinjam == 3:
                            durasi_pinjam = "14 hari"

                        
                        chart_pinjam[jatah_pinjam]["Durasi"] = durasi_pinjam
                        jatah_pinjam += 1
                    # ----
                

                # Validasi tambah buku lagi, max pinjam 3 buku
                val_tambah_chart = input("Apakah ingin meminjam buku lain? (Y/N)").upper()
                print()
                if val_tambah_chart == "Y":
                    if jatah_pinjam == 3:
                        print("Jumlah buku yang dipinjam sudah mencapai maximal : 3 buku")
                        break
                elif val_tambah_chart == "N": 
                    break

            #showing chart_pinjam
            print() 
            print('Book_ID'.ljust(9," "),
                'Title'.ljust(20," "),
                'Genre'.ljust(15," "),
                'Author'.ljust(20," "),
                'Publisher'.ljust(15," "),
                'Tahun_Terbit'.ljust(15," "),
                'Durasi'.ljust(10," ")
                )
            for i in range(len(chart_pinjam)) :
                print(str(chart_pinjam[i]['Book_ID']).ljust(9," "),
                    str(chart_pinjam[i]['Title']).ljust(20," "),
                    str(chart_pinjam[i]['Genre']).ljust(15," "),
                    str(chart_pinjam[i]['Author']).ljust(20," "),
                    str(chart_pinjam[i]['Publisher']).ljust(15," "),
                    str(chart_pinjam[i]['Tahun_Terbit']).ljust(15," "),
                    str(chart_pinjam[i]['Durasi']).ljust(10," ")
                    )
            
            validasi_pinjam = input("Apakah Anda yakin meminjam buku di atas? (Y/N)").upper()
            if validasi_pinjam == "Y":
            # Mengurangi stock buku yang dipinjam
                for i in chart_pinjam :
                    all_buku[i["Index_Pinjam"]]['Stock'] = all_buku[i["Index_Pinjam"]]['Stock'] - 1
                print("Buku berhasil dipinjam")
                continue
                
                    
            elif validasi_pinjam == "N":
                print("Peminjaman buku dibatalkan") 
                continue
        
        # Menu Pengembalian Buku        
        elif menu_pinjam == '2': #ingin tambahkan tgl pengembalian buku
            inbalik = int(input("Masukkan BOOK ID yang akan dikembalikan: "))
            is_buku_dipinjam = 0
            for i in chart_pinjam :
                if i['Book_ID'] == inbalik:
                    is_buku_dipinjam = 1
                    all_buku[i["Index_Pinjam"]]['Stock'] = all_buku[i["Index_Pinjam"]]['Stock'] + 1
                    print(f"Buku dengan BOOK_ID:{inbalik} berhasil dikembalikan")
                    chart_pinjam.remove(i)
                    break
                    
                elif i['Book_ID'] != inbalik :
                    is_buku_dipinjam = 0
                    
            if is_buku_dipinjam == 0:
                print("Kamu tidak meminjam BOOK ID tersebut")
                pass
        

        elif menu_pinjam == '3':
            break
        else :
            print("Mohon masukkan angka menu dengan benar")
                     

# Flow Besar Aplikasi
while True:
    menu()
    pilih_menu = input("Silakan input menu yang kamu pilih:")
    if pilih_menu.isnumeric() == True:
        pilih_menu = int(pilih_menu)
        if pilih_menu == 1:
            read_menu()
        elif pilih_menu == 2:
            tambah_buku()
        elif pilih_menu == 3:
            update_buku()
        elif pilih_menu == 4:
            hapus_buku()
        elif pilih_menu == 5:
            pinjam_buku()
        elif pilih_menu == 6:
            print("Terima kasih telah mengakses Anastasia Library System!")
            break
        else:
            print("Menu yang kamu pilih tidak tersedia")
    else:
        print("Mohon pilih menu dalam bentuk angka")
