import os

def solve(data):
    N = data[0]
    K = data[1]
    idx = 2
    result = []
    for _ in range(N):
        key = data[idx]
        val = data[idx + 1]
        idx += 2
        try:
            val_int = int(val)
            if val_int > K:
                result.append(f"{key} {val}")
        except:
            result.append(f"{key} {val}")

    if not result:
        result.append("Empty")
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
        lines = fin.read().strip().split()
        # Đọc dữ liệu giữ nguyên định dạng (key và val có thể là chuỗi, nên không ép int)
        data = []
        # Dòng đầu: N
        data.append(int(lines[0]))
        # Dòng hai: K
        data.append(int(lines[1]))
        # Các dòng tiếp theo: key val
        # Tổng số phần tử còn lại là 2*N (key,val)
        for i in range(2, 2 + 2*data[0], 2):
            data.append(lines[i])     # key
            data.append(lines[i+1])   # val
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
