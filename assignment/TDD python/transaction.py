def calculate_balance(transaction):
    if len(transaction) == 0:
        return 0
    balance = 0
    for amounts in transaction:
        balance = balance + amounts
    return balance

print(calculate_balance([10, 20, -3, 4]))
print(calculate_balance([]))
