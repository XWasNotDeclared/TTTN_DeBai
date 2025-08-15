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
        input_data: dữ liệu input từ file .in, dạng list các dòng hoặc các giá trị đã split.
    
    Returns:
        list: danh sách kết quả (string hoặc số) tương ứng với từng test case.
    """
    results = []
    
    # Lấy ngưỡng tốc độ gió từ input_data
    wind_threshold = int(input_data[0].strip())
    
    # 1. Tìm thành phố có nhiệt độ cao nhất
    max_temp_city = max(data_json, key=lambda x: x['temperature_celsius'])
    results.append(max_temp_city['city'])
    
    # 2. Tìm thành phố có độ ẩm thấp nhất  
    min_humidity_city = min(data_json, key=lambda x: x['humidity_percent'])
    results.append(min_humidity_city['city'])
    
    # 3. Tìm các thành phố có tốc độ gió > W, sắp xếp giảm dần theo tốc độ gió
    high_wind_cities = [city for city in data_json if city['wind_kmh'] > wind_threshold]
    
    if high_wind_cities:
        # Sắp xếp theo tốc độ gió giảm dần
        high_wind_cities.sort(key=lambda x: x['wind_kmh'], reverse=True)
        for city in high_wind_cities:
            results.append(city['city'])
    else:
        results.append("None")
    
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
        # Đọc dữ liệu file .in theo định dạng bài (một dòng chứa số nguyên W)
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