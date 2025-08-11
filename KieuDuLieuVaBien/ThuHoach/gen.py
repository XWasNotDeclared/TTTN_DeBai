import os

"""
def solve(data):
    Hàm giải bài toán chính.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - TODO: Viết logic giải ở đây.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    # Ví dụ: bài tính tổng của từng test case
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        result.append(a + b)  # thay bằng logic của bạn
    return result
"""
def solve(data):
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        t = data[idx]
        k = data[idx + 1]
        n = data[idx + 2]
        idx += 3
        if t<=n and not k == 0:
            result.append((n-t)//k+1)   
        else:
            result.append(0)
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
