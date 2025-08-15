import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_bmi_status(weight_kg, height_m):
    """
    Tính BMI và trả về trạng thái tương ứng.
    """
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        return 1
    elif 18.5 <= bmi < 25:
        return 2
    elif 25 <= bmi < 30:
        return 3
    else:  # bmi >= 30
        return 4

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính.
    
    Args:
        data_json: dữ liệu JSON đã load.
        input_data: dữ liệu input từ file .in, dạng list các dòng.
    
    Returns:
        list: danh sách kết quả tương ứng với từng test case.
    """
    # Tạo dictionary để tra cứu nhanh theo id
    person_dict = {person["id"]: person for person in data_json}
    
    # Parse input data
    n = int(input_data[0])
    ids = list(map(int, input_data[1].split()))
    
    results = []
    
    for person_id in ids:
        if person_id in person_dict:
            person = person_dict[person_id]
            status = calculate_bmi_status(person["weight_kg"], person["height_m"])
            results.append(f"{person_id} {status}")
        else:
            results.append(f"{person_id} NOT FOUND")
    
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
    
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu file .in theo định dạng bài
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
    data_json = load_json("./data/datas.json")  # đúng tên file theo đề bài
    
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