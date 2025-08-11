import os

import math

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.isqrt(x))
    for i in range(3, r+1, 2):
        if x % i == 0:
            return False
    return True

def solve(data):
    """
    - data[0]: số test case T
    - data[1..]: các phần tử input của từng test case
    """
    t = data[0]
    idx = 1
    result = []

    for _ in range(t):
        # Đọc N, p, m
        n = data[idx]
        p = data[idx+1]
        m = data[idx+2]
        idx += 3

        # Đọc mảng a
        a = data[idx: idx + n]
        idx += n

        # Tính median
        sorted_a = sorted(a)
        if n % 2 == 1:
            median = sorted_a[n // 2]
        else:
            median = (sorted_a[n//2 - 1] + sorted_a[n//2]) // 2  # làm tròn xuống

        # Tính thuế
        tax = []
        for income in a:
            base = math.ceil(income * p / 100)
            if income > median:
                base += m
            tax.append(base)

        total_tax = sum(tax)

        # Nếu tổng là số nguyên tố → giảm 1 đô cho người nghèo nhất
        if is_prime(total_tax):
            total_tax -= 1

        result.append(str(total_tax))

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
