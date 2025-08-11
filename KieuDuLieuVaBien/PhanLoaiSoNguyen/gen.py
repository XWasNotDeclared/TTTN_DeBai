import os

def solve(data):
    """
    - data[0]: số test case T
    - data[1..]: các số nguyên lần lượt theo test case
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        if n == 0:
            result.append("Zero")
        elif n > 0 and n % 3 == 0:
            result.append("Group A")
        elif n < 0 and n % 5 == 0:
            result.append("Group B")
        else:
            result.append("Others")
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
    Giữ nguyên phần này cho các bài sau, trừ khi định dạng input/output thay đổi.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")

    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input
        # TODO: Sửa cách đọc nếu bài yêu cầu định dạng khác
        data = list(map(int, fin.read().strip().split()))

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
