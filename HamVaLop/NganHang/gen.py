import os

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

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Tìm và trả về danh sách tất cả các file .in trong thư mục đó.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    Giữ nguyên phần này cho các bài sau, trừ khi định dạng input/output thay đổi.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        B = int(lines[0])
        N = int(lines[1])
        data = [B, N]
        
        for i in range(2, 2 + N):
            parts = lines[i].split()
            operation = parts[0]
            amount = int(parts[1])
            data.extend([operation, amount])
        
        # Gọi hàm giải
        res = solve(data)
        # Ghi kết quả ra file output
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    """
    Hàm chính: tìm các file input, xử lý từng file, tạo file output.
    """
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()