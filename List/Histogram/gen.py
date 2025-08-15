import os

def solve(data):
    """
    Hàm giải bài toán tính histogram ảnh xám.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    idx = 0
    H, W = data[idx], data[idx + 1]
    idx += 2
    
    # Đọc ma trận ảnh và tính histogram đồng thời
    histogram = [0] * 256  # Mảng đếm cho 256 mức xám (0-255)
    
    for i in range(H):
        for j in range(W):
            pixel_value = data[idx]
            histogram[pixel_value] += 1
            idx += 1
    
    # Tạo kết quả chỉ với các mức xám xuất hiện ít nhất một lần
    result = []
    for gray_level in range(256):
        if histogram[gray_level] > 0:
            result.append(f"{gray_level} {histogram[gray_level]}")
    
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
        data = list(map(int, fin.read().strip().split()))
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