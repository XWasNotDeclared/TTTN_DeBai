import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính.
    
    Args:
        data_json: dữ liệu JSON đã load.
        input_data: dữ liệu input từ file .in, dạng list các dòng.
    
    Returns:
        list: danh sách kết quả (string) tương ứng với output.
    """
    coffee_shop = data_json["coffee_shop"]
    
    # Tạo dictionary để tra cứu giá nhanh
    menu_dict = {}
    for item in coffee_shop["menu"]:
        menu_dict[item["item"]] = item["price"]
    
    # Đọc số lượng query từ dòng đầu
    Q = int(input_data[0])
    
    # Dictionary để lưu các món đã order
    orders = {}
    
    # Xử lý các query
    for i in range(1, min(Q + 1, len(input_data))):
        line = input_data[i].strip()
        if not line:
            continue
            
        parts = line.rsplit(' ', 1)  # Tách từ cuối
        
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
    
    # Tạo kết quả
    results = []
    results.append(coffee_shop["name"])
    
    total = 0
    for ten_mon, so_luong in orders.items():
        gia = menu_dict[ten_mon]
        thanh_tien = gia * so_luong
        total += thanh_tien
        results.append(f"{ten_mon} x {so_luong} = {thanh_tien}")
    
    results.append(f"Tong: {total}")
    
    return results

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Trả về danh sách file .in trong thư mục.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile, data_json):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    
    Args:
        infile: tên file input
        data_json: dữ liệu từ JSON
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Processing {infile} -> {outfile} ...")
    
    with open(infile, "r", encoding="utf-8") as fin, open(outfile, "w", encoding="utf-8") as fout:
        # Đọc dữ liệu file .in
        input_data = [line.strip() for line in fin]
        
        # Gọi hàm solve
        res = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        fout.write("\n".join(res) + "\n")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    # 1. Load dữ liệu JSON
    data_json = load_json("./data/datas.json")
    
    # 2. Chuẩn bị danh sách file input
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    
    # 3. Xử lý từng file
    for infile in sorted(in_files):
        process_file(infile, data_json)

if __name__ == "__main__":
    main()