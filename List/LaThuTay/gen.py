import os

def solve_from_input(t, test_cases):
    """
    t: số lượng test case
    test_cases: list các tuple (n, s, x_list)
    Trả về list kết quả (mỗi kết quả là số bước tối thiểu)
    """
    results = []
    for i in range(t):
        n, s, x = test_cases[i]
        min_x = x[0]
        max_x = x[-1]
        dist1 = abs(s - min_x) + (max_x - min_x)
        dist2 = abs(s - max_x) + (max_x - min_x)
        results.append(str(min(dist1, dist2)))
    return results

def prepare_working_dir():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")

    with open(infile, "r") as fin:
        lines = fin.read().strip().split("\n")

    t = int(lines[0])
    test_cases = []
    idx = 1
    for _ in range(t):
        n, s = map(int, lines[idx].split())
        idx += 1
        x = list(map(int, lines[idx].split()))
        idx += 1
        test_cases.append((n, s, x))

    results = solve_from_input(t, test_cases)

    with open(outfile, "w") as fout:
        fout.write("\n".join(results) + "\n")

def main():
    in_files = prepare_working_dir()

    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return

    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()
