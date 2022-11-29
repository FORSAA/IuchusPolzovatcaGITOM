class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.__price = price
        self.__salePercent = 0

    @property
    def salePrice(self):
        return self.__price - self.__price*(self.__salePercent/100)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if(price>0):
            self.__price=price

    def Sale(self, percent):
        if(percent <= 100 and percent >= 0):
            self.__salePercent=percent

    def GetFullPrice(self, count, is_on_sale):
        if is_on_sale:
            price = self.salePrice*count
        else:
            price = self.__price * count
        return price

    def qqqqqqq(self):
        return 1
