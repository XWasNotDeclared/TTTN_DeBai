import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        pairs = []
        for __ in range(n):
            key = data[idx]
            value = data[idx + 1]
            idx += 2
            pairs.append((key, value))
        pairs.sort(key=lambda x: x[0])
        for key, val in pairs:
            result.append(f"{key} {val}")
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
        lines = fin.read().strip().split('\n')
        # Đọc số bộ test
        t = int(lines[0].strip())
        data = [t]
        idx_line = 1
        for _ in range(t):
            n = int(lines[idx_line].strip())
            idx_line += 1
            data.append(n)
            for __ in range(n):
                parts = lines[idx_line].strip().split()
                idx_line += 1
                key = parts[0]
                value = int(parts[1])
                data.extend([key, value])

        res = solve(data)

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
