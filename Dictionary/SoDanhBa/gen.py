import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách các dòng truy vấn đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    company = {}  # Dictionary lồng nhau: {phong_ban: {ten_nv: sdt}}
    result = []
    
    q = int(data[0])
    
    for i in range(1, q + 1):
        query = data[i].strip().split()
        command = query[0]
        
        if command == "ADD":
            phong_ban = query[1]
            ten_nv = query[2]
            sdt = query[3]
            
            if phong_ban not in company:
                company[phong_ban] = {}
            company[phong_ban][ten_nv] = sdt
            
        elif command == "DEL":
            phong_ban = query[1]
            ten_nv = query[2]
            
            if phong_ban in company and ten_nv in company[phong_ban]:
                del company[phong_ban][ten_nv]
                
        elif command == "FIND":
            phong_ban = query[1]
            ten_nv = query[2]
            
            if phong_ban in company and ten_nv in company[phong_ban]:
                result.append(company[phong_ban][ten_nv])
            else:
                result.append("NOT FOUND")
                
        elif command == "LIST":
            phong_ban = query[1]
            
            if phong_ban in company and company[phong_ban]:
                # Sắp xếp theo thứ tự từ điển của tên nhân viên
                sorted_employees = sorted(company[phong_ban].items())
                employee_list = [f"{ten}:{sdt}" for ten, sdt in sorted_employees]
                result.append(" ".join(employee_list))
            else:
                result.append("EMPTY")
    
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
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        data = lines
        
        # Gọi hàm giải
        res = solve(data)
        
        # Ghi kết quả ra file output
        if res:
            fout.write("\n".join(res) + "\n")

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