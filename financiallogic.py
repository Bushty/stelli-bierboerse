import random
import os
import json

##### TODO: REMOVE SOMEHOW DUPLICATES FROM DATAMANAGER #####
jsonPath = "./history.json"

def check_history_exists():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = "history.json"
    file_path = os.path.join(current_directory, file_name)
    if not os.path.exists(file_path):
        data = {
            "config": {
                "intervall_s": 300.0,
                "factor_price_increase": 1.05,
                "factor_price_decrease": 0.95,
                "beverages": [
                    {
                        "name": "Bier 0.3l",
                        "default_price": 1.5,
                        "price_min": 0.5,
                        "price_max": 10.0
                    },
                    {
                        "name": "Bier 0.5l",
                        "default_price": 2.0,
                        "price_min": 0.8,
                        "price_max": 10.0
                    },
                    {
                        "name": "Cider",
                        "default_price": 2.0,
                        "price_min": 1.0,
                        "price_max": 10.0
                    },
                    {
                        "name": "Mische",
                        "default_price": 3.0,
                        "price_min": 1.5,
                        "price_max": 10.0
                    },
                    {
                        "name": "Bachwasser",
                        "default_price": 2.0,
                        "price_min": 1.0,
                        "price_max": 10.0
                    },
                    {
                        "name": "Shot",
                        "default_price": 1.0,
                        "price_min": 0.5,
                        "price_max": 10.0
                    }
                ]
            },
            "history": {
                "time": [
                        0
                ],
                "beverages": [
                    {
                        "name": "Bier 0.3L",
                        "prices": [
                            1.5
                        ]
                    },
                    {
                        "name": "Bier 0.5L",
                        "prices": [
                            2.0
                        ]
                    },
                    {
                        "name": "Cider",
                        "prices": [
                            2.0
                        ]
                    },
                    {
                        "name": "Mische",
                        "prices": [
                            3.0
                        ]
                    },
                    {
                        "name": "Bachwasser",
                        "prices": [
                            2.0
                        ]
                    },
                    {
                        "name": "Shot",
                        "prices": [
                            1.0
                        ]
                    }
                ]
            }
        }

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

def get_history_data():
    check_history_exists()
    with open(jsonPath, 'r') as file:
        data = json.load(file)
    return data

def get_config():
    data = get_history_data()
    return data['config']

####---------------------#####

# def get_random_price():
#     whole = random.randint(1, 10)
#     komma = random.randint(0, 99)
#     random_float = float(f"{whole}.{komma}")
#     return random_float


# def old_prices_test():
#     test_prices = {
#         "bier03l": get_random_price(),
#         "bier05l": get_random_price(),
#         "mische": get_random_price(),
#         "shot": get_random_price(),
#         "cider": get_random_price(),
#         "bachwasser": get_random_price()
#     }
#     return test_prices

def sales_numbers_test():
    bier03l_random = random.randint(1, 10)
    bier05l_random = random.randint(1, 10)
    mische_random = random.randint(1, 10)
    shot_random = random.randint(1, 10)
    cider_random = random.randint(1, 10)
    bachwasser_random = random.randint(1, 10)
    test_numbers = {
        "bier03l": bier03l_random,
        "bier05l": bier05l_random,
        "mische": mische_random,
        "shot": shot_random,
        "cider": cider_random,
        "bachwasser": bachwasser_random
    }
    return test_numbers

def calculate_financials(sales_numbers, history_config):
    config_data = history_config["config"]
    factor_price_increase = config_data["factor_price_increase"].value
    factor_price_decrease = config_data["factor_price_decrease"].value

    # get old prices from history_config
    old_prices = {
        "bier03l": 0.00,
        "bier05l": 0.00,
        "mische": 0.00,
        "shot": 0.00,
        "cider": 0.00,
        "bachwasser": 0.00
    }
    history_beverages = history_config['history']['beverages']
    
    for beverage in history_beverages:
        if beverage["name"] == "Bier 0.3L":
            old_prices["bier03l"].value = beverage["prices"][-1]
        if beverage["name"] == "Bier 0.5L":
            old_prices["bier05l"].value = beverage["prices"][-1]
        if beverage["name"] == "Mische":
            old_prices["mische"].value = beverage["prices"][-1]
        if beverage["name"] == "Shot":
            old_prices["shot"].value = beverage["prices"][-1]
        if beverage["name"] == "Cider":
            old_prices["cider"].value = beverage["prices"][-1]
        if beverage["name"] == "Bachwasser":
            old_prices["bachwasser"].value = beverage["prices"][-1]

    

    # get range of sales
    lowest = min(sales_numbers.values())
    highest = max(sales_numbers.values())

    range = highest - lowest
    average = range / 2


    # update prices
    for beverage in sales_numbers:
        if beverage.value > average:
            old_prices[beverage].value = old_prices[beverage].value * factor_price_increase
        if beverage.value < average:
            old_prices[beverage].value = old_prices[beverage].value * factor_price_decrease

    # get min & max prices from history_config

    # ensure min & max prices are kept

    # return new prices

    return old_prices

# def test():
#     print(calculate_financials(sales_numbers_test(), old_prices_test()))
#     return

# if __name__ == '__main__':
#     test()