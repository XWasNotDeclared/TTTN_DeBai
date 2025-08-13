import os
import math

def solve(data):
    """
    Hàm giải bài toán GCD của dãy số.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các kết quả GCD (mỗi test 1 dòng).
    """
    t = data[0]  # số test case
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx: idx + n]
        idx += n
        gcd_val = arr[0]
        for num in arr[1:]:
            gcd_val = math.gcd(gcd_val, num)
        result.append(gcd_val)
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
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        data = list(map(int, fin.read().strip().split()))
        res = solve(data)
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()
