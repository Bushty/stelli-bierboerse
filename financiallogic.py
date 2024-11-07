import random



def submit_purchases():
    return

def calculate_winners_losers():
    return

def calculate_new_prices():
    return


def get_random_price():
    whole = random.randint(1, 10)
    komma = random.randint(0, 99)
    random_float = float(f"{whole}.{komma}")
    return random_float

def calculate_financials():

    prices_new = {
        "bier_03l": 0.00,
        "bier_05l": 0.00,
        "mische": 0.00,
        "shot": 0.00,
        "cider": 0.00,
        "bachwasser": 0.00
    }

    return prices_new