import os

def solve(data):
    """
    data là danh sách gồm:
    [N, key1_1, val1_1, key1_2, val1_2, ..., M, key2_1, val2_1, ...]
    """
    idx = 0
    N = data[idx]
    idx += 1

    dict1 = {}
    order1 = []
    for _ in range(N):
        key = data[idx]
        val = data[idx + 1]
        idx += 2
        dict1[key] = val
        order1.append(key)

    M = data[idx]
    idx += 1

    dict2 = {}
    order2 = []
    for _ in range(M):
        key = data[idx]
        val = data[idx + 1]
        idx += 2
        dict2[key] = val
        order2.append(key)

    result_dict = dict1.copy()
    for k, v in dict2.items():
        result_dict[k] = v

    output = []
    used = set()
    for k in order1:
        output.append(f"{k} {result_dict[k]}")
        used.add(k)
    for k in order2:
        if k not in used:
            output.append(f"{k} {result_dict[k]}")

    return output


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
        # Đọc file theo format đề bài: đầu tiên là số nguyên,
        # tiếp theo là các cặp khóa giá trị, trong đó khóa là chuỗi.
        lines = fin.read().strip().split("\n")

        data = []
        # Đọc N
        N = int(lines[0])
        data.append(N)

        # Đọc cặp khóa - giá trị của dict1
        for i in range(1, N + 1):
            key, val = lines[i].split()
            data.append(key)
            data.append(int(val))

        # Đọc M
        M = int(lines[N + 1])
        data.append(M)

        # Đọc cặp khóa - giá trị của dict2
        for i in range(N + 2, N + 2 + M):
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
