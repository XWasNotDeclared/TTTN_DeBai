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
        list: danh sách kết quả (string) tương ứng với từng test case.
    """
    devices = data_json["devices"]
    results = []
    
    # Đọc số test case
    t = int(input_data[0].strip())
    line_idx = 1
    
    for i in range(t):
        # Đọc thông số chuẩn cho test case này
        line = input_data[line_idx].strip()
        target_temp, target_humidity, target_light = map(float, line.split())
        line_idx += 1
        
        # Sắp xếp thiết bị theo ID tăng dần
        sorted_devices = sorted(devices, key=lambda x: x["id"])
        
        # Thêm dòng trắng giữa các test case (trừ test case đầu)
        if i > 0:
            results.append("")
        
        # Xử lý từng thiết bị
        for device in sorted_devices:
            device_id = device["id"]
            current_temp = device["nhiet_do"]
            current_humidity = device["do_am"]
            current_light = device["anh_sang"]
            
            # Tính delta (cần tăng/giảm)
            delta_temp = target_temp - current_temp
            delta_humidity = target_humidity - current_humidity
            delta_light = target_light - current_light
            
            # Làm tròn đến 1 chữ số thập phân
            delta_temp = round(delta_temp, 1)
            delta_humidity = round(delta_humidity, 1)
            delta_light = round(delta_light, 1)
            
            # Format output: id delta_T delta_D delta_A
            result_line = f"{device_id} {delta_temp} {delta_humidity} {delta_light}"
            results.append(result_line)
    
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
        for line in res:
            fout.write(line + "\n")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    # 1. Load dữ liệu JSON
    try:
        data_json = load_json("./data/datas.json")
    except FileNotFoundError:
        print("Không tìm thấy file ./data/datas.json")
        return
    except json.JSONDecodeError:
        print("File JSON không hợp lệ")
        return
    
    # 2. Chuẩn bị danh sách file input
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    
    # 3. Xử lý từng file
    for infile in sorted(in_files):
        try:
            process_file(infile, data_json)
        except Exception as e:
            print(f"Lỗi khi xử lý file {infile}: {e}")

if __name__ == "__main__":
    main()