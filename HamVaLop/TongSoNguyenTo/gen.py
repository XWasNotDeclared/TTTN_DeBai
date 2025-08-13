import os

def sieve(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

def solve(data):
    t = data[0]
    idx = 1
    result = []
    max_val = 0
    tmp_idx = 1
    for _ in range(t):
        n = data[tmp_idx]
        tmp_idx += 1
        arr = data[tmp_idx: tmp_idx + n]
        tmp_idx += n
        max_val = max(max_val, max(arr))
    prime_table = sieve(max_val)
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx: idx + n]
        idx += n
        total = sum(x for x in arr if prime_table[x])
        result.append(total)
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
