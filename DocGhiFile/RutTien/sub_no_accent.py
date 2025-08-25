import json

def load_json(file_path):
    """Doc file JSON va tra ve du lieu."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve():
    """Ham giai bai toan chinh."""
    # Doc du lieu tu file JSON
    data = load_json("./data/datas.json")
    transactions = data["transactions"]
    
    # Tinh so du tai khoan tu cac giao dich completed
    balance = 0
    for transaction in transactions:
        if transaction["status"] == "completed":
            if transaction["type"] == "deposit":
                balance += transaction["amount"]
            elif transaction["type"] == "withdrawal":
                balance -= transaction["amount"]
    
    # Doc so test case tu ban phim
    t = int(input())
    
    # In so du tai khoan
    print(balance)
    
    # Xu ly tung test case
    for _ in range(t):
        query_type, query_status = input().split()
        
        # Tim cac giao dich thoa man dieu kien
        matching_ids = []
        for transaction in transactions:
            if transaction["type"] == query_type and transaction["status"] == query_status:
                matching_ids.append(transaction["id"])
        
        # Sap xep theo id tang dan va in ra
        matching_ids.sort()
        if matching_ids:
            print(" ".join(map(str, matching_ids)))
        else:
            print("")  # In dong trong neu khong co giao dich nao

if __name__ == "__main__":
    solve()