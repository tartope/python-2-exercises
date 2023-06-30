class TaxMan:
    def __init__(self, items, tax):
        self.items = items
        self.tax = tax
        self.__price = 0

    

    def calc_total(self):
        for p in self.items:
            self.__price += p['price']
        
        tax = float(self.tax.strip("%")) / 100
        self.__price = self.__price + (self.__price * tax)
    
    def get_total(self):
        return self.__price