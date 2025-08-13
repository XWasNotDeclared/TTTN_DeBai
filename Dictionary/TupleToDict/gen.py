import os

def solve(data):
    n = data[0]
    keys = data[1:1+2*n:2]
    vals = data[2:1+2*n:2]
    d = {}
    for i in range(n):
        d[keys[i]] = vals[i]
    return [str(d)]

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
        n = int(lines[0])
        data = [n]
        for i in range(1, n+1):
            k, v = lines[i].split()
            data.append(k)
            data.append(int(v))
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
