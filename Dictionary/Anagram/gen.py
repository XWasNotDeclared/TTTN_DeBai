import os
from collections import Counter

def solve(data):
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        bin_a = bin(a)[2:].zfill(32)
        bin_b = bin(b)[2:].zfill(32)

        count_a = Counter(bin_a)
        count_b = Counter(bin_b)

        if count_a == count_b:
            result.append("Yes")
        else:
            result.append("No")
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
