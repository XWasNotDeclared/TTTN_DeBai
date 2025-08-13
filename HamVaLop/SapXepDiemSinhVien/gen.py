import os

def solve(data):
    """
    Hàm giải bài toán quản lý danh sách sinh viên.
    - data: danh sách chứa thông tin đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    result = []
    idx = 0
    t = data[idx]
    idx += 1
    
    for case in range(1, t + 1):
        n = data[idx]
        idx += 1
        
        students = []
        for _ in range(n):
            student_data = data[idx]
            idx += 1
            students.append(student_data)
        
        # Tính tổng điểm và chuẩn bị dữ liệu cho việc sắp xếp
        student_list = []
        for student in students:
            parts = student.split()
            student_id = parts[0]
            
            # Tìm vị trí của điểm Toán (số thực đầu tiên từ cuối)
            # Lấy 5 phần tử cuối: Toán, Lý, Hóa, Khóa, Lớp
            toan = float(parts[-5])
            ly = float(parts[-4])
            hoa = float(parts[-3])
            course = int(parts[-2])
            class_name = parts[-1]
            
            # Tên là tất cả các phần từ vị trí 1 đến trước điểm Toán
            name = " ".join(parts[1:-5])
            
            total = toan + ly + hoa
            
            student_list.append({
                'id': student_id,
                'name': name,
                'total': total,
                'class': class_name,
                'course': course
            })
        
        # Sắp xếp: giảm dần theo tổng điểm, tăng dần theo mã sinh viên nếu bằng nhau
        student_list.sort(key=lambda x: (-x['total'], x['id']))
        
        # Tạo output cho test case này
        result.append(f"Case #{case}:")
        for student in student_list:
            result.append(f"{student['id']} {student['name']} {student['total']:.2f} {student['class']} {student['course']}")
    
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
        lines = [line.strip() for line in fin.readlines()]
        data = []
        idx = 0
        
        t = int(lines[idx])
        data.append(t)
        idx += 1
        
        for _ in range(t):
            n = int(lines[idx])
            data.append(n)
            idx += 1
            
            for _ in range(n):
                data.append(lines[idx])
                idx += 1
        
        # Gọi hàm giải
        res = solve(data)
        # Ghi kết quả ra file output
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