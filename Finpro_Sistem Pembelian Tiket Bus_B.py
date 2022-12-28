def pertama() :
    print("  ________________________________________ ")
    print(" |selamat datang di pembelian tiket bus   |")
    print(" |________________________________________|")
    print(" |           oleh : Naufal Baihaqi M      |")
    print(" |________________________________________|")
    def welcome():
        awal=input('apakah anda ingin melakukan pemesanan tiket(y/n):')
        if awal=='y' :
            print('selamat datang di menu pemesanan tiket bus')
        else:
            print('oke')
            exit
        
    welcome()

    nama = str(input('silahkan masukkan nama: '))
    nomor = int(input('silahkan masukkan nomor: '))


    
    print(" _________________________________________ ")
    print("|             terminal bus                |")
    print("|_________________________________________|")
    print("| 1.Surabaya-Sidoarjo                     |")
    print("| 2.Surabaya-Jombang                      |")
    print("|_________________________________________|")
    print("rutebus")
    rutebus=[]
    for menu1 in rutebus :
        print(menu1, end=' \n')

    def rute() :
        menukelas=int(input('silahkan memasukkan input berdasarkan rute perjalanan:'))
        if menukelas== 1 :
            print('selamat datang di rute surabaya-sidoarjo')
        elif menukelas== 2 :
            print('selamat datang di rute surabaya-jombang')    
        else:
            print('input salah')
            rute()
    rute()

    print(" _______________________ ")
    print("|tiket berdasarkan class|")
    print("|_______________________|")
    print("|1.VIP                  |")
    print("|2.BISNIS               |")
    print("|3.EKONOMI              |")
    print("|_______________________|")
    print("menupemesanan")
    menupemesanan=[]
    for menu2 in menupemesanan:
        print(menu2, end='  ')

    def kelas() :
        menukelas=int(input('silahkan memasukkan angka berdasarkan tiket kelas yang tersedia'))
        if menukelas==1 :
            print("selamat datang di VIP class")
        elif menukelas==2 :
            print('selamat datang di BISNIS class')
        elif menukelas==3 :
            print('selamat datang di EKONOMI class')
        else:
            print('input salah')
            kelas()
    kelas()

    print(" _______________________ ")
    print("|metode pembayaran tiket|")
    print("|_______________________|")
    print("|1.TUNAI                |")
    print("|2.NON TUNAI            |")
    print("|_______________________|")
    print("metodepembayaran")
    metodepembayaran=[]
    for menu3 in metodepembayaran:
        print(menu3, end='  ')
    
    def metode() :
        metodepembayaran=int(input('silahkan memasukkan angka berdasarkan metode pembayaran'))
        if metodepembayaran==1 :
            print('ambil struk, bayar di loket bus')
            print('terima kasih telah melakukan pembelian tiket')
            exit()
        elif metodepembayaran==2 :
            print('silahkan menyelesaikan pembayaran')
        else:
            print('input salah')
            metode()


        uang=int(input('silahkan memasukkan uang sebesar Rp.100.000 :'))
        if uang>=100000:
            hasil=uang-100000
            print ('kembalian uang anda', hasil)
            print('pembayaran selesai, menampilkan tiket online', nama, ' ', nomor)
        elif uang< 100000:
            print('uang anda tidak mencukupi')
            metode()

    metode()

    
    def last() :
        again=(input('apakah anda ingin melakukan pembelian lagi (y/n) :'))
        if again=='y' :
            pertama()
        elif again=='n' :
            print('terima kasih telah melakukan pembelian tiket bus')
            quit()
        else:
            print('input salah')
            last()
    last()
pertama()
