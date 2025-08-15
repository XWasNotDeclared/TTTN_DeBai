import json

def load_json(file_path):
    """Đọc file JSON và trả về dữ liệu."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve():
    """Hàm giải bài toán chính."""
    # Đọc dữ liệu từ file JSON
    data = load_json("./data/datas.json")
    transactions = data["transactions"]
    
    # Tính số dư tài khoản từ các giao dịch completed
    balance = 0
    for transaction in transactions:
        if transaction["status"] == "completed":
            if transaction["type"] == "deposit":
                balance += transaction["amount"]
            elif transaction["type"] == "withdrawal":
                balance -= transaction["amount"]
    
    # Đọc số test case từ bàn phím
    t = int(input())
    
    # In số dư tài khoản
    print(balance)
    
    # Xử lý từng test case
    for _ in range(t):
        query_type, query_status = input().split()
        
        # Tìm các giao dịch thỏa mãn điều kiện
        matching_ids = []
        for transaction in transactions:
            if transaction["type"] == query_type and transaction["status"] == query_status:
                matching_ids.append(transaction["id"])
        
        # Sắp xếp theo id tăng dần và in ra
        matching_ids.sort()
        if matching_ids:
            print(" ".join(map(str, matching_ids)))
        else:
            print("")  # In dòng trống nếu không có giao dịch nào

if __name__ == "__main__":
    solve()