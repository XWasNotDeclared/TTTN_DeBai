import os

def decimal_to_ternary(n: int) -> str:
    """Chuyển số nguyên dương n sang hệ tam phân (chuỗi)."""
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //=3
    return "".join(digits[::-1])

def solve(nums):
    """
    nums chứa danh sách các số nguyên đọc từ file .in.
    Bài này mỗi file chỉ có 1 số nguyên N (theo đề bài).
    Trả về danh sách các dòng kết quả (ở đây 1 dòng).
    """
    n = nums[0]
    res = decimal_to_ternary(n)
    return [res]

def prepare_working_dir():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")

    with open(infile, "r") as fin, open(outfile, "w") as fout:
        data = list(map(int, fin.read().strip().split()))
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
