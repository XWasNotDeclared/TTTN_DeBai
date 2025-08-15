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
        list: danh sách kết quả (string hoặc số) tương ứng với từng test case.
    """
    results = []
    
    # Đọc số lượng test case
    t = int(input_data[0])
    
    # Xử lý từng test case
    line_idx = 1
    for _ in range(t):
        # Đọc id sản phẩm
        product_id = int(input_data[line_idx])
        line_idx += 1
        
        # Đọc 4 dự đoán
        guesses = list(map(int, input_data[line_idx].split()))
        line_idx += 1
        
        # Tìm giá thật của sản phẩm
        real_price = None
        for product in data_json:
            if product["id"] == product_id:
                real_price = product["price"]
                break
        
        if real_price is None:
            results.append(-1)
            continue
        
        # Tìm người thắng
        winner = -1
        best_guess = -1
        
        for i in range(4):
            guess = guesses[i]
            # Chỉ xét những dự đoán <= giá thật
            if guess <= real_price:
                # Nếu đây là dự đoán tốt hơn (gần giá thật hơn)
                if guess > best_guess:
                    best_guess = guess
                    winner = i + 1  # Người chơi đánh số từ 1
        
        results.append(winner)
    
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
        # Đọc dữ liệu file .in theo định dạng bài
        input_data = [line.strip() for line in fin]
        
        # Gọi hàm solve
        res = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    # 1. Load dữ liệu JSON
    data_json = load_json("./data/datas.json")  # đường dẫn file JSON theo đề bài
    
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