import os

def solve(data):
    """
    Hàm giải bài toán MIDEQUE.
    - data: danh sách chứa số thao tác và các thao tác.
    - Trả về: list chứa các kết quả của pop và size.
    """
    q = data[0]
    idx = 1
    result = []
    mideque = []  # Sử dụng list để mô phỏng mideque
    
    for _ in range(q):
        operation = data[idx]
        
        if operation == "push_front":
            x = data[idx + 1]
            mideque.insert(0, x)  # Thêm vào đầu
            idx += 2
        elif operation == "push_back":
            x = data[idx + 1]
            mideque.append(x)  # Thêm vào cuối
            idx += 2
        elif operation == "pop":
            if not mideque:
                result.append("EMPTY")
            else:
                n = len(mideque)
                # Tính vị trí phần tử giữa (chỉ số bắt đầu từ 1)
                if n % 2 == 0:  # Chẵn
                    mid_pos = n // 2 + 1  # Vị trí thứ n/2 + 1
                else:  # Lẻ
                    mid_pos = (n - 1) // 2 + 1  # Vị trí thứ (n-1)/2 + 1 = (n+1)/2
                
                # Chuyển về chỉ số 0-indexed
                mid_idx = mid_pos - 1
                popped_element = mideque.pop(mid_idx)
                result.append(popped_element)
            idx += 1
        elif operation == "size":
            result.append(len(mideque))
            idx += 1
    
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
    with open(infile, "r", encoding='utf-8') as fin, open(outfile, "w", encoding='utf-8') as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        data = []
        q = int(lines[0])
        data.append(q)
        
        for i in range(1, q + 1):
            parts = lines[i].split()
            if len(parts) == 2:  # push_front hoặc push_back
                operation = parts[0]
                x = int(parts[1])
                data.extend([operation, x])
            else:  # pop hoặc size
                operation = parts[0]
                data.append(operation)
        
        # Gọi hàm giải
        res = solve(data)
        # Ghi kết quả ra file output
        if res:
            fout.write("\n".join(map(str, res)) + "\n")

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