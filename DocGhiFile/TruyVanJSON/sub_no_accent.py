import json
import sys
import os

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def query_json(data, path):
    """
    Truy van du lieu JSON theo duong dan.
    
    Args:
        data: du lieu JSON
        path: duong dan truy van (string)
    
    Returns:
        tuple: (result, status) 
        - result: gia tri tim duoc hoac None
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
        
        # Kiem tra ket qua cuoi cung
        if isinstance(current, (dict, list)):
            return current, "invalid"
        else:
            return current, "found"
            
    except (KeyError, TypeError):
        return None, "not_found"

def solve_single_query(data_json, query):
    """
    Giai mot truy van don.
    
    Args:
        data_json: du lieu JSON
        query: truy van dang "GET path"
    
    Returns:
        string: ket qua truy van
    """
    if not query.startswith("GET "):
        return "Invalid query"
    
    path = query[4:].strip()  # Bo "GET " o dau
    result, status = query_json(data_json, path)
    
    if status == "found":
        return str(result)
    elif status == "invalid":
        return "Invalid query"
    else:
        return "Not found"

def main():
    """
    Ham chinh: doc tu stdin hoac file JSON neu co.
    """
    # Thu doc tu file JSON neu co
    json_file = "./data/datas.json"
    if os.path.exists(json_file):
        data_json = load_json(json_file)
    else:
        # Du lieu mau neu khong co file
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
    
    # Doc input tu stdin
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