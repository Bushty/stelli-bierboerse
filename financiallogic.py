import random
import os
import json

##### TODO: REMOVE SOMEHOW DUPLICATION FROM DATAMANAGER #####
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
    random_max = 100
    bier03l_random = random.randint(1, random_max)
    bier05l_random = random.randint(1, random_max)
    mische_random = random.randint(1, random_max)
    shot_random = random.randint(1, random_max)
    cider_random = random.randint(1, random_max)
    bachwasser_random = random.randint(1, random_max)
    test_numbers = {
        "bier03l": bier03l_random,
        "bier05l": bier05l_random,
        "mische": mische_random,
        "shot": shot_random,
        "cider": cider_random,
        "bachwasser": bachwasser_random
    }
    print(f"Test sales_numbers: {test_numbers}")
    return test_numbers

def calculate_financials(sales_numbers, history_config):
    config_data = history_config["config"]
    factor_price_increase = config_data["factor_price_increase"]
    factor_price_decrease = config_data["factor_price_decrease"]

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
            old_prices["bier03l"] = beverage["prices"][-1]
        if beverage["name"] == "Bier 0.5L":
            old_prices["bier05l"] = beverage["prices"][-1]
        if beverage["name"] == "Mische":
            old_prices["mische"] = beverage["prices"][-1]
        if beverage["name"] == "Shot":
            old_prices["shot"] = beverage["prices"][-1]
        if beverage["name"] == "Cider":
            old_prices["cider"] = beverage["prices"][-1]
        if beverage["name"] == "Bachwasser":
            old_prices["bachwasser"] = beverage["prices"][-1]

    

    # get range of sales
    lowest = min(sales_numbers.values())
    highest = max(sales_numbers.values())

    range = highest - lowest
    average = range / 2
    range_weight = range / 10

    print(f"range: {range}")
    print(f"average: {average}")
    print(f"range_weight: {range_weight}")
    print(f"power: {pow(1, range_weight)}")

    # update prices
    for beverage in sales_numbers:
        if float(sales_numbers[beverage]) > average:
            new_price = float(old_prices[beverage]) * (pow(factor_price_increase, range_weight))
            new_price_shortened = round(new_price, 2)
            old_prices[beverage] = new_price_shortened
        if float(sales_numbers[beverage]) < average:
            new_price = float(old_prices[beverage]) * (pow(factor_price_decrease, range_weight))
            new_price_shortened = round(new_price, 2)
            old_prices[beverage] = new_price_shortened

    # get min & max prices from history_config
    config_beverages = history_config["config"]["beverages"]
    # ensure min & max prices are kept
    for beverage in config_beverages:
        if beverage["name"] == "Bier 0.3l":
            beverage_max = beverage["price_max"]
            beverage_min = beverage["price_min"]
            if old_prices["bier03l"] > beverage_max:
                old_prices["bier03l"] = beverage_max
            if old_prices["bier03l"] < beverage_min:
                old_prices["bier03l"] = beverage_min
        if beverage["name"] == "Bier 0.5l":
            beverage_max = beverage["price_max"]
            beverage_min = beverage["price_min"]
            if old_prices["bier05l"] > beverage_max:
                old_prices["bier05l"] = beverage_max
            if old_prices["bier05l"] < beverage_min:
                old_prices["bier05l"] = beverage_min
        if beverage["name"] == "Cider":
            beverage_max = beverage["price_max"]
            beverage_min = beverage["price_min"]
            if old_prices["cider"] > beverage_max:
                old_prices["cider"] = beverage_max
            if old_prices["cider"] < beverage_min:
                old_prices["cider"] = beverage_min
        if beverage["name"] == "Mische":
            beverage_max = beverage["price_max"]
            beverage_min = beverage["price_min"]
            if old_prices["mische"] > beverage_max:
                old_prices["mische"] = beverage_max
            if old_prices["mische"] < beverage_min:
                old_prices["mische"] = beverage_min
        if beverage["name"] == "Bachwasser":
            beverage_max = beverage["price_max"]
            beverage_min = beverage["price_min"]
            if old_prices["bachwasser"] > beverage_max:
                old_prices["bachwasser"] = beverage_max
            if old_prices["bachwasser"] < beverage_min:
                old_prices["bachwasser"] = beverage_min
        if beverage["name"] == "Shot":
            beverage_max = beverage["price_max"]
            beverage_min = beverage["price_min"]
            if old_prices["shot"] > beverage_max:
                old_prices["shot"] = beverage_max
            if old_prices["shot"] < beverage_min:
                old_prices["shot"] = beverage_min
            

    # return new prices

    return old_prices

def test():
    print(calculate_financials(sales_numbers_test(), get_history_data()))
    return

if __name__ == '__main__':
    test()