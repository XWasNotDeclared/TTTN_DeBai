import json
import sys

def load_json(file_path):
    """Doc file JSON va tra ve du lieu."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_rectangle_by_id(rectangles, target_id):
    """Tim hinh chu nhat theo id."""
    for rect in rectangles:
        if rect["id"] == target_id:
            return rect
    return None

def calculate_intersection(rect1, rect2):
    """
    Tinh giao cua hai hinh chu nhat.
    
    Args:
        rect1, rect2: dictionary chua thong tin hinh chu nhat
        
    Returns:
        tuple: (x, y, width, height) neu co giao, None neu khong giao
    """
    # Toa do goc tren trai va duoi phai cua rect1
    x1_left, y1_top = rect1["x"], rect1["y"]
    x1_right, y1_bottom = x1_left + rect1["width"], y1_top + rect1["height"]
    
    # Toa do goc tren trai va duoi phai cua rect2
    x2_left, y2_top = rect2["x"], rect2["y"]
    x2_right, y2_bottom = x2_left + rect2["width"], y2_top + rect2["height"]
    
    # Tinh toa do giao nhau
    intersect_left = max(x1_left, x2_left)
    intersect_top = max(y1_top, y2_top)
    intersect_right = min(x1_right, x2_right)
    intersect_bottom = min(y1_bottom, y2_bottom)
    
    # Kiem tra co giao nhau khong (khong tinh truong hop cham canh)
    if intersect_left >= intersect_right or intersect_top >= intersect_bottom:
        return None
    
    # Tinh chieu rong va chieu cao
    width = intersect_right - intersect_left
    height = intersect_bottom - intersect_top
    
    return (intersect_left, intersect_top, width, height)

def main():
    """Ham chinh de giai bai toan."""
    try:
        # Doc du lieu tu file JSON
        data = load_json("./data/datas.json")
        rectangles = data["rectangles"]
        
        # Doc so luong test case
        n = int(input().strip())
        
        # Xu ly tung test case
        for _ in range(n):
            line = input().strip()
            id1, id2 = map(int, line.split())
            
            # Tim hai hinh chu nhat theo id
            rect1 = find_rectangle_by_id(rectangles, id1)
            rect2 = find_rectangle_by_id(rectangles, id2)
            
            if rect1 is None or rect2 is None:
                print("NO INTERSECTION")
                continue
            
            # Tinh giao cua hai hinh chu nhat
            intersection = calculate_intersection(rect1, rect2)
            
            if intersection is None:
                print("NO INTERSECTION")
            else:
                x, y, width, height = intersection
                print(f"{x} {y} {width} {height}")
                
    except Exception as e:
        print("NO INTERSECTION")

if __name__ == "__main__":
    main()