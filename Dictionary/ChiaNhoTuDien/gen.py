import os

def solve(data):
    """
    data = [N, K, key1, val1, key2, val2, ..., keyN, valN]
    """
    N = data[0]
    K = data[1]
    res = []
    idx = 2
    while idx < 2 + 2 * N:
        sub_dict = []
        for _ in range(K):
            if idx >= 2 + 2 * N:
                break
            key = data[idx]
            val = data[idx + 1]
            sub_dict.append(f"{key}:{val}")
            idx += 2
        res.append(" ".join(sub_dict))
    return res

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
        lines = fin.read().strip().split("\n")
        # Dòng đầu lấy N, K
        N, K = map(int, lines[0].split())
        data = [N, K]
        for line in lines[1:]:
            key, val = line.split()
            val = int(val)
            data.append(key)
            data.append(val)
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
