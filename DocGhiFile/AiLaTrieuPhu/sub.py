import json
import sys

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}")
        sys.exit(1)

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
    
    last_correct = 0  # Câu đúng cuối cùng (0-indexed trong safe_points)
    
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

def main():
    """
    Hàm chính: đọc input từ bàn phím và file JSON, xử lý và in kết quả.
    """
    # Load dữ liệu JSON
    data_json = load_json("./data/datas.json")
    
    # Đọc số test case
    t = int(input().strip())
    
    results = []
    for _ in range(t):
        # Đọc một dòng input cho test case
        line = input().strip().split()
        quiz_id = int(line[0])
        answers = line[1:]  # Danh sách câu trả lời
        
        # Giải test case
        result = solve_millionaire(data_json, quiz_id, answers)
        results.append(result)
    
    # In kết quả
    for result in results:
        print(result)

if __name__ == "__main__":
    main()