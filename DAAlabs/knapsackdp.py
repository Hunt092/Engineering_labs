def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


def takeItems(weight, value):
    id = len(weight)+1
    profitOfItem = int(input("Enter profit for id- %s : " % id))
    wiegthOfItem = int(input("Enter weight for id-%s : " % id))
    weight.append(wiegthOfItem)
    value.append(profitOfItem)


if __name__ == "__main__":
    maxWeight = int(input("Enter Max weight of the sack: "))
    noItems = int(input("Enter total number of items: "))
    weight = []
    value = []
    for _ in range(noItems):
        takeItems(weight, value)
    print(knapSack(maxWeight, weight, value, noItems))
