import random
import os
import json

##### TODO: REMOVE SOMEHOW DUPLICATION FROM DATAMANAGER #####
jsonPath = "./history.json"

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

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def calculate_financials(sales_numbers, history_config):
    config_data = history_config["config"]
    factor_price_increase = config_data["factor_price_increase"]
    factor_price_decrease = config_data["factor_price_decrease"]

    # get old prices from history_config
    old_prices = []
    history_beverages = history_config['history']['beverages']
    for beverage in history_beverages:
        old_prices.append(beverage["prices"][-1])

    # get range of sales
    lowest = min(sales_numbers)
    highest = max(sales_numbers)

    sales_range = highest - lowest
    average = sales_range / 2
    range_weight = sales_range / 10

    # print(f"sales_range: {sales_range}")
    # print(f"average: {average}")
    # print(f"range_weight: {range_weight}")
    # print(f"power: {pow(1, range_weight)}")

    # update prices
    for i in range(len(old_prices)):
        if float(sales_numbers[i]) > average:
            new_price = float(old_prices[i]) * (pow(factor_price_increase, range_weight))
            new_price_shortened = round(new_price, 2)
            old_prices[i] = new_price_shortened

        if float(sales_numbers[i]) < average:
            new_price = float(old_prices[i]) * (pow(factor_price_decrease, range_weight))
            new_price_shortened = round(new_price, 2)
            old_prices[i] = new_price_shortened

    # get min & max prices from history_config
    config_beverages = history_config["config"]["beverages"]

    # ensure values are within min max boundry
    for i in range(len(old_prices)):
        old_prices[i] = clamp(old_prices[i], config_beverages[i]['price_min'], config_beverages[i]['price_max'])


    # return new prices
    return old_prices
