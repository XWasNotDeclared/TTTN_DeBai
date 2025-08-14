import json
import sys
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_library_management(data_json, queries):
    """
    Giải bài toán quản lý thư viện.
    
    Args:
        data_json: dữ liệu JSON chứa thông tin thư viện
        queries: danh sách ID cần truy vấn
    
    Returns:
        list: danh sách kết quả
    """
    results = []
    
    # Tính tổng số sách trong thư viện (bao gồm cả đang mượn)
    total_books = 0
    available_books = 0
    
    books_dict = {}
    
    for book in data_json["books"]:
        books_dict[book["id"]] = book
        total_books += book["quantity"]
        available_books += book["quantity"]
    
    # Tính số sách đang được mượn
    borrowers_dict = {}
    for borrower in data_json["borrowers"]:
        borrowers_dict[borrower["id"]] = borrower
        for borrowed in borrower["borrowed_books"]:
            total_books += 1  # Mỗi sách được mượn cũng tính vào tổng
    
    results.append(str(total_books))
    results.append(str(available_books))
    
    # Xử lý từng truy vấn
    for query_id in queries:
        if query_id in borrowers_dict:
            borrower = borrowers_dict[query_id]
            results.append(f"{borrower['id']} {borrower['name']}")
            
            # Sắp xếp sách theo book_id
            borrowed_books = sorted(borrower["borrowed_books"], key=lambda x: x["book_id"])
            for borrowed in borrowed_books:
                book_id = borrowed["book_id"]
                if book_id in books_dict:
                    results.append(books_dict[book_id]["title"])
        else:
            results.append("NOT FOUND")
    
    return results

def main():
    """
    Hàm chính: đọc input và xử lý
    """
    # Thử đọc từ file JSON nếu có
    data_json = load_json("./data/datas.json")
    
    # Nếu không có file JSON, sử dụng dữ liệu mẫu
    if data_json is None:
        data_json = {
            "books": [
                {"id": 1, "title": "Những tấm lòng cao cả", "quantity": 3},
                {"id": 2, "title": "Đắc Nhân Tâm", "quantity": 0},
                {"id": 3, "title": "Sapiens", "quantity": 5}
            ],
            "borrowers": [
                {"id": 1, "name": "Nguyễn Văn A", "borrowed_books": [
                    {"book_id": 2},
                    {"book_id": 1}
                ]},
                {"id": 2, "name": "Trần Thị B", "borrowed_books": []}
            ]
        }
    
    # Đọc input
    n = int(input())
    queries = []
    for _ in range(n):
        queries.append(int(input()))
    
    # Giải bài toán
    results = solve_library_management(data_json, queries)
    
    # In kết quả
    for result in results:
        print(result)

if __name__ == "__main__":
    main()