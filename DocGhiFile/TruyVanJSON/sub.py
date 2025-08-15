import json
import sys
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def query_json(data, path):
    """
    Truy vấn dữ liệu JSON theo đường dẫn.
    
    Args:
        data: dữ liệu JSON
        path: đường dẫn truy vấn (string)
    
    Returns:
        tuple: (result, status) 
        - result: giá trị tìm được hoặc None
        - status: "found", "invalid", "not_found"
    """
    if not path:
        return data, "invalid" if isinstance(data, (dict, list)) else "found"
    
    parts = path.split('/')
    current = data
    
    try:
        for part in parts:
            if isinstance(current, dict):
                if part in current:
                    current = current[part]
                else:
                    return None, "not_found"
            else:
                return None, "not_found"
        
        # Kiểm tra kết quả cuối cùng
        if isinstance(current, (dict, list)):
            return current, "invalid"
        else:
            return current, "found"
            
    except (KeyError, TypeError):
        return None, "not_found"

def solve_single_query(data_json, query):
    """
    Giải một truy vấn đơn.
    
    Args:
        data_json: dữ liệu JSON
        query: truy vấn dạng "GET path"
    
    Returns:
        string: kết quả truy vấn
    """
    if not query.startswith("GET "):
        return "Invalid query"
    
    path = query[4:].strip()  # Bỏ "GET " ở đầu
    result, status = query_json(data_json, path)
    
    if status == "found":
        return str(result)
    elif status == "invalid":
        return "Invalid query"
    else:
        return "Not found"

def main():
    """
    Hàm chính: đọc từ stdin hoặc file JSON nếu có.
    """
    # Thử đọc từ file JSON nếu có
    json_file = "./data/datas.json"
    if os.path.exists(json_file):
        data_json = load_json(json_file)
    else:
        # Dữ liệu mẫu nếu không có file
        data_json = {
            "user": {
                "1": {"name": "Alice", "email": "alice@example.com"},
                "2": {"name": "Bob", "email": "bob@example.com"}
            },
            "files": {
                "images": {"img1": "image1.png", "thumb1": "thumb1.png"},
                "docs": {"doc1": "document1.txt"}
            },
            "settings": {
                "theme": "dark",
                "language": "en",
                "features": {"beta": True}
            }
        }
    
    # Đọc input từ stdin
    try:
        while True:
            line = input().strip()
            if not line:
                break
            result = solve_single_query(data_json, line)
            print(result)
    except EOFError:
        pass

if __name__ == "__main__":
    main()