"""
    **Ürün Envanter Sistemi**: Dictionary ile ürün ekleme, stok güncelleme, arama
"""

products = []
categories = {}

def add_category():
    input_category = input("Kategori adı: ").strip()
    if not input_category:
        print("✖️ Kategori adı boş olamaz!")
        return

    input_category = input_category.title()
    if input_category in categories.values():
        print("✖️ Bu kategori zaten mevcut!")
        return

    new_id = len(categories) + 1
    categories[new_id] = input_category
    print(f"✔️ '{input_category}' kategorisi eklendi (ID: {new_id}).")


def add_product():
    if not categories:
        print("✖️ Önce en az bir kategori ekleyin!")
        return

    print("\nMevcut kategoriler:")
    for cid, name in categories.items():
        print(f"  {cid}: {name}")
    
    try:
        cat_id = int(input("\nKategori ID'sini seçin: "))
        if cat_id not in categories:
            print("✖️ Geçersiz kategori ID'si!")
            return
    except ValueError:
        print("✖️ Lütfen geçerli bir sayı girin!")
        return

    product_name = input("Ürün adı: ").strip()
    if not product_name:
        print("✖️ Ürün adı boş olamaz!")
        return
    product_name = product_name.title()

    for product in products:
        if product["category_id"] == cat_id and product["product_name"] == product_name:
            print("✖️ Bu kategoride aynı isimde bir ürün zaten var!")
            return

    try:
        stock = int(input("Stok miktarı: "))
        if stock < 0:
            print("✖️ Stok negatif olamaz!")
            return
    except ValueError:
        print("✖️ Stok sayısı geçersiz!")
        return

    new_product = {
        "id": len(products),
        "category_id": cat_id,
        "product_name": product_name,
        "stock": stock
    }
    products.append(new_product)
    print(f"✅ '{product_name}' ürünü eklendi (Kategori: {categories[cat_id]}).")


def update_stock():
    if not products:
        print("✖️ Henüz ürün eklenmemiş!")
        return

    search_term = input("Stok güncellemek için ürün adı veya ID girin: ").strip()
    if not search_term:
        print("✖️ Arama terimi boş olamaz!")
        return

    matched_products = []
    if search_term.isdigit():
        product_id = int(search_term)
        for p in products:
            if p["id"] == product_id:
                matched_products.append(p)
                break

    if not matched_products:
        search_term = search_term.title()
        for p in products:
            if search_term in p["product_name"]:
                matched_products.append(p)

    if not matched_products:
        print("✖️ Ürün bulunamadı!")
        return
    elif len(matched_products) == 1:
        product = matched_products[0]
    else:
        print("\nBirden fazla ürün bulundu:")
        for i, p in enumerate(matched_products):
            print(f"  {i+1}. ID: {p['id']}, Ürün: {p['product_name']}, Stok: {p['stock']}")
        try:
            choice = int(input("Güncellemek için seçim yapın (1-{}): ".format(len(matched_products))))
            if 1 <= choice <= len(matched_products):
                product = matched_products[choice - 1]
            else:
                print("✖️ Geçersiz seçim!")
                return
        except ValueError:
            print("✖️ Geçersiz seçim!")
            return

    try:
        new_stock = int(input(f"Mevcut stok: {product['stock']}\nYeni stok miktarı: "))
        if new_stock < 0:
            print("✖️ Stok negatif olamaz!")
            return
        product["stock"] = new_stock
        print(f"✅ '{product['product_name']}' stok miktarı {new_stock} olarak güncellendi.")
    except ValueError:
        print("✖️ Geçersiz stok değeri!")


def search():
    """Ürün ara (isim veya kategoriye göre)."""
    if not products:
        print("✖️ Ürün listesi boş!")
        return

    term = input("Arama terimi (ürün adı veya kategori): ").strip()
    if not term:
        print("✖️ Arama terimi boş olamaz!")
        return

    term = term.title()
    results = []

    for p in products:
        cat_name = categories.get(p["category_id"], "Bilinmeyen")
        if term in p["product_name"] or term == cat_name:
            results.append(p)

    if not results:
        print("✖️ Aradığınız kriterde ürün bulunamadı.")
    else:
        print(f"\n✔️ {len(results)} ürün bulundu:")
        print("-" * 60)
        print(f"{'ID':<5} {'Kategori':<15} {'Ürün Adı':<20} {'Stok':<10}")
        print("-" * 60)
        for p in results:
            cat_name = categories.get(p["category_id"], "Bilinmeyen")
            print(f"{p['id']:<5} {cat_name:<15} {p['product_name']:<20} {p['stock']:<10}")



while True:
    print("\n" + "="*50)
    print("ÜRÜN ENVANTER SİSTEMİ")
    print("="*50)
    print("1. Kategori Ekle")
    print("2. Ürün Ekle")
    print("3. Stok Güncelle")
    print("4. Ürün Ara")
    print("5. Tüm Ürünleri Göster")
    print("q. Çıkış")
    print("-"*50)
    
    option = input("Seçiminiz: ").strip().lower()

    if option == "1":
        add_category()
    elif option == "2":
        add_product()
    elif option == "3":
        update_stock()
    elif option == "4":
        search()
    elif option == "5":
        if not products:
            print("✖️ Ürün listesi boş.")
        else:
            print("\n📋 TÜM ÜRÜNLER:")
            print("-" * 60)
            print(f"{'ID':<5} {'Kategori':<15} {'Ürün Adı':<20} {'Stok':<10}")
            print("-" * 60)
            for p in products:
                cat_name = categories.get(p["category_id"], "Bilinmeyen")
                print(f"{p['id']:<5} {cat_name:<15} {p['product_name']:<20} {p['stock']:<10}")
    elif option == "q":
        print("✔️ Programdan çıkılıyor. İyi günler!")
        break
    else:
        print("✖️ Geçersiz seçim! Lütfen 1-5 arasında bir değer girin veya 'q' ile çıkın.")
