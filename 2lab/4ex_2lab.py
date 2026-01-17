def main():
    try:
        with open("4ex.txt") as f:
            names = f.readline().split()
            n = int(f.readline().strip())

            expenses = {name: 0.0 for name in names}

            for i in range(n):
                line = f.readline().strip()
                if not line:
                    continue
                name, amount = line.split()
                expenses[name] += float(amount)

    except FileNotFoundError:
        print("Файл 4.txt не найден")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    total_expenses = sum(expenses.values())
    average = total_expenses / len(names)

    balances = []
    for name in names:
        balance = expenses[name] - average
        balance = round(balance, 10)
        balances.append((name, balance))

    balances.sort()

    transactions = []
    left = 0
    right = len(balances) - 1

    while left < right:
        debtor_name, debtor_balance = balances[left]
        creditor_name, creditor_balance = balances[right]

        if abs(debtor_balance) < 1e-9:
            left += 1
            continue
        if abs(creditor_balance) < 1e-9:
            right -= 1
            continue

        amount = min(-debtor_balance, creditor_balance)
        amount = round(amount, 2)

        if amount < 0.01:
            if abs(debtor_balance) < abs(creditor_balance):
                left += 1
            else:
                right -= 1
            continue

        transactions.append((debtor_name, creditor_name, amount))

        debtor_balance = round(debtor_balance + amount, 10)
        creditor_balance = round(creditor_balance - amount, 10)

        balances[left] = (debtor_name, debtor_balance)
        balances[right] = (creditor_name, creditor_balance)

        if abs(debtor_balance) < 1e-9:
            left += 1
        if abs(creditor_balance) < 1e-9:
            right -= 1

    print(len(transactions))
    for debtor, creditor, amount in transactions:
        print(f"{debtor} {creditor} {amount:.2f}")


if __name__ == "__main__":
    main()