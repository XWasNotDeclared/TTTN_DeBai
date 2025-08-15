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
    transactions = data_json["transactions"]
    
    # Tính số dư tài khoản từ các giao dịch completed
    balance = 0
    for transaction in transactions:
        if transaction["status"] == "completed":
            if transaction["type"] == "deposit":
                balance += transaction["amount"]
            elif transaction["type"] == "withdrawal":
                balance -= transaction["amount"]
    
    # Đọc số test case
    t = int(input_data[0])
    
    results = [str(balance)]  # Dòng đầu tiên là số dư
    
    # Xử lý từng test case
    for i in range(1, t + 1):
        query_type, query_status = input_data[i].split()
        
        # Tìm các giao dịch thỏa mãn điều kiện
        matching_ids = []
        for transaction in transactions:
            if transaction["type"] == query_type and transaction["status"] == query_status:
                matching_ids.append(transaction["id"])
        
        # Sắp xếp theo id tăng dần
        matching_ids.sort()
        if matching_ids:
            results.append(" ".join(map(str, matching_ids)))
        else:
            results.append("")  # Dòng trống nếu không có giao dịch nào
    
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
        results = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        fout.write("\n".join(results) + "\n")

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