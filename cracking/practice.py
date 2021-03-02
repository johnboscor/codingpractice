change = [25, 10, 5, 1]

def minCoins(money):
    if money <= 0:
        return 0
    if mc[money] != 0:
        return mc[money]
    min_coins = float('inf')
    for c in change:
        if money - c >= 0:
            curr_min = minCoins(money - c)
            if curr_min < min_coins:
                min_coins = curr_min
    mc[money] = min_coins + 1
    return mc[money]

my_money = 101

mc = [0 for i in range(my_money+1)]

print(minCoins(my_money))