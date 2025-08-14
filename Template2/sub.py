import json

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    
    Args:
        file_path (str): đường dẫn tới file JSON.
    
    Returns:
        dict hoặc list: dữ liệu JSON.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, data_input):
    """
    Hàm giải bài toán chính.
    
    Args:
        data_json: dữ liệu đã load từ file JSON.
        data_input: dữ liệu nhập từ bàn phím (list, str, số, tuỳ bài).
    
    Returns:
        list: danh sách các kết quả (string hoặc số) cho mỗi test case.
    """
    # TODO: Viết logic xử lý bài toán ở đây
    # Ví dụ:
    # - Lọc hoặc tính toán dựa trên data_json
    # - Sử dụng data_input làm input từ người dùng
    # - Lưu kết quả từng test case vào list
    results = []
    
    return results

def main():
    # 1. Load dữ liệu JSON
    data_json = load_json("./data/file.json")  # đổi đường dẫn file nếu cần
    
    # 2. Nhập dữ liệu từ bàn phím
    # Ví dụ: nhập t số test case và dữ liệu kèm theo
    t = int(input().strip())
    data_input = []
    for _ in range(t):
        # tuỳ bài: nhập từng dòng, split, map sang int/float...
        line = input().strip()
        data_input.append(line)
    
    # 3. Gọi hàm solve
    res = solve(data_json, data_input)
    
    # 4. In kết quả
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()
