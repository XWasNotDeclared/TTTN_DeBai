import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_students(students, gender, class_name):
    """Lọc học sinh theo giới tính và lớp"""
    filtered = []
    for student in students:
        if student['gender'] == gender and student['class'] == class_name:
            filtered.append(student)
    return filtered

def calculate_math_statistics(students):
    """Tính thống kê điểm toán: sum, avg, max, min"""
    if not students:
        return 0.00, 0.00, 0.00, 0.00
    
    math_scores = [student['math'] for student in students]
    
    total = sum(math_scores)
    average = total / len(math_scores)
    maximum = max(math_scores)
    minimum = min(math_scores)
    
    return total, average, maximum, minimum

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính.
    
    Args:
        data_json: dữ liệu JSON đã load (danh sách học sinh).
        input_data: dữ liệu input từ file .in, dạng list các dòng.
    
    Returns:
        list: danh sách kết quả (string) tương ứng với từng test case.
    """
    results = []
    
    # Dòng đầu tiên là số test case
    T = int(input_data[0])
    
    # Xử lý từng test case
    for i in range(1, T + 1):
        line = input_data[i].strip().split()
        gender = line[0]
        class_name = line[1]
        
        # Lọc học sinh theo điều kiện
        filtered_students = filter_students(data_json, gender, class_name)
        
        # Tính thống kê điểm toán
        total, avg, maximum, minimum = calculate_math_statistics(filtered_students)
        
        # Định dạng kết quả với 2 chữ số thập phân
        result = f"{total:.2f} {avg:.2f} {maximum:.2f} {minimum:.2f}"
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
        # Đọc dữ liệu file .in
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
    data_json = load_json("./data/students.json")  # đường dẫn file JSON
    
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