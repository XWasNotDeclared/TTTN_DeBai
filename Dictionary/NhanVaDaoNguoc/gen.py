import os

def solve(data):
    N = data[0]
    keys = []
    values = []
    idx = 1
    for _ in range(N):
        key = data[idx]
        value = data[idx + 1]
        keys.append(key)
        values.append(value)
        idx += 2
    
    result = []
    for i in range(N - 1, -1, -1):
        pos = N - i
        val_new = values[i] * pos
        result.append(f"{keys[i]} {val_new}")
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
        lines = fin.read().strip().split('\n')
        N = int(lines[0])
        data = [N]
        for i in range(1, N + 1):
            key, val = lines[i].split()
            data.append(key)
            data.append(int(val))
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
