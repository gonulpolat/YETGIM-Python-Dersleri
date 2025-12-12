"""
    **İndirim Hesaplayıcı**: Ürün fiyatı ve indirim oranını alıp yeni fiyatı hesaplayan program
"""

class Product:
    def __init__(self, product_name: str, price: float):
        self._product_name = product_name
        self._price = price
        self._new_price = 0
        self._discount = 0


    @property
    def product_name(self):
        return self._product_name
    @product_name.setter
    def product_name(self, param_product_name):
        self._product_name = param_product_name  


    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, param_price):
        self._price = param_price  


    @property
    def new_price(self):
        return self._new_price
    @new_price.setter
    def new_price(self, param_new_price):
        self._new_price = param_new_price  


    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, param_discount):
        self._discount = param_discount 


    def  entry_discount(self, d: int):
        self.discount = d
        self.new_price = self.price * (1 - d/100)
        print(f"Yüzde {d} indirim uygulandı.")

    def compare_prices(self):
        print(f"{self.product_name}".center(30, "-"))
        if self.new_price == 0:
            print(f"Fiyat: {self.price} (İndirim yok)")
        else:
            print(f"Eski fiyat: {self.price}")
            print(f"Yeni fiyat: {self.new_price}  (%{self.discount} indirim)")


if __name__ == "__main__":
    urun1 = Product("Kalem", 20)
    urun2 = Product("Defter", 50)
    urun2.entry_discount(20)

    urun1.compare_prices()
    urun2.compare_prices()
