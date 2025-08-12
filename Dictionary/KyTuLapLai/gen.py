import os

def solve(data):
    """
    Hàm giải bài 'Ký tự lặp lại'.
    - data: list, phần tử đầu tiên là chuỗi cần xử lý.
    - Trả về: list chứa 1 dòng kết quả.
    """
    s = data[0]
    freq = {}
    duplicates = []

    # Đếm tần suất ký tự
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Lấy ký tự lặp theo thứ tự xuất hiện lần đầu
    for c in s:
        if freq[c] > 1 and c not in duplicates:
            duplicates.append(c)

    if duplicates:
        return [" ".join(duplicates)]
    else:
        return ["None"]


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
    Giữ nguyên định dạng chuỗi, kể cả khoảng trắng.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")

    with open(infile, "r", encoding="utf-8") as fin, \
         open(outfile, "w", encoding="utf-8") as fout:
        # Đọc nguyên chuỗi, kể cả khoảng trắng
        s = fin.read().rstrip("\n")
        data = [s]

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