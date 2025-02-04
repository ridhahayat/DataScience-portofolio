set_aku = {'Avengers', 'hulk', 'iron man 3', 'wonder women', 'batman'}
set_kamu = {'Avengers', 'hulk', 'iron man 2', 'superman', 'wonder women'}

set_suka = set_aku.intersection(set_kamu)
set_kesamaan = (len(set_suka)) / (len(set_aku)) *100

print(f'Kesukaan Film kalian yang sama sebesar {set_kesamaan}%')

#=============================================================================


# list_buah = getFromDatabase();

# def printBuah()
#     for i, buah in enumerate(list_buah):
#         print(i, buah['Nama'], buah['Stock'], buah['Harga'])    

list_buah = [
            {'Nama' : 'Apel', 'Stock' : 20, 'Harga' : 10000},
            {'Nama' : 'Jeruk', 'Stock' : 15, 'Harga': 15000},
            {'Nama' : 'Anggur', 'Stock' : 25, 'Harga' : 20000}
        ]
list_keranjang = [] #container kosong untuk nampung list 'Nama', 'Qty', 'Harga', 'Total Harga'

# Step 1 Bikin Menunya Looping
while True: #Mengulang program list menu
    print("\tSelamat Datang di Pasar Buah")
    print()
    print("list Menu: ")
    print('\n1. Menampilkan Daftar Buah' '\n2. Menambah Buah' '\n3. Menghapus Buah' '\n4. Membeli Buah' '\n5. Exit Program')
    
    menu = int(input("Masukkan angka Menu yang ingin dijalankan : "))

    # jika menu 1
    # maka print (sudah masuk menu 1)
    # if menu == 5:
    #     break

# Step 2 Bikin Print untuk setiap Menu
    if menu == 1:
        print("Daftar Buah")
        print("Index | Nama | Stock | Harga")

        for i, buah  in enumerate(list_buah): #enumerate untuk memilih index buah, i = key, buah = value
            print(i, buah['Nama'], buah['Stock'], buah['Harga'])


# Step 3 bikin Print untuk memasukan nama buah yang mau ditambah
    elif menu == 2:
       nama_buah = input('Masukkan Nama Buah: ' )
       stock = int(input('Masukkan Stock Buah: ' ))
       harga = int(input('Masukkan Harga Buah: ' ))

    #    tambah_buah = {'Nama' : 'Nanas', 'Stock' : 10, 'Harga' : 25000}
    #    list_buah.append(tambah_buah) # Tidak cocok karena tidak bisa memasukan nama, stock dan harga buah secara random 

       list_buah.append({'Nama' : nama_buah, 'Stock' : stock, 'Harga' : harga}) # Hardcored nama stock dan harga dengan keinginan user secara random
          
       print("Daftar Buah")
       print("Index | Nama | Stock | Harga")

       for i, buah  in enumerate(list_buah):
          print(i, buah['Nama'], buah['Stock'], buah['Harga'])

    #    tambahin nanas ke dictionary

# Step 4 bikin print untuk menghapus nama buah sesuai index
    # print('Sudah masuk print 2')
    elif menu == 3:
        hapus_buah = int(input('Masukkan index Buah yang ingin dihapus: '))

        list_buah.pop(hapus_buah) # .pop(hapus_buah) untuk memilih index buah yang mau di hapus
        for i, buah in enumerate(list_buah): #enumerate untuk mencari index
            print(i, buah['Nama'], buah['Stock'], buah['Harga'])


        # print('Sudah masukprint 3')
    elif menu == 4:

        # Munculin inputan untuk beli lagi
        while True:

            index_buah = int(input('Masukkan index buah yang ingin dibeli: '))
            jumlah_buah = int(input('Masukkan jumlah yang ingin dibeli: '))
            
            stock_dict = list_buah[index_buah]['Stock'] # variabel untuk mengisi jumlah buah yang diinginkan
           
            if stock_dict >= jumlah_buah:
                
                list_buah[index_buah]['Stock'] = stock_dict - jumlah_buah

                # Mau beli Jeruk, jumlah_buah, dictionary_buah harga * jumlah_buah
                list_keranjang.append({
                    'Nama' : list_buah[index_buah]['Nama'],
                    'Qty': jumlah_buah,
                    'Harga' : list_buah[index_buah]['Harga'],
                    'Total_Harga' : list_buah[index_buah]['Harga']*jumlah_buah
            })
            

            else:
                print(f'stock tidak cukup, stock {list_buah[index_buah]['Nama']} tinggal {stock_dict}')

            

            print('Isi Cart : ')
            print('Nama | Qty | Harga')

            for i, buah in enumerate(list_keranjang):
                print(buah['Nama'], buah['Qty'], buah['Harga'])

            lanjut_beli = input('Mau Beli yang lain? ') # Input print

            if lanjut_beli == 'tidak': #lanjut ke print struk
                
                print('Daftar Belanja')
                print('Nama | Qty | Harga | Total Harga')
                Total_harga = 0 # Kalau = 1 maka total harga ada angka 1 misal 1000 menjadi 1001

                for i, buah in enumerate(list_keranjang):
                    print(buah['Nama'], buah['Qty'], buah['Harga'], buah['Total_Harga'])
                    # Jumlahkan setiap total harga ke dalam variabel total_harga
                    Total_harga += buah['Total_Harga'] 
                
                print(f'Total harga {Total_harga}')
                masukkan_uang = int(input('Masukkan jumlah uang : '))

                if Total_harga > masukkan_uang:
                    print('Uang tidak cukup')

                else:
                    print('Terima kasih') 
                    print(f'Uang kembali anda : {masukkan_uang-Total_harga}')
                
                break
    elif menu == 5:
        break      # Keluar program
 
        #if stock dict < inputan
        #maka stock ga cukup

        # kalau stock dict > inputan
        # maka stock dikurangin

        # print(f'Stock tidak cukup, stock {list_buah[index_buah]['Nama']} tinggal ')


        # stock_buah =  - index_buah
        # print(f'Stock tidak cukup, stock jeruk tinggal {stock_buah}')
    


