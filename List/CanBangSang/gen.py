import os

def solve(data):
    """
    Hàm giải bài toán cân bằng histogram.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    idx = 0
    N, M = data[idx], data[idx + 1]
    idx += 2
    
    # Đọc ma trận ảnh
    image = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(data[idx])
            idx += 1
        image.append(row)
    
    # Bước 1: Tính histogram gốc
    histogram = [0] * 256
    for i in range(N):
        for j in range(M):
            histogram[image[i][j]] += 1
    
    # Bước 2: Tính CDF (Cumulative Distribution Function)
    cdf = [0] * 256
    cdf[0] = histogram[0]
    for k in range(1, 256):
        cdf[k] = cdf[k-1] + histogram[k]
    
    # Bước 3: Cân bằng histogram
    total_pixels = N * M
    result_image = []
    
    for i in range(N):
        row_result = []
        for j in range(M):
            old_value = image[i][j]
            # Tính giá trị mới: new_value = round(255 * cdf[old_value] / total_pixels)
            new_value = round(255 * cdf[old_value] / total_pixels)
            row_result.append(str(new_value))
        result_image.append(' '.join(row_result))
    
    return result_image

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