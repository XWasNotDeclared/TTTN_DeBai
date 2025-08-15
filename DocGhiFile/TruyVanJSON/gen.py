import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def query_json(data, path):
    """
    Truy vấn dữ liệu JSON theo đường dẫn.
    
    Args:
        data: dữ liệu JSON
        path: đường dẫn truy vấn (string)
    
    Returns:
        tuple: (result, status) 
        - result: giá trị tìm được hoặc None
        - status: "found", "invalid", "not_found"
    """
    if not path:
        return data, "invalid" if isinstance(data, (dict, list)) else "found"
    
    parts = path.split('/')
    current = data
    
    try:
        for part in parts:
            if isinstance(current, dict):
                if part in current:
                    current = current[part]
                else:
                    return None, "not_found"
            else:
                return None, "not_found"
        
        # Kiểm tra kết quả cuối cùng
        if isinstance(current, (dict, list)):
            return current, "invalid"
        else:
            return current, "found"
            
    except (KeyError, TypeError):
        return None, "not_found"

def solve_single_query(data_json, query):
    """
    Giải một truy vấn đơn.
    
    Args:
        data_json: dữ liệu JSON
        query: truy vấn dạng "GET path"
    
    Returns:
        string: kết quả truy vấn
    """
    if not query.startswith("GET "):
        return "Invalid query"
    
    path = query[4:].strip()  # Bỏ "GET " ở đầu
    result, status = query_json(data_json, path)
    
    if status == "found":
        return str(result)
    elif status == "invalid":
        return "Invalid query"
    else:
        return "Not found"

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính.
    
    Args:
        data_json: dữ liệu JSON đã load.
        input_data: dữ liệu input từ file .in, dạng list các dòng.
    
    Returns:
        list: danh sách kết quả (string) tương ứng với từng truy vấn.
    """
    results = []
    for query in input_data:
        query = query.strip()
        if query:  # Bỏ qua dòng trống
            result = solve_single_query(data_json, query)
            results.append(result)
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
        # Đọc dữ liệu file .in - mỗi dòng là một truy vấn
        input_data = [line.strip() for line in fin if line.strip()]
        
        # Gọi hàm solve
        results = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        if results:
            fout.write("\n".join(results) + "\n")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    # 1. Load dữ liệu JSON
    json_file = "./data/datas.json"
    if not os.path.exists(json_file):
        print(f"Không tìm thấy file JSON: {json_file}")
        return
    
    data_json = load_json(json_file)
    
    # 2. Chuẩn bị danh sách file input
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    
    # 3. Xử lý từng file
    for infile in sorted(in_files):
        process_file(infile, data_json)
    
    print("Hoàn thành xử lý tất cả file test!")

if __name__ == "__main__":
    main()