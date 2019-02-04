# Incomplete

coins = 997
splits = 0

def split(coins):
    removed = coins // 3 - 1
    coins = coins - removed
    return coins

while coins > 0:
    lastval = coins
    print('Split #{}'.format(splits))
    print('Amount: {}'.format(coins))
    coins = split(coins)
    splits += 1
    if lastval == coins:
        break
