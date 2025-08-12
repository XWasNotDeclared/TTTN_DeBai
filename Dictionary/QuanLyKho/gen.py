import os

def solve(data):
    """
    Hàm giải bài toán chính cho bài 'Quản lý kho hàng'.
    - data: danh sách (chuỗi + số) đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string hoặc số).
    """
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1

    inventory = {}  # tên sản phẩm -> giá trị tồn kho

    # Nhập hàng
    for _ in range(n):
        name = data[idx]; idx += 1
        value = int(data[idx]); idx += 1
        inventory[name] = inventory.get(name, 0) + value

    results = []

    # Xử lý truy vấn
    for _ in range(q):
        k = int(data[idx]); idx += 1
        total = 0
        for __ in range(k):
            name = data[idx]; idx += 1
            total += inventory.get(name, 0)
        results.append(total)

    return results


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
    Đọc input đúng format bài 'Quản lý kho hàng'.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")

    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input (giữ nguyên string + int)
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
