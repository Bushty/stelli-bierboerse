import os
import json
import time
from financiallogic import calculate_financials

jsonPath = "./history.json"

beverage_sales = {
    "bier03l": 0,
    "bier05l": 0,
    "mische": 0,
    "shot": 0,
    "cider": 0,
    "bachwasser": 0
}

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

def get_history_timestamps():
    data = get_history_data()
    history_timestamps = data['history']['time']
    return history_timestamps

def get_history_prices():
    data = get_history_data()
    history_prices = data['history']['beverages']
    return history_prices

def get_config():
    data = get_history_data()
    return data['config']

def store_sales_numbers(sales_data):
    if "bier03l" in sales_data:
        bier_03l_sales = sales_data["bier03l"]
    if "bier05l" in sales_data:
        bier_05l_sales = sales_data["bier05l"]
    if "mische" in sales_data:
        mische_sales = sales_data["mische"]
    if "shot" in sales_data:
        shot_sales = sales_data["shot"]
    if "cider" in sales_data:
        cider_sales = sales_data["cider"]
    if "bachwasser" in sales_data:
        bachwasser_sales = sales_data["bachwasser"]

    beverage_sales["bier03l"] += bier_03l_sales
    beverage_sales["bier05l"] += bier_05l_sales
    beverage_sales["mische"] += mische_sales
    beverage_sales["shot"] += shot_sales
    beverage_sales["cider"] += cider_sales
    beverage_sales["bachwasser"] += bachwasser_sales
    print(beverage_sales)


def write_history_change_test():
    check_history_exists()
    current_time = time.strftime("%H:%M", time.localtime())
    data = get_history_data()
    data["history"]["time"].append(current_time)
    for beverage in data["history"]["beverages"]:
        beverage["prices"].append(financiallogic.get_random_price())

    with open(jsonPath, 'w') as file:
        json.dump(data, file, indent=4)

def test2():
    print(calculate_financials())

if __name__ == '__main__':
    test2()
