import json

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    # Đọc dữ liệu từ file JSON
    data = load_json("./data/datas.json")
    coffee_shop = data["coffee_shop"]
    
    # Tạo dictionary để tra cứu giá nhanh
    menu_dict = {}
    for item in coffee_shop["menu"]:
        menu_dict[item["item"]] = item["price"]
    
    # Đọc số lượng query
    Q = int(input())
    
    # Dictionary để lưu các món đã order
    orders = {}
    
    # Đọc các query
    for _ in range(Q):
        line = input().strip()
        parts = line.rsplit(' ', 1)  # Tách từ cuối để tránh lỗi với tên món có nhiều từ
        
        if len(parts) != 2:
            continue
            
        ten_mon = parts[0]
        try:
            so_luong = int(parts[1])
        except ValueError:
            continue
        
        # Kiểm tra món có trong menu không
        if ten_mon in menu_dict:
            if ten_mon in orders:
                orders[ten_mon] += so_luong
            else:
                orders[ten_mon] = so_luong
    
    # In hóa đơn
    print(coffee_shop["name"])
    
    total = 0
    for ten_mon, so_luong in orders.items():
        gia = menu_dict[ten_mon]
        thanh_tien = gia * so_luong
        total += thanh_tien
        print(f"{ten_mon} x {so_luong} = {thanh_tien}")
    
    print(f"Tong: {total}")

if __name__ == "__main__":
    main()