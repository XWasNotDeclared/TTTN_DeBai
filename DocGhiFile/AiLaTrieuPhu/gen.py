import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_millionaire(data_json, quiz_id, answers):
    """
    Giải bài toán Ai Là Triệu Phú cho một test case.
    
    Args:
        data_json: dữ liệu JSON đã load
        quiz_id: id bộ câu hỏi
        answers: danh sách câu trả lời ['A', 'C', 'B', ...]
    
    Returns:
        int: số tiền thưởng nhận được
    """
    # Tìm bộ câu hỏi theo id
    quiz_set = None
    for quiz in data_json["quiz_sets"]:
        if quiz["id"] == quiz_id:
            quiz_set = quiz
            break
    
    if not quiz_set:
        return 0
    
    # Tạo dictionary prizes theo question_id
    prize_dict = {}
    for prize in data_json["prizes"]:
        prize_dict[prize["question_id"]] = prize["amount"]
    
    # Mốc an toàn: câu 0, 5, 10
    safe_points = {0: 0, 5: prize_dict[5], 10: prize_dict[10]}
    
    last_correct = 0  # Câu đúng cuối cùng
    
    # Xử lý từng câu trả lời
    for i, answer in enumerate(answers):
        question_num = i + 1  # Câu hỏi từ 1-15
        
        if answer == 'X':
            # Bỏ cuộc, nhận tiền của câu đúng gần nhất
            return prize_dict[last_correct] if last_correct > 0 else 0
        
        # Kiểm tra đáp án đúng
        correct_answer = quiz_set["questions"][i]["correct"]
        
        if answer == correct_answer:
            # Đúng, cập nhật last_correct
            last_correct = question_num
        else:
            # Sai, về mốc an toàn
            if question_num <= 5:
                return safe_points[0]
            elif question_num <= 10:
                return safe_points[5]
            else:
                return safe_points[10]
    
    # Nếu đúng hết hoặc đúng đến câu cuối cùng được trả lời
    return prize_dict[last_correct] if last_correct > 0 else 0

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
    
    # Đọc số test case
    t = int(input_data[0].strip())
    
    # Xử lý từng test case
    for i in range(1, t + 1):
        line = input_data[i].strip().split()
        quiz_id = int(line[0])
        answers = line[1:]  # Danh sách câu trả lời
        
        # Giải test case
        result = solve_millionaire(data_json, quiz_id, answers)
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