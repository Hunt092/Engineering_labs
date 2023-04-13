def Knapsnack(maxWeigth, items):
    itemspicked = []
    profit = 0
    capacity = maxWeigth
    for item in items:
        if capacity == 0:
            break
        elif item["weight"] < capacity:
            item["size"] = 1
            itemspicked.append(item)
            profit += item["profit"]
            capacity -= item["weight"]
        elif item["weight"] > capacity:
            PbyW = item["profit"]/item["weight"]
            profit += capacity*PbyW
            item["size"] = capacity / item["weight"]
            itemspicked.append(item)
            break
    return itemspicked, profit


def sortbyPWratio(itemArray):
    return sorted(itemArray, key=lambda x: x["profit"]/x["weight"], reverse=True)


def takeItems(itemsArray):
    id = len(itemsArray)+1
    profitOfItem = int(input("Enter profit for id- %s : " % id))
    wiegthOfItem = int(input("Enter weight for id-%s : " % id))
    itemsArray.append({"profit": profitOfItem, "weight": wiegthOfItem})


if __name__ == "__main__":
    maxWeight = int(input("Enter Max weight of the sack: "))
    noItems = int(input("Enter total number of items: "))
    items = []
    for _ in range(noItems):
        takeItems(items)
    sortedItems = sortbyPWratio(items)
    Sack, profit = Knapsnack(maxWeight, sortedItems)

    print("Total profit is ", profit)
    print("for items \n", Sack)
