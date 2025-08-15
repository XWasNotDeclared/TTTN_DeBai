import os

def solve(data):
    """
    Hàm giải bài toán xoay list sang phải k bước.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các phần tử sau khi xoay.
    """
    n = data[0]
    k = data[1]
    arr = data[2:2+n]
    
    # Tối ưu k để tránh xoay thừa
    k = k % n if n > 0 else 0
    
    # Xoay list sang phải k bước
    if k == 0:
        result = arr
    else:
        result = arr[-k:] + arr[:-k]
    
    return [' '.join(map(str, result))]

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
        n, k = map(int, lines[0].split())
        data = [n, k]
        
        if n > 0 and len(lines) > 1:
            arr = list(map(int, lines[1].split()))
            data.extend(arr)
        
        # Gọi hàm giải
        res = solve(data)
        # Ghi kết quả ra file output
        fout.write(res[0] + "\n")

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