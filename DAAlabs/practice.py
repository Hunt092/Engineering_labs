def fibonacci(max):
    if max < 1:
        return max
    return fibonacci(max-1)+fibonacci(max-2)


def knapsackgreedy(items, maxweight):
    itemsPicked = []
    profit = 0
    capacity = maxweight
    items = sorted(
        items, key=lambda item: item["profit"]/item['weight'], reverse=True)
    for item in items:
        if capacity == 0:
            break
        if item['weight'] < capacity:
            item["size"] = 1
            itemsPicked.append(item)
            profit = item['profit']
            capacity -= item["weight"]

        if item['weight'] > capacity:
            pbyW = item["profit"]/item['weight']
            item["size"] = capacity / item['weight']
            profit += pbyW*capacity
            itemsPicked.append(item)
            break

    return itemsPicked, profit


def knapsackDp(totalcount, profits, weights, maxweight):
    items = [[0 for x in range(maxweight+1)] for i in range(totalcount+1)]

    for i in range(totalcount+1):
        for w in range(maxweight+1):
            if i == 0 or w == 0:
                items[i][w] = 0
            elif weights[i-1] <= w:
                items[i][w] = max(profits[i-1] + items[i-1][w-weights[i-1]],  items[i-1][w])
            else:
                items[i][w] = items[i-1][w]

    return items[totalcount][maxweight]
