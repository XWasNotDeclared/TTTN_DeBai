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
    Hàm giải bài toán chính.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - TODO: Viết logic giải ở đây.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    """
    B = data[0]  # Số dư ban đầu
    N = data[1]  # Số lượng giao dịch
    
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
    B = int(input().strip())  # số dư ban đầu
    N = int(input().strip())  # số lượng giao dịch
    data.extend([B, N])
    
    for _ in range(N):
        parts = input().strip().split()
        operation = parts[0]  # 'D' hoặc 'W'
        amount = int(parts[1])
        data.extend([operation, amount])
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()