import os
import math

def solve(data):
    """
    Giải bài cộng 2 phân số
    """
    t = data[0]
    idx = 1
    result = []
    
    for _ in range(t):
        a, b, c, d = data[idx:idx+4]
        idx += 4
        
        # Tính tổng: a/b + c/d = (a*d + c*b)/(b*d)
        tu = a * d + c * b
        mau = b * d
        
        # Rút gọn
        if tu == 0:
            result.append("0")
        else:
            # Xử lý dấu âm
            if mau < 0:
                tu = -tu
                mau = -mau
            
            # Tìm GCD và rút gọn
            gcd = math.gcd(abs(tu), abs(mau))
            tu //= gcd
            mau //= gcd
            
            if mau == 1:
                result.append(str(tu))
            else:
                result.append(f"{tu}/{mau}")
    
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
    
    with open(infile, "r") as fin:
        lines = [line.strip() for line in fin.readlines() if line.strip()]
    
    data = []
    data.append(int(lines[0]))  # T
    
    for i in range(1, len(lines)):
        numbers = list(map(int, lines[i].split()))
        data.extend(numbers)
    
    res = solve(data)
    
    with open(outfile, "w") as fout:
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