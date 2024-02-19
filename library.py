class Kütüphane:
    def __init__(self):
        self.dosya_yolu = "kitaplar.txt"
        self.dosya = open(self.dosya_yolu, "a+")

    def dosyayi_kapat(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()

        if not kitaplar:
            print("Kütüphanede kitap yok.")
            return

        kitap_bilgileri = [kitap.split(',') for kitap in kitaplar]
        for başlık, yazar, _, _ in kitap_bilgileri:
            print(f"Başlık: {başlık}, Yazar: {yazar}")

    def kitap_ekle(self):
        başlık = input("Kitap başlığını girin: ")
        yazar = input("Kitap yazarını girin: ")
        yayın_tarihi = input("Yayın yılını girin: ")
        sayfa_sayısı = input("Sayfa sayısını girin: ")

        kitap_bilgisi = f"{başlık},{yazar},{yayın_tarihi},{sayfa_sayısı}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitap başarıyla eklendi!")

    def kitap_sil(self):
        silinecek_başlık = input("Silmek istediğiniz kitabın başlığını girin: ")

        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()

        kitaplar = [kitap for kitap in kitaplar if silinecek_başlık not in kitap.split(',')]

        self.dosya.seek(0)
        self.dosya.truncate()
        for kitap in kitaplar:
            self.dosya.write(kitap + '\n')

        # Dosyanın sonuna bir satır boşluk eklenmiş olabilir, bu yüzden dosyayı kapatıp tekrar açıyoruz.
        self.dosyayi_kapat()
        self.dosya = open(self.dosya_yolu, "a+")

        print("Kitap başarıyla silindi!")

# Kütüphane nesnesi oluştur
kütüphane = Kütüphane()

# Menü
while True:
    print("\n** MENÜ **")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    print("4) Çıkış")

    seçim = input("Seçiminizi yapın (1-4): ")

    if seçim == '1':
        kütüphane.kitaplari_listele()
    elif seçim == '2':
        kütüphane.kitap_ekle()
    elif seçim == '3':
        kütüphane.kitap_sil()
    elif seçim == '4':
        kütüphane.dosyayi_kapat()
        print("Kütüphane Yönetim Sisteminden çıkılıyor. İyi günler!")
        break
    else:
        print("Geçersiz seçim. Lütfen geçerli bir seçenek girin.")
