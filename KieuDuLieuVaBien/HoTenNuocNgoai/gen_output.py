import os

# Lấy thư mục chứa file hiện tại
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print(dname)

# lấy tất cả các tệp .in trong thư mục
def getListFile(dir_):
    list_=[]
    for file_ in os.listdir(dir_):
        if file_.endswith('.in'):
            list_.append(file_)
    return list_

def read_nonempty_line(f):
    """Đọc dòng không rỗng (strip). Trả về None nếu EOF."""
    while True:
        line = f.readline()
        if not line:
            return None
        line = line.strip()
        if line != '':
            return line

# hàm chính của chương trình
def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f, \
         open(out_path, 'w', encoding='utf-8') as fout:
        first = read_nonempty_line(f)
        if first is None:
            return
        try:
            count = int(first)
        except ValueError:
            # nếu không phải số, dừng
            return
        for _ in range(count):
            line = read_nonempty_line(f)
            if line is None:
                break
            parts = line.split()
            # đảm bảo đúng 3 từ; nếu không đủ, bỏ qua hoặc xử lý tùy ý
            if len(parts) != 3:
                # nếu có nhiều hơn 3 từ thì lấy 3 đầu; nếu ít hơn thì ghi dòng rỗng
                if len(parts) > 3:
                    parts = parts[:3]
                else:
                    fout.write("\n")
                    continue
            ho, tendem, tenchinh = parts[0], parts[1], parts[2]
            fout.write(f"{tenchinh} {ho} {tendem}\n")

def main():
    for file_ in getListFile(dname):
        out_name = file_[:-3] + '.out'
        print("Processing", file_)
        in_path = os.path.join(dname, file_)
        out_path = os.path.join(dname, out_name)
        process_file(in_path, out_path)

if __name__ == '__main__':
    main()
