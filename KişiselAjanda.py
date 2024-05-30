def menu():
    print("1. Etkinlik Ekle")
    print("2. Etkinlikleri Göster")
    print("3. Etkinlikleri Sil")
    print("4. Çıkış")
    
def etkinlik_ekle(ajanda):
    isim = input("Etkinlik Adı: ")
    tarih = input("Tarih (Örn: 01-01-2024 13:00): ")
    if isim and tarih:
        ajanda.append({'isim': isim, 'tarih': tarih})
        print("Etkinlik eklendi!")
    else:
        print("Etkinlik adı ve tarih boş bırakılamaz.")
        
def etkinlikleri_göster(ajanda):
    if not ajanda:
        print("Hiç etkinlik yok.")
    else:
        for i, etkinlik in enumerate(ajanda):
            print(f"{i + 1}. {etkinlik['isim']} - {etkinlik['tarih']}")
            
def etkinlik_sil(ajanda):
    etkinlikleri_göster(ajanda)
    silinecek_index = int(input("Silmek istediğiniz etkinliğin numarasını girin: ")) - 1
    if 0 <= silinecek_index < len(ajanda):
        del ajanda[silinecek_index]
        print("Etkinlik silindi.")
    else:
        print("Geçersiz index")
        
def main():
    ajanda = []
    while True:
        menu()
        secim = input("Bir seçenek girin: ")
        if secim == "1":
            etkinlik_ekle(ajanda)
        elif secim == "2":
            etkinlikleri_göster(ajanda)
        elif secim == "3":
            etkinlik_sil(ajanda)
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")
            
if __name__ == "__main__":
    main()