basket = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}

basket["watermelon"] = 5

for idx, (fruit, amount) in enumerate(basket.items()):
    if idx == len(basket) - 1:
        print(fruit, amount)
