def menu():
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")
    
def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölen sıfır olamaz."
    
def main():
    while True:
        menu()
        secim = input("Bir seçenek girin: ")
        if secim == "5":
            print("Çıkış yapılıyor...")
            break
        elif secim in ["1", "2", "3", "4"]:
            a = float(input("Birinci sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            if secim == "1":
                print(f"Sonuç: {toplama(a, b)}")
            elif secim == "2":
                print(f"Sonuç: {cikarma(a, b)}")
            elif secim == "3":
                print(f"Sonuç: {carpma(a, b)}")
            elif secim == "4":
                print(f"Sonuç: {bolme(a, b)}")
        else:
            print("Geçersiz seçenek lütfen tekrar deneyiniz.")
            
if __name__ == "__main__":
    main()