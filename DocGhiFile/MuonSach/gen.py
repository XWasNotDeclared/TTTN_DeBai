import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, input_data):
    """
    Hàm giải bài toán quản lý thư viện.
    
    Args:
        data_json: dữ liệu JSON đã load.
        input_data: dữ liệu input từ file .in, dạng list các dòng.
    
    Returns:
        list: danh sách kết quả (string) tương ứng với output.
    """
    results = []
    
    # Parse input
    n = int(input_data[0])
    queries = []
    for i in range(1, n + 1):
        queries.append(int(input_data[i]))
    
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
        # Đọc dữ liệu file .in
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
    data_json = load_json("./data/datas.json")  # đường dẫn file JSON
    
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