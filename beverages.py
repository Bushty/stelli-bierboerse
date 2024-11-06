

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