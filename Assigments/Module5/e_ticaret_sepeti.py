"""
    **E-Ticaret Sepeti**: Ürün ekleme, çıkarma, toplam fiyat hesaplama
"""

products = [
    {
        "id": 1,
        "name": "Defter",
        "price": 89.99,
    },
    {
        "id": 2,
        "name": "Kalem",
        "price": 189.99,
    },
    {
        "id": 3,
        "name": "Silgi",
        "price": 10.50,
    },
    {
        "id": 4,
        "name": "Kitap",
        "price": 450.99,
    },
    {
        "id": 5,
        "name": "Çanta",
        "price": 200.00,
    },
    {
        "id": 6,
        "name": "Cetvel",
        "price": 49.99,
    },
    {
        "id": 7,
        "name": "Kalemlik",
        "price": 80.99,
    },
    {
        "id": 8,
        "name": "Pergel",
        "price": 49.99,
    },
    {
        "id": 9,
        "name": "Sözlük",
        "price": 189.99,
    },
    {
        "id": 10,
        "name": "Dosya",
        "price": 30.25,
    },
]

basket = []

def show_products():
    print("="*40)
    print("📐 KIRTASİYE ÜRÜNLERİ".center(40))
    print("="*40)
    for product in products:
        print(f"{product["id"]} : {product["name"]} (🏷️  {product["price"]} TL)")
    print()


def add_product():
    """
    Sepete ürün ekle
    """
    product_id = int(input("Eklemek istediğiniz ürünü tuşlayınız: "))
    if 1 <= product_id <= 10:     # Burası dinamik olmalı, bende 10 tane ürün olduğu için bu şekilde yazdım
        for product in products:
            if product["id"] == product_id:
                basket.append(product)
                print(f"{product["name"]} sepete eklendi.")
    else:
        print("Ürün bulunamadı")

def remove_product():
    """
    Sepetten ürün çıkartma işlemi
    """
    product = (input("Çıkartmak istediğiniz ürünü yazınız: "))
    for i in basket:
        if i["name"] == product:
            basket.remove(i)
            print(f"{i["name"]} sepetten çıkartıldı.")  

def show_basket():
    print("="*40)
    print("🛒 SEPET".center(40))
    print()
    total = 0
    for i in basket:
        total += i["price"]
        print(f"{i["name"]} : {i["price"]} TL")
    print(f"Sepet tutarı: {total} TL")
    print("="*40)
    print()

    while True:
        print("İşlemler".center(40, "-"))
        print("\n1: Sepetten ürün çıkart")
        print("2: Ana sayfaya git")
        print("q: Çıkış")

        girdi = input("Yapacağınız işlemi tuşlayınız: ")
        if girdi == "q":
            break
        elif girdi == "1":
            remove_product()
        elif girdi == "2":
            main()
            break
        else:
            print("Yanlış tuşlama yaptınız.")

def main():
    show_products()

    while True:
        print("İşlemler".center(40, "-"))
        print("\n1: Sepete ürün ekle")
        print("2: Sepete git")
        print("q: Çıkış")

        girdi = input("Yapacağınız işlemi tuşlayınız: ")
        if girdi == "q":
            break
        elif girdi == "1":
            add_product()
        elif girdi == "2":
            show_basket()
            break
        else:
            print("Yanlış tuşlama yaptınız.")

if __name__ == "__main__":
    main()
