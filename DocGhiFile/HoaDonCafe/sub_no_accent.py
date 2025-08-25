import json

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    # Doc du lieu tu file JSON
    data = load_json("./data/datas.json")
    coffee_shop = data["coffee_shop"]
    
    # Tao dictionary de tra cuu gia nhanh
    menu_dict = {}
    for item in coffee_shop["menu"]:
        menu_dict[item["item"]] = item["price"]
    
    # Doc so luong query
    Q = int(input())
    
    # Dictionary de luu cac mon da order
    orders = {}
    
    # Doc cac query
    for _ in range(Q):
        line = input().strip()
        parts = line.rsplit(' ', 1)  # Tach tu cuoi de tranh loi voi ten mon co nhieu tu
        
        if len(parts) != 2:
            continue
            
        ten_mon = parts[0]
        try:
            so_luong = int(parts[1])
        except ValueError:
            continue
        
        # Kiem tra mon co trong menu khong
        if ten_mon in menu_dict:
            if ten_mon in orders:
                orders[ten_mon] += so_luong
            else:
                orders[ten_mon] = so_luong
    
    # In hoa don
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