import os

def solve(data):
    res = []
    idx = 0
    N = data[idx]
    idx += 1

    for _ in range(N):
        name = data[idx]
        idx += 1
        M = data[idx]
        idx += 1
        subjects = []
        for __ in range(M):
            subj = data[idx]
            score = data[idx+1]
            idx += 2
            subjects.append((subj, score))
        subjects.sort(key=lambda x: x[1])
        res.append(name)
        for s, sc in subjects:
            res.append(f"{s} {sc}")

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
        lines = fin.read().strip().split('\n')
        data = []
        N = int(lines[0].strip())
        data.append(N)
        line_idx = 1
        for _ in range(N):
            name = lines[line_idx].strip()
            line_idx += 1
            M = int(lines[line_idx].strip())
            line_idx += 1
            data.append(name)
            data.append(M)
            for __ in range(M):
                subj_line = lines[line_idx].split()
                line_idx += 1
                data.append(subj_line[0])
                data.append(int(subj_line[1]))

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
