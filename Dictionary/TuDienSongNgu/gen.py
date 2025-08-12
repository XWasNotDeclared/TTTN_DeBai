import os

def solve(data):
    """
    Hàm giải bài toán từ điển song ngữ.
    - data: danh sách các dòng lệnh đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả cho các lệnh find.
    """
    dictionary = {}
    result = []
    
    q = int(data[0])
    
    for i in range(1, q + 1):
        line = data[i].strip()
        parts = line.split(' ', 2)  # Tách tối đa thành 3 phần
        
        command = parts[0]
        
        if command == "add":
            eng = parts[1]
            viet = parts[2] if len(parts) > 2 else ""
            dictionary[eng] = viet
            
        elif command == "find":
            eng = parts[1]
            if eng in dictionary:
                result.append(dictionary[eng])
            else:
                result.append("Not found")
    
    return result

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Tìm và trả về danh sách tất cả các file .in trong thư mục đó.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    
    with open(infile, "r", encoding="utf-8") as fin, open(outfile, "w", encoding="utf-8") as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        
        # Gọi hàm giải
        res = solve(lines)
        
        # Ghi kết quả ra file output
        if res:
            fout.write("\n".join(map(str, res)) + "\n")
        else:
            fout.write("")

def main():
    """
    Hàm chính: tìm các file input, xử lý từng file, tạo file output.
    """
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()