import os

def process_word(word):
    """Xử lý 1 từ theo quy tắc nhấp nhô."""
    res = []
    upper = True
    for ch in word:
        if upper:
            res.append(ch.upper())
        else:
            res.append(ch.lower())
        upper = not upper
    return "".join(res)

def solve(data):
    """
    - data[0]: số test case T
    - Sau đó mỗi test case là 1 chuỗi tên.
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        name = data[idx]
        idx += 1
        words = name.split()
        processed = [process_word(w) for w in words]
        result.append(" ".join(processed))
    return result

def prepare_working_dir():
    """Chuyển thư mục làm việc về nơi chứa script hiện tại."""
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    """Xử lý 1 file .in và tạo file .out tương ứng."""
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r", encoding="utf-8") as fin, \
         open(outfile, "w", encoding="utf-8") as fout:
        lines = fin.read().strip().split("\n")
        t = int(lines[0])
        data = [t] + lines[1:]
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
