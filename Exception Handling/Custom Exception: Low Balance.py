class LowBalanceError(Exception):
    pass

try:
    balance = float(input("Enter account balance: "))
    if balance < 500:
        raise LowBalanceError("Balance too low for transaction!")
    print("Transaction approved")
except LowBalanceError as e:
    print("Error:", e)

# output:
# Enter account balance: 5000
# Transaction approved
