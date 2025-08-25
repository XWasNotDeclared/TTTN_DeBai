class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited: {amount}, New Balance: {self.__balance}"
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return f"Withdrew: {amount}, Remaining Balance: {self.__balance}"
        else:
            return "Insufficient funds"

def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach so nguyen hoac chuoi da duoc doc tu input.
    - TODO: Viet logic giai o day.
    - Tra ve: list (hoac iterable) chua cac dong ket qua (string hoac so).
    """
    B = data[0]  # So du ban dau
    N = data[1]  # So luong giao dich
    
    account = Account(B)
    result = []
    
    idx = 2
    for _ in range(N):
        operation = data[idx]
        amount = data[idx + 1]
        idx += 2
        
        if operation == 'D':
            result.append(account.deposit(amount))
        elif operation == 'W':
            result.append(account.withdraw(amount))
    
    return result

def main():
    data = []
    B = int(input().strip())  # so du ban dau
    N = int(input().strip())  # so luong giao dich
    data.extend([B, N])
    
    for _ in range(N):
        parts = input().strip().split()
        operation = parts[0]  # 'D' hoac 'W'
        amount = int(parts[1])
        data.extend([operation, amount])
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()