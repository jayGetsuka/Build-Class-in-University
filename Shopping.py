class Shopping:
    price = 0
    product = {"Node MCU": 157, "Shoes Nike": 2599, "Sweater Adidas": 1299, "Jeans": 1299,
               "Hat Gucci": 10999, "Rubber Ducky": 2500, "Digispark attiny85": 40}

    def Sumproduct(self, products):
        total = {}
        for data in products:
            if data in Shopping.product:
                print(data, "Price", Shopping.product[data], "฿")
                total[data] = Shopping.product[data]
            else:
                pass
        self.total = total
        Shopping.price += sum(self.total.values())
        print()
        print("************* All Products **************")
        for k,v in self.total.items():
            print(k, v)
        print()
        print("Price = ", Shopping.price, "฿")
        print("Delivery = 35 ฿")
        print("Total = ", Shopping.price + 35, "฿")
        print("-----------Thank you--------------")

    def SearchProduct(self, name_product):
        self.name_pro = name_product
        if self.name_pro in Shopping.product:
            print(self.name_pro, Shopping.product[self.name_pro], "฿")
        else:
            print(self.name_pro,"have not in Products")
            print("We will update coming soon...")

    def AllProduct(self):
        for k,v in Shopping.product.items():
            print(k, "price: ", v, "฿")

while True:
    print("""
********** Welcome to JShopping **************
* 1.Shop Products                            *
* 2.Search Product                           *
* 3.All Products                             *    
* 4. Anykey to shutdown Program              *
**********************************************""")
    Cusch = int(input("Choose: "))
    if Cusch == 1:
        shopping_ = Shopping()
        for k, v in shopping_.product.items():
            print(k, "Price", v, "฿")
        print()
        choose_products = list(input("input name_products: ").split(","))
        print()
        shopping_.Sumproduct(choose_products)
    elif Cusch == 2:
        name_product_Sh = input("Name product: ")
        shopping_ = Shopping()
        shopping_.SearchProduct(name_product_Sh)
    elif Cusch == 3:
        shopping_ = Shopping()
        shopping_.AllProduct()
    else:
        break
