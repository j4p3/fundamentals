order_data = [
    {"type": "Chicken Burger", "toppings": ["cheese", "onion"]},
    {"type": "Chicken Burger", "toppings": ["cheese"]},
    {"type": "Chicken Burger", "toppings": ["onion"]},
    {"type": "Chicken Burger", "toppings": ["lettuce", "tomato"]},

    {"type": "Big Texan Burger", "toppings": ["cheese", "lettuce"]},
    {"type": "Big Texan Burger", "toppings": ["peppers"]},
    {"type": "Big Texan Burger", "toppings": ["peppers"]},
    {"type": "Big Texan Burger", "toppings": ["peppers", "cheese"]},

    {"type": "Mushroom Burger", "toppings": ["mushroom", "onion"]},
    {"type": "Mushroom Burger", "toppings": ["mushroom"]},
    {"type": "Mushroom Burger", "toppings": ["lettuce"]},
    {"type": "Mushroom Burger", "toppings": ["peppers", "mushroom"]},

    {"type": "Fish Burger", "toppings": ["anchovie", "onion"]},
    {"type": "Fish Burger", "toppings": ["cheese"]},
    {"type": "Fish Burger", "toppings": ["anchovie"]},
    {"type": "Fish Burger", "toppings": ["lettuce", "tomato"]},
]

# Question 1
# write an algorithm that counts the number of times a
# given burger type was ordered with a given topping name


def count_type_toppings(burger_type, topping_name):
    total = 0
    for order in order_data:
        if order['type'] == burger_type and topping_name in order['toppings']:
            total += 1
    return total


# print(count_type_toppings('Chicken Burger', 'cheese'))

# Question 2
# write an algorithm that prints out the number of times
# each topping was ordered with each burger


def count_burgers_and_toppings():
    # {"Chicken Burger": {"cheese": 1, "onion": 2}}
    frequency = {}

    for order in order_data:
        for topping in order['toppings']:
            if not frequency.get(order['type']):
                frequency[order['type']] = {}
            if frequency[order['type']].get(topping):
                frequency[order['type']][topping] += 1
            else:
                frequency[order['type']][topping] = 1

    return frequency


print(count_burgers_and_toppings())
