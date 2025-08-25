import json
import os

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, last_three_digits):
    """
    Ham giai bai toan chinh - tim SIM theo 3 so cuoi.
    
    Args:
        data_json: du lieu JSON da load (chua sim va price).
        last_three_digits: 3 so cuoi can tim (string).
    
    Returns:
        list: danh sach ket qua (string) tuong ung voi tung SIM tim duoc.
    """
    results = []
    
    # Tao dictionary de tra cuu gia theo type nhanh hon
    price_dict = {}
    for price_info in data_json["price"]:
        price_dict[price_info["type"]] = price_info["price"]
    
    # Duyet qua tat ca SIM de tim nhung SIM co 3 so cuoi khop
    for sim in data_json["sim"]:
        sim_number = sim["number"]
        if sim_number.endswith(last_three_digits):
            # Lay thong tin SIM
            network = sim["network"]
            active = str(sim["active"]).lower()  # chuyen ve lowercase string
            sim_type = sim["type"]
            price = price_dict.get(sim_type, 0)  # lay gia theo type
            
            # Format ket qua: <so> <nha mang> <trang thai> <gia>
            result_line = f"{sim_number} {network} {active} {price}"
            results.append(result_line)
    
    return results

def main():
    """
    Ham chinh: doc input tu ban phim va xu ly.
    """
    try:
        # 1. Load du lieu JSON
        data_json = load_json("./data/datas.json")
        
        # 2. Nhap 3 so cuoi tu ban phim
        last_three_digits = input().strip()
        
        # 3. Giai bai toan
        results = solve(data_json, last_three_digits)
        
        # 4. In ket qua
        for result in results:
            print(result)
            
    except FileNotFoundError:
        print("Khong tim thay file datas.json")
    except KeyError as e:
        print(f"Loi cau truc du lieu JSON: {e}")
    except Exception as e:
        print(f"Loi: {e}")

if __name__ == "__main__":
    main()