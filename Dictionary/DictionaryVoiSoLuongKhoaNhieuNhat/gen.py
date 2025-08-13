import os

def solve(data):
    N = data[0]
    max_keys = 0
    for i in range(1, N + 1):
        line = data[i]
        if line == "":
            count_keys = 0
        else:
            pairs = line.split(',')
            count_keys = len(pairs)
        if count_keys > max_keys:
            max_keys = count_keys
    return [max_keys]

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
        data = [N] + lines[1:]
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
