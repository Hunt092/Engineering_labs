# orderProto={item_name,quantity,price}
import random


def createOrders():

    orderArray = []
    while True:
        order = {}
        order["item_name"] = input(
            "What item would you like to add to your order:")
        quantity = int(input("How many of these: "))
        order['quantity'] = quantity
        order['price'] = random.randint(0, 1000)*quantity
        orderArray.append(order)
        cond = input("Do you want to add anythin else? (y/n):").lower()
        if (cond == 'n'):
            break

    return orderArray
