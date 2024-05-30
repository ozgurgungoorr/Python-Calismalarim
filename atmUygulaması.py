def menu():
    print("1. Bakiye Sorgula")
    print("2. Para Çek")
    print("3. Para Yatır")
    print("4. Çıkış")

def bakiye_sorgula(bakiye):
    print(f"Şu anki bakiyeniz: {bakiye} TL")

def para_cek(bakiye):
    miktar = float(input("Çekmek istediğiniz miktarı girin: "))
    if miktar > 0 and miktar <= bakiye:
        bakiye -= miktar
        print(f"{miktar} TL çekildi.")
    else:
        print("Geçersiz miktar.")

def para_yatir(bakiye):
    miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
    if miktar > 0:
        bakiye += miktar
        print(f"{miktar} TL yatırıldı.")
    else:
        print("Geçersiz miktar.")

def main():
    bakiye = 1000  # Başlangıç bakiyesi
    while True:
        menu()
        secim = input("Bir seçenek girin: ")
        if secim == "1":
            bakiye_sorgula(bakiye)
        elif secim == "2":
            para_cek(bakiye)
        elif secim == "3":
            para_yatir(bakiye)
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
