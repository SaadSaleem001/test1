starting_money=100
starting_num_items=10
item_price=4

def buy_items(money, num_items, price):
    """Calculates how many items can be bought with the given money and price."""

    num_bought = 0

    while money >= price and num_items > 0:
        money -= price  # Subtract the price from the remaining money
        num_items -= 1  # Decrement the number of items available
        num_bought += 1  # Increment the number of items bought

    return num_bought

# Main code for buying dog treats
total = buy_items(starting_money, starting_num_items, item_price)
print("You were able to buy " + str(total) + " dog treats.")


total_1=buy_items(100,10,4)
print('Test 1 ' +str(total_1))
total_2=buy_items(10,10,4)
print('Test 2 ' +str(total_2))