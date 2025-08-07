import os

# Lấy thư mục chứa file hiện tại
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print(f"Thư mục hiện tại: {dname}")

# Lấy tất cả các tệp .in trong thư mục
def getListFile(dir_):
    return [file_ for file_ in os.listdir(dir_) if file_.endswith('.in')]

# Hàm đọc dòng không rỗng
def read_nonempty_line(f):
    while True:
        line = f.readline()
        if not line:
            return None
        line = line.strip()
        if line != '':
            return line

# Hàm xử lý từng test case
def analyze_ki_values(ki_list):
    result = []
    exploded = False
    for k in ki_list:
        if exploded:
            result.append('?')
        elif k > 100000:
            result.append('?')
            exploded = True
        elif k <= 10:
            result.append('N')
        elif k <= 1000:
            result.append('S')
        elif k <= 100000:
            result.append('SS')
    return result

# Hàm chính xử lý file
def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f, \
         open(out_path, 'w', encoding='utf-8') as fout:
        
        T_line = read_nonempty_line(f)
        if T_line is None:
            return
        try:
            T = int(T_line)
        except ValueError:
            return

        for _ in range(T):
            n_line = read_nonempty_line(f)
            ki_line = read_nonempty_line(f)
            if n_line is None or ki_line is None:
                break
            try:
                n = int(n_line)
                ki_values = list(map(int, ki_line.split()))
                if len(ki_values) != n:
                    fout.write("INVALID INPUT\n")
                    continue
                result = analyze_ki_values(ki_values)
                fout.write(' '.join(result) + '\n')
            except:
                fout.write("INVALID INPUT\n")

# Hàm main
def main():
    for file_ in getListFile(dname):
        out_name = file_[:-3] + '.out'
        print(f"Đang xử lý {file_} -> {out_name}")
        in_path = os.path.join(dname, file_)
        out_path = os.path.join(dname, out_name)
        process_file(in_path, out_path)

if __name__ == '__main__':
    main()
