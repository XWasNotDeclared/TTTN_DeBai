import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_rectangle_by_id(rectangles, target_id):
    """Tìm hình chữ nhật theo id."""
    for rect in rectangles:
        if rect["id"] == target_id:
            return rect
    return None

def calculate_intersection(rect1, rect2):
    """
    Tính giao của hai hình chữ nhật.
    
    Args:
        rect1, rect2: dictionary chứa thông tin hình chữ nhật
        
    Returns:
        tuple: (x, y, width, height) nếu có giao, None nếu không giao
    """
    # Tọa độ góc trên trái và dưới phải của rect1
    x1_left, y1_top = rect1["x"], rect1["y"]
    x1_right, y1_bottom = x1_left + rect1["width"], y1_top + rect1["height"]
    
    # Tọa độ góc trên trái và dưới phải của rect2
    x2_left, y2_top = rect2["x"], rect2["y"]
    x2_right, y2_bottom = x2_left + rect2["width"], y2_top + rect2["height"]
    
    # Tính tọa độ giao nhau
    intersect_left = max(x1_left, x2_left)
    intersect_top = max(y1_top, y2_top)
    intersect_right = min(x1_right, x2_right)
    intersect_bottom = min(y1_bottom, y2_bottom)
    
    # Kiểm tra có giao nhau không (không tính trường hợp chạm cạnh)
    if intersect_left >= intersect_right or intersect_top >= intersect_bottom:
        return None
    
    # Tính chiều rộng và chiều cao
    width = intersect_right - intersect_left
    height = intersect_bottom - intersect_top
    
    return (intersect_left, intersect_top, width, height)

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính.
   
    Args:
        data_json: dữ liệu JSON đã load.
        input_data: dữ liệu input từ file .in, dạng list các dòng.
   
    Returns:
        list: danh sách kết quả (string) tương ứng với từng test case.
    """
    results = []
    rectangles = data_json["rectangles"]
    
    for line in input_data:
        line = line.strip()
        if not line:
            continue
            
        try:
            # Đọc id1, id2 từ dòng input
            id1, id2 = map(int, line.split())
            
            # Tìm hai hình chữ nhật theo id
            rect1 = find_rectangle_by_id(rectangles, id1)
            rect2 = find_rectangle_by_id(rectangles, id2)
            
            if rect1 is None or rect2 is None:
                results.append("NO INTERSECTION")
                continue
            
            # Tính giao của hai hình chữ nhật
            intersection = calculate_intersection(rect1, rect2)
            
            if intersection is None:
                results.append("NO INTERSECTION")
            else:
                x, y, width, height = intersection
                results.append(f"{x} {y} {width} {height}")
                
        except Exception as e:
            results.append("NO INTERSECTION")
    
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
        results = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        for result in results:
            fout.write(result + "\n")

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