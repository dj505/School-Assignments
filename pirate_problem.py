amount = 16
loops_brother = 3

def check_if_divisible(amount):
    if amount % 3 - 1 == 0:
        return True
    else:
        return False

def divide(amount):
    amount = amount * 3 + 1
    print(amount)

def do_division(amount, loops_brother):
    if check_if_divisible(amount) == True:
        divide(amount)
    else:
        print('Not further divisible')

while loops_brother <= 3:
    do_division(amount, loops_brother)
    loops_brother += 1
