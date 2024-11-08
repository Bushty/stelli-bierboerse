class Beverage:
    def __init__(self, name, ini_price, min_price, max_price, use_max_price):
        name = name
        current_price = ini_price
        min_price = min_price
        max_price = max_price
        use_max_price = use_max_price

    def get_price(self):
        return self.current_price
    
    def increase_price(self, percentage):
        faktor = 1 + percentage/100
        self.current_price *= faktor

    def decrease_price(self, percentage):
        faktor = 1 - (percentage/100)
        self.current_priace *= faktor

class BeverageHistoryItem:
    def __init__(self):
        pass

class BeverageHistory:
    def __init__(self, beverage):
        pass

def get_initialized_beverages():
    beverages = []
    beverages.append(Beverage("Bier 0,3l", 1.50, 0.00, 100.00, True))
    beverages.append(Beverage("Bier 0,5l", 2.00, 0.00, 100.00, True))
    beverages.append(Beverage("Shot", 1.00, 0.00, 100.00, True))
    beverages.append(Beverage("Mische", 3.00, 0.00, 100.00, True))
    beverages.append(Beverage("Cider", 2.00, 0.00, 100.00, True))
    beverages.append(Beverage("Bachwasser", 2.00, 0.00, 100.00, True))

    return beverages
