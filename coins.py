import timeit

# Набір монет
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    # Жадібний алгоритм для видачі решти - обирає найбільший можливий номінал на кожному кроці
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin  # Скільки монет цього номіналу вміщується
            if count > 0:
                result[coin] = count
                amount = amount - (coin * count)
        if amount == 0:
            break
    return result

def find_min_coins(amount):
    # Алгоритм динамічного програмування - знаходить справді мінімальну кількість монет
    # dp[i] буде зберігати мінімальну кількість монет для суми i
    # Ініціалізуємо нескінченністю, крім 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Для відновлення результату запам'ятовуємо, яку монету додали останньою
    last_coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    last_coin_used[i] = coin

    # Якщо рішення не знайдено (для даного набору монет це неможливо, але для загального випадку)
    if dp[amount] == float('inf'):
        return {}

    # Відновлення результату (зворотний хід)
    result = {}
    current_sum = amount
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_sum -= coin

    return result

# Блок тестування та порівняння
if __name__ == "__main__":
    test_amount = 113
    print(f"Сума: {test_amount}")
    print(f"Жадібний: {find_coins_greedy(test_amount)}")
    print(f"Динамічний: {find_min_coins(test_amount)}")
    print("-" * 20)

    # Тест на великій сумі для порівняння часу
    large_sum = 5000 # Це значення можна змінити на 10000 або більше
    print(f"Тестування на сумі: {large_sum}")
    
    time_greedy = timeit.timeit(lambda: find_coins_greedy(large_sum), number=100)
    time_dp = timeit.timeit(lambda: find_min_coins(large_sum), number=100)
    
    print(f"Час виконання (Жадібний): {time_greedy:.6f} сек")
    print(f"Час виконання (DP):       {time_dp:.6f} сек")