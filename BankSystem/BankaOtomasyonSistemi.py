#  <<<<<<<<<<<<<<<< Banka otomasyonu >>>>>>>>>>>>>>>>>>>>>
# Ozellikle Liste Ve Dosya Islemleri Kullanilarak Python Dilinde Yazilmis Basit Bir Otomasyon Sistemi

h_sayisi = 0
satir = []
tumhesaplar = []
satir1 = []
sayilar = "1234567890"

with open("21100011048.txt", "r+") as oto:
    satir.append(oto.readlines())
for i in satir:
    for j in i:
        if i == "\n" or j == "\n":
            continue
        else:
            satir1.append(j.split("\n")[0])
lsatir1 = len(satir1)
h_sayisi += (lsatir1 // 7)
for k in range((lsatir1 // 7)):
    sozluk = {"ad_soyad": None, "para": None, "hesap_no": None, "kredi_karti": 0, "elektrik": 0, "su": 0,
              "dogalgaz": 0}
    for i, j in zip(satir1, sozluk):
        for z in i.split(":")[1]:
            if z in sayilar:
                sozluk[str(j)] = int(i.split(":")[1])
            else:
                sozluk[str(j)] = i.split(":")[1]
    tumhesaplar.append(sozluk)
    for a in range(0, 7):
        h = 0
        satir1.pop(h)


def menu():
    print("\033[36m\033[1m")  # renkli yazmak icin kullandım
    print("\n************* MENU *************")
    print("\n ( 1 ) | Hesap Ekle")
    print("\n ( 2 ) | Hesap Bilgileri Guncelle")
    print("\n ( 3 ) | Hesap Ara")
    print("\n ( 4 ) | Hesap Sil")
    print("\n ( 5 ) | Hesaplari Listele")
    print("\n ( 6 ) | Para Yatirma / Cekme")
    print("\n ( 7 ) | Harcama Ekle")
    print("\n ( 8 ) | Fatura Ode")
    print("\n ( 9 ) | Dosya islemleri")
    print("\n ( 0 ) | Cikis")
    print("\n********************************")


def ekle(hsayisi, a):
    # print("\033[36m\033[1m")
    print("\n--- Yeni Musteri Hesabi Acilisi ---")
    ad_soyad = input("\nLutfen ad ve soyad giriniz:> ")
    para = int(input("\nLutfen hesabiniza yatiracaginiz tutari giriniz:> "))
    a[hsayisi - 1]["ad_soyad"] = ad_soyad
    a[hsayisi - 1]["para"] = para
    a[hsayisi - 1]["hesap_no"] = hsayisi
    borclar = {"kredi_karti": 0, "elektrik": 0, "su": 0, "dogalgaz": 0}
    a[hsayisi - 1].update(borclar)
    print("\nHesabiniz acilmistir.")
    dosyaisleme(tumhesaplar)


def harcama_ekle(hesapno, a):
    # print("\033[34m\033[1m")
    sec = input("\nKredi karti borcu ekleme icin (1) elektrik icin (2) su icin(3) dogalgaz (4) \n"
                "ana menuye donmek icin (0) gir")
    if sec == "1":
        borc = int(input("\nKredi karti borcunu gir"))
        a[hesapno - 1]["kredi_karti"] += borc
        dosyaisleme(a)
        harcama_ekle(hesapno, a)
    elif sec == "2":
        borc = int(input("\nElektrik faturasi borcunu gir"))
        a[hesapno - 1]["elektrik"] += borc
        dosyaisleme(a)
        harcama_ekle(hesapno, a)
    elif sec == "3":
        borc = int(input("\nSu faturasi borcunu gir"))
        a[hesapno - 1]["su"] += borc
        dosyaisleme(a)
        harcama_ekle(hesapno, a)
    elif sec == "4":
        borc = int(input("\nDogalgaz faturasi borcunu gir"))
        a[hesapno - 1]["dogalgaz"] += borc
        dosyaisleme(a)
        harcama_ekle(hesapno, a)
    elif sec == "0":
        menu()
    else:
        print("Lutfen belirtilen seceneklerden birini seciniz")


def paraYatir_cek(hno, l):
    # print("\033[34m\033[1m")
    sec = input("Para yatirmak icin (1) cekmek icin (2) gir")
    if sec == "1":
        yatirilacak = int(input("\nYatiracagin tutari gir"))
        l[hno - 1]["para"] += yatirilacak
        dosyaisleme(l)
    elif sec == "2":
        cekilecek = int(input("\nCekecegin tutari gir"))
        l[hno - 1]["para"] -= cekilecek
        dosyaisleme(l)
    else:
        print("Lutfen belirtilen seceneklerden birini seciniz")


def faturaode(hno, l):
    # print("\033[34m\033[1m")
    sec = input("\nKredi borcu icin (1) elektrik icin (2) su icin (3) dogalgaz icin (4) menuye donmek icin (0) giriniz")
    if sec == "1":
        miktar = int(input("\nOdemek istediginiz miktari giriniz"))
        if l[hno - 1]["para"]>=miktar:
            l[hno - 1]["kredi_karti"] -= miktar
            l[hno - 1]["para"]-=miktar
        else:
            print("\n Uzgunuz hesabinizda o kadar para bulunmuyor para yatirarak tekrar deneyebilirsiniz")
        faturaode(hno, l)
    elif sec == "2":
        miktar = int(input("\nOdemek istediginiz miktari giriniz"))
        if l[hno - 1]["para"] >= miktar:
            l[hno - 1]["elektrik"] -= miktar
            l[hno - 1]["para"] -= miktar
        else:
            print("\n Uzgunuz hesabinizda o kadar para bulunmuyor para yatirarak tekrar deneyebilirsiniz")
        faturaode(hno, l)
    elif sec == "3":
        miktar = int(input("\nOdemek istediginiz miktari giriniz"))
        if l[hno - 1]["para"] >= miktar:
            l[hno - 1]["su"] -= miktar
            l[hno - 1]["para"] -= miktar
        else:
            l[hno - 1]["para"] -= miktar
        faturaode(hno, l)
    elif sec == "4":
        miktar = int(input("\nOdemek istediginiz miktari giriniz"))
        if l[hno - 1]["para"] >= miktar:
            l[hno - 1]["dogalgaz"] -= miktar
            l[hno - 1]["para"] -= miktar
        else:
            l[hno - 1]["para"] -= miktar
        faturaode(hno, l)
    elif sec == "0":
        dosyaisleme(l)
        menu()
    else:
        print("Lutfen belirtilen seceneklerden birini seciniz")
        faturaode(hno, l)


def hesap_Sil(hsayisi, hno, l):
    # print("\033[36m\033[1m")
    print("\nhesabiniz siliniyor")
    for i in range(hno, hsayisi):
        l[i]["hesap_no"] -= 1
    l.pop(hno - 1)
    print("\nHesabiniz silindi ve hesap numaralari otomatik guncellendi ")
    print("\n Guncel otomosyonu ve yeni hesap numaralarini asagida gorebilirsiniz ")
    dosyaisleme(l)
    Listele(hsayisi, hno, l)


def arama(hno, l):
    print("\nAradiginiz hesap goruntuleniyor")
    for i in l[hno - 1]:
        a = 13 * "  "
        print(i, (13 - len(i)) * " ", l[hno - 1][i])


def guncelleme(hno, l):
    sec = int(input("\nSectiginiz kullanıcının hangi bilgisini guncellemek istersiniz? "
                    "lutfen ad_soyad bılgısı ıcın (1) para icin (2) veya fatura tutarlarını degistirmek icin (0) giriniz"))
    if sec == 1:
        yeni = input("\nKullanicicin yeni ismini giriniz")
        l[hno - 1]["ad_soyad"] = yeni
        dosyaisleme(l)
    elif sec == 7:
        yeni = input("\nKullanicicin yeni parasini giriniz")
        l[hno - 1]["para"] = yeni
        dosyaisleme(l)
    elif sec == 0:
        harcama_ekle(hno, tumhesaplar)
    else:
        print("\n Yanlis bir secim oldu lutfen tekrar deneyiniz")
        guncelleme(hno, l)


def Listele(hsayisi, a, l):
    k = 0
    for i in l:
        for j in i:
            print(j, (13 - len(j)) * " ", l[k][j])
        k += 1
        print("\n\n")


def dosyaisleme(tumhesaplar):
    b = 0
    with open("21100011048.txt",  "r+") as otok:
        otok.truncate(0)
    with open("21100011048.txt",  "r+") as oto:

        for i in tumhesaplar:
            for p in i:
                a = tumhesaplar[b][p]
                if type(a) == str:
                    oto.write(p + ":" + str(a) + "\n")
                elif type(a) == int:
                    oto.write(f"{p}:{a}\n")
            oto.write("\n")
            b += 1


def dosyaoku():
    with open("21100011048.txt", "r+") as oto:
        print(oto.read())


hsayisi = h_sayisi
while True:
    menu()
    secim = input("\nYapmak istedigin islemin numarasini gir Dosyayi okumak icin r veya R gir\n")
    if secim == "1":
        hsayisi += 1
        hesap = {}
        tumhesaplar.append(hesap)
        ekle(hsayisi, tumhesaplar)
    elif secim == "2":
        hno = int(input("\nislem yapmak istediginiz hesap numarasini giriniz"))
        guncelleme(hno, tumhesaplar)
    elif secim == "3":
        no = int(input("\nAramak goruntulemek istediginiz hesano no'sunu giriniz"))
        arama(no, tumhesaplar)
    elif secim == "4":
        hno = int(input("\nSilmek istedigin hesap numarasini gir"))
        hesap_Sil(hsayisi, hno, tumhesaplar)
        hsayisi -= 1
    elif secim == "5":
        print("\nHesaplar listeleniyor...\n")
        Listele(hsayisi, h_sayisi, tumhesaplar)
    elif secim == "6":
        hno = int(input("\nPara yatirmak ya da cekmek istedigin hesap numarasini gir"))
        paraYatir_cek(hno, tumhesaplar)
    elif secim == "7":
        hesapno = int(input("\nHesap numarasini gir"))
        harcama_ekle(hesapno, tumhesaplar)
    elif secim == "8":
        hno = int(input("\nislem yapmak istediginiz hesap numarasini giriniz"))
        faturaode(hno, tumhesaplar)
    elif secim == "9":
        dosyaisleme(tumhesaplar)
    elif secim == "r" or secim == "R":
        dosyaoku()
    elif secim == "0":
        dosyaisleme(tumhesaplar)
        break
    else:
        print("\nYanlis bir secim tekrar deneyiniz")
