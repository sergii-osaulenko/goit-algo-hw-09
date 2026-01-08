coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    remaining = amount
    for c in sorted(coins, reverse=True):
        if remaining >= c:
            count = remaining // c
            result[c] = count
            remaining -= count * c
    return result

def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
    if dp[amount] == float('inf'):
        return {}
    
    # Реконструкція
    result = {}
    remaining = amount
    for c in sorted(coins, reverse=True):
        while remaining >= c and dp[remaining] == dp[remaining - c] + 1:
            result[c] = result.get(c, 0) + 1
            remaining -= c
    return result