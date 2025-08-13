import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách dữ liệu đã được đọc từ input (kiểu string).
    - Trả về: list chứa các dòng kết quả (string).
    """
    t = int(data[0])
    idx = 1
    result = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        num_chars = len(s)
        num_words = len(s.strip().split()) if s.strip() else 0
        num_upper = sum(1 for c in s if c.isupper())
        result.append(f"{num_chars} {num_words} {num_upper}")
    return result

def prepare_working_dir():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r", encoding="utf-8") as fin, open(outfile, "w", encoding="utf-8") as fout:
        # Đọc dữ liệu từ file input, giữ nguyên từng dòng
        lines = fin.read().splitlines()
        data = lines
        res = solve(data)
        fout.write("\n".join(res) + "\n")

def main():
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()
