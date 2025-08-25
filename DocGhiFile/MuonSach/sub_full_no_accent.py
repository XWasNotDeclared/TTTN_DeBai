import json
import sys
import os

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_library_management(data_json, queries):
    """
    Giai bai toan quan ly thu vien.
    
    Args:
        data_json: du lieu JSON chua thong tin thu vien
        queries: danh sach ID can truy van
    
    Returns:
        list: danh sach ket qua
    """
    results = []
    
    # Tinh tong so sach trong thu vien (bao gom ca dang muon)
    total_books = 0
    available_books = 0
    
    books_dict = {}
    
    for book in data_json["books"]:
        books_dict[book["id"]] = book
        total_books += book["quantity"]
        available_books += book["quantity"]
    
    # Tinh so sach dang duoc muon
    borrowers_dict = {}
    for borrower in data_json["borrowers"]:
        borrowers_dict[borrower["id"]] = borrower
        for borrowed in borrower["borrowed_books"]:
            total_books += 1  # Moi sach duoc muon cung tinh vao tong
    
    results.append(str(total_books))
    results.append(str(available_books))
    
    # Xu ly tung truy van
    for query_id in queries:
        if query_id in borrowers_dict:
            borrower = borrowers_dict[query_id]
            results.append(f"{borrower['id']} {borrower['name']}")
            
            # Sap xep sach theo book_id
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
    Ham chinh: doc input va xu ly
    """
    # Thu doc tu file JSON neu co
    data_json = load_json("./data/datas.json")
    
    # Neu khong co file JSON, su dung du lieu mau
    if data_json is None:
        data_json = {
            "books": [
                {"id": 1, "title": "Nhung tam long cao ca", "quantity": 3},
                {"id": 2, "title": "Dac Nhan Tam", "quantity": 0},
                {"id": 3, "title": "Sapiens", "quantity": 5}
            ],
            "borrowers": [
                {"id": 1, "name": "Nguyen Van A", "borrowed_books": [
                    {"book_id": 2},
                    {"book_id": 1}
                ]},
                {"id": 2, "name": "Tran Thi B", "borrowed_books": []}
            ]
        }
    
    # Doc input
    n = int(input())
    queries = []
    for _ in range(n):
        queries.append(int(input()))
    
    # Giai bai toan
    results = solve_library_management(data_json, queries)
    
    # In ket qua
    for result in results:
        print(result)

if __name__ == "__main__":
    main()