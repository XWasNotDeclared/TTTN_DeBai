import os

def solve(data):
    t = data[0]
    idx = 1
    result = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx: idx + n]
        idx += n
        
        max_val = max(arr)
        freq = [0] * (max_val + 1)
        
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        
        for k in range(1, max_val + 1):
            s = 0
            for multiple in range(k, max_val + 1, k):
                s += count[multiple]
            freq[k] = s
        
        pairs = []
        for k in range(1, max_val + 1):
            if freq[k] > 0:
                pairs.append(f"{k}: {freq[k]}")
        result.append("{" + ", ".join(pairs) + "}")
    
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
