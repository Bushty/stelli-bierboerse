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
                "intervall_s": 120,
                "show_history_h": 2,
                "factor_price_increase": 1.25,
                "factor_price_decrease": 0.91,
                "beverages": [
                    {
                        "name": "Bier 0.3l",
                        "default_price": 1.5,
                        "price_min": 0.6,
                        "price_max": 10.0
                    },
                    {
                        "name": "Bier 0.5l",
                        "default_price": 2.0,
                        "price_min": 0.8,
                        "price_max": 10.0
                    },
                    {
                        "name": "Mische",
                        "default_price": 3.0,
                        "price_min": 1.3,
                        "price_max": 10.0
                    },
                    {
                        "name": "Shot",
                        "default_price": 1.0,
                        "price_min": 0.2,
                        "price_max": 10.0
                    },
                    {
                        "name": "Cider",
                        "default_price": 2.0,
                        "price_min": 1.2,
                        "price_max": 10.0
                    },
                    {
                        "name": "Bachwasser",
                        "default_price": 2.0,
                        "price_min": 0.6,
                        "price_max": 10.0
                    }
                ]
            },
            "history": {
                "time": [
                    "15:00:00"
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
                        "name": "Mische",
                        "prices": [
                            3.0
                        ]
                    },
                    {
                        "name": "Shot",
                        "prices": [
                            1.0
                        ]
                    },
                    {
                        "name": "Cider",
                        "prices": [
                            2.0
                        ]
                    },
                    {
                        "name": "Bachwasser",
                        "prices": [
                            2.0
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

def get_current_prices():
    # preise aus json laden
    beverages = get_history_prices()

    # aktuelle Preise zusammenfassen
    latestPrices = [
        {
            "name": beverage["name"],
            "price": beverage["prices"][-1]
        }
        for beverage in beverages
    ]
    return latestPrices

def handle_sales(sales_numbers):
    # aktuelle preise holen
    current_prices = get_current_prices()

    # neue Preise berechnen lassen
    new_prices = calculate_financials(sales_numbers, get_history_data())

    write_history_change(new_prices)

def write_history_change(new_prices):
    check_history_exists()

    # neuen timestamp setzen
    current_time = time.strftime("%H:%M:%S", time.localtime())
    data = get_history_data()
    data["history"]["time"].append(current_time)

    # neue Preise in json einfügen
    for i in range(len(new_prices)):
        data["history"]["beverages"][i]["prices"].append(new_prices[i])

    with open(jsonPath, 'w') as file:
        json.dump(data, file, indent=4)

def test2():
    print(calculate_financials(beverage_sales))

if __name__ == '__main__':
    test2()
