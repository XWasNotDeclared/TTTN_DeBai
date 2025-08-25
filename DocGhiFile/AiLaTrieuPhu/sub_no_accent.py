import json
import sys

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}")
        sys.exit(1)

def solve_millionaire(data_json, quiz_id, answers):
    """
    Giai bai toan Ai La Trieu Phu cho mot test case.
    
    Args:
        data_json: du lieu JSON da load
        quiz_id: id bo cau hoi
        answers: danh sach cau tra loi ['A', 'C', 'B', ...]
    
    Returns:
        int: so tien thuong nhan duoc
    """
    # Tim bo cau hoi theo id
    quiz_set = None
    for quiz in data_json["quiz_sets"]:
        if quiz["id"] == quiz_id:
            quiz_set = quiz
            break
    
    if not quiz_set:
        return 0
    
    # Tao dictionary prizes theo question_id
    prize_dict = {}
    for prize in data_json["prizes"]:
        prize_dict[prize["question_id"]] = prize["amount"]
    
    # Moc an toan: cau 0, 5, 10
    safe_points = {0: 0, 5: prize_dict[5], 10: prize_dict[10]}
    
    last_correct = 0  # Cau dung cuoi cung (0-indexed trong safe_points)
    
    # Xu ly tung cau tra loi
    for i, answer in enumerate(answers):
        question_num = i + 1  # Cau hoi tu 1-15
        
        if answer == 'X':
            # Bo cuoc, nhan tien cua cau dung gan nhat
            return prize_dict[last_correct] if last_correct > 0 else 0
        
        # Kiem tra dap an dung
        correct_answer = quiz_set["questions"][i]["correct"]
        
        if answer == correct_answer:
            # Dung, cap nhat last_correct
            last_correct = question_num
        else:
            # Sai, ve moc an toan
            if question_num <= 5:
                return safe_points[0]
            elif question_num <= 10:
                return safe_points[5]
            else:
                return safe_points[10]
    
    # Neu dung het hoac dung den cau cuoi cung duoc tra loi
    return prize_dict[last_correct] if last_correct > 0 else 0

def main():
    """
    Ham chinh: doc input tu ban phim va file JSON, xu ly va in ket qua.
    """
    # Load du lieu JSON
    data_json = load_json("./data/datas.json")
    
    # Doc so test case
    t = int(input().strip())
    
    results = []
    for _ in range(t):
        # Doc mot dong input cho test case
        line = input().strip().split()
        quiz_id = int(line[0])
        answers = line[1:]  # Danh sach cau tra loi
        
        # Giai test case
        result = solve_millionaire(data_json, quiz_id, answers)
        results.append(result)
    
    # In ket qua
    for result in results:
        print(result)

if __name__ == "__main__":
    main()