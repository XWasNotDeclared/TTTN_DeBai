import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách dữ liệu đã được đọc từ input (các phần tử là chuỗi).
    - Mỗi test case gồm:
        name (str)
        price (float)
        quantity (int)
        promo (str)
    - Trả về: list chứa các dòng kết quả (string).
    """
    t = int(data[0])
    idx = 1
    result = []
    for _ in range(t):
        name = data[idx]
        price = float(data[idx + 1])
        quantity = int(data[idx + 2])
        promo = data[idx + 3].lower()
        idx += 4

        total_value = price * quantity
        if promo == "yes":
            total_value *= 0.9

        result.append(f"Product: {name}")
        result.append(f"Total value: {total_value:.2f} USD")
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

    with open(infile, "r", encoding="utf-8") as fin, open(outfile, "w", encoding="utf-8") as fout:
        # Đọc dữ liệu từ file input dạng chuỗi (không ép về int)
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
