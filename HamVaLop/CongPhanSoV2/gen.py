import os
import math

def solve(data):
    """
    Giải bài cộng nhiều phân số  
    """
    idx = 0
    t = data[idx]
    idx += 1
    result = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        # Khởi tạo tổng = 0/1
        sum_tu = 0
        sum_mau = 1
        
        for i in range(n):
            a = data[idx]
            b = data[idx + 1]
            idx += 2
            
            # Cộng a/b vào tổng hiện tại
            new_tu = sum_tu * b + a * sum_mau
            new_mau = sum_mau * b
            
            sum_tu = new_tu
            sum_mau = new_mau
        
        # Rút gọn kết quả cuối
        if sum_tu == 0:
            result.append("0")
        else:
            # Xử lý dấu âm
            if sum_mau < 0:
                sum_tu = -sum_tu
                sum_mau = -sum_mau
            
            # Tìm GCD và rút gọn
            gcd = math.gcd(abs(sum_tu), abs(sum_mau))
            sum_tu //= gcd
            sum_mau //= gcd
            
            if sum_mau == 1:
                result.append(str(sum_tu))
            else:
                result.append(f"{sum_tu}/{sum_mau}")
    
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
    idx = 0
    t = int(lines[idx])
    data.append(t)
    idx += 1
    
    for _ in range(t):
        n = int(lines[idx])
        data.append(n)
        idx += 1
        
        for i in range(n):
            a, b = map(int, lines[idx].split())
            data.extend([a, b])
            idx += 1
    
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