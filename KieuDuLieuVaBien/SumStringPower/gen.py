import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string hoặc số).
    """
    t = int(data[0])
    idx = 1
    result = []
    for _ in range(t):
        a = int(data[idx])
        b = float(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        # 1. Tổng a + b (2 chữ số thập phân)
        result.append(f"{a + b:.2f}")
        
        # 2. Bình phương của a
        result.append(str(a * a))
        
        # 3. Lặp chuỗi hoặc EMPTY
        if a > 0:
            result.append(s * a)
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
        # Đọc dữ liệu từ file input (không ép kiểu vội, để solve tự ép)
        data = fin.read().strip().split()

        # Gọi hàm giải
        res = solve(data)

        # Ghi kết quả ra file output
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
