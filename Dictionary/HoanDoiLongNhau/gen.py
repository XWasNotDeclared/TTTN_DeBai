import os

def solve(data):
    n = data[0]
    idx = 1
    orig_dict = {}

    for _ in range(n):
        key1 = data[idx]
        idx += 1
        m = data[idx]
        idx += 1
        orig_dict[key1] = {}
        for __ in range(m):
            key2 = data[idx]
            idx += 1
            k = data[idx]
            idx += 1
            vals = data[idx:idx+k]
            idx += k
            orig_dict[key1][key2] = vals

    from collections import defaultdict
    new_dict = defaultdict(dict)
    for key1, inner in orig_dict.items():
        for key2, vals in inner.items():
            new_dict[key2][key1] = vals

    result = [str(len(new_dict))]
    for key2 in sorted(new_dict):
        result.append(key2)
        subdict = new_dict[key2]
        result.append(str(len(subdict)))
        for key1 in sorted(subdict):
            vals = subdict[key1]
            result.append(f"{key1} {len(vals)} {' '.join(map(str, vals))}")

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
        data = []
        n = int(lines[0])
        data.append(n)
        idx = 1
        for _ in range(n):
            key1 = lines[idx].strip()
            idx += 1
            m = int(lines[idx])
            idx += 1
            data.append(key1)
            data.append(m)
            for __ in range(m):
                parts = lines[idx].split()
                idx += 1
                key2 = parts[0]
                k = int(parts[1])
                vals = list(map(int, parts[2:2+k]))
                data.append(key2)
                data.append(k)
                data.extend(vals)

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
