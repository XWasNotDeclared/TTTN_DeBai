import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, last_three_digits):
    """
    Hàm giải bài toán chính - tìm SIM theo 3 số cuối.
    
    Args:
        data_json: dữ liệu JSON đã load (chứa sim và price).
        last_three_digits: 3 số cuối cần tìm (string).
    
    Returns:
        list: danh sách kết quả (string) tương ứng với từng SIM tìm được.
    """
    results = []
    
    # Tạo dictionary để tra cứu giá theo type nhanh hơn
    price_dict = {}
    for price_info in data_json["price"]:
        price_dict[price_info["type"]] = price_info["price"]
    
    # Duyệt qua tất cả SIM để tìm những SIM có 3 số cuối khớp
    for sim in data_json["sim"]:
        sim_number = sim["number"]
        if sim_number.endswith(last_three_digits):
            # Lấy thông tin SIM
            network = sim["network"]
            active = str(sim["active"]).lower()  # chuyển về lowercase string
            sim_type = sim["type"]
            price = price_dict.get(sim_type, 0)  # lấy giá theo type
            
            # Format kết quả: <số> <nhà mạng> <trạng thái> <giá>
            result_line = f"{sim_number} {network} {active} {price}"
            results.append(result_line)
    
    return results

def main():
    """
    Hàm chính: đọc input từ bàn phím và xử lý.
    """
    try:
        # 1. Load dữ liệu JSON
        data_json = load_json("./data/datas.json")
        
        # 2. Nhập 3 số cuối từ bàn phím
        last_three_digits = input().strip()
        
        # 3. Giải bài toán
        results = solve(data_json, last_three_digits)
        
        # 4. In kết quả
        for result in results:
            print(result)
            
    except FileNotFoundError:
        print("Không tìm thấy file datas.json")
    except KeyError as e:
        print(f"Lỗi cấu trúc dữ liệu JSON: {e}")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()