import os
import json
import time

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

def load_history_data():
    check_history_exists()
    with open(jsonPath, 'r') as file:
        data = json.load(file)
    return data

def get_timestamps():
    data = load_history_data()
    history_timestamps = data['history']['time']
    return history_timestamps

def get_history_prices():
    data = load_history_data()
    history_prices = data['history']['beverages']
    return history_prices

def write_history_change():
    timestamp = time.localtime()




if __name__ == '__main__':
    check_history_exists()
