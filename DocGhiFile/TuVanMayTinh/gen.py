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
    computers = data_json
    
    # Đọc số lượng test case
    t = int(input_data[0])
    
    for i in range(1, t + 1):
        line = input_data[i].strip()
        cpu, ram, ssd = line.split()
        
        # Tìm máy tính phù hợp
        matching_computers = []
        
        for computer in computers:
            if (computer["cpu"] == cpu and 
                computer["ram"] == ram and 
                computer["ssd"] == ssd):
                matching_computers.append(computer)
        
        if not matching_computers:
            results.append("Khong co may nao phu hop")
        else:
            # Sắp xếp theo giá tăng dần
            matching_computers.sort(key=lambda x: x["gia"])
            
            for computer in matching_computers:
                result_line = f"{computer['ten']} {computer['cpu']} {computer['ram']} {computer['ssd']} {computer['gia']}"
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
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    # 1. Load dữ liệu JSON
    data_json = load_json("./data/datas.json")  # đường dẫn file JSON
    
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