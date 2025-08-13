import os

def solve(data):
    N = data[0]
    idx = 1
    matrix = []
    for _ in range(N):
        length = data[idx]
        idx += 1
        row = data[idx:idx+length]
        idx += length
        matrix.append(row)

    M = data[idx]
    idx += 1
    scoring = {}
    for _ in range(M):
        word = data[idx]
        point = data[idx+1]
        idx += 2
        scoring[word] = point

    res = []
    for row in matrix:
        total = 0
        for w in row:
            total += scoring.get(w, 0)
        res.append(total)

    return res

def prepare_working_dir():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Processing {infile} -> {outfile} ...")
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        lines = fin.read().strip().split()
        # lines gồm cả số và từ, cần parse sao cho đúng:
        data = []
        i = 0
        N = int(lines[i]); i += 1
        data.append(N)
        for _ in range(N):
            length = int(lines[i]); i += 1
            data.append(length)
            row = lines[i:i+length]
            i += length
            data.extend(row)
        M = int(lines[i]); i += 1
        data.append(M)
        for _ in range(M):
            w = lines[i]; p = int(lines[i+1])
            i += 2
            data.append(w)
            data.append(p)
        res = solve(data)
        fout.write(" ".join(map(str, res)) + "\n")

def main():
    in_files = prepare_working_dir()
    if not in_files:
        print("No .in files found in", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()
