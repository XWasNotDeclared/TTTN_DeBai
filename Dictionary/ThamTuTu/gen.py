import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách các dòng đã được đọc từ input.
    - TODO: Viết logic giải ở đây.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    """
    idx = 0
    n = int(data[idx])
    idx += 1
    
    # Đọc bảng tra cứu
    dictionary = {}
    for _ in range(n):
        line = data[idx].strip()
        parts = line.split(' ', 1)  # Tách thành tối đa 2 phần
        x = parts[0]  # từ viết tắt
        y = parts[1]  # từ đầy đủ
        dictionary[x] = y
        idx += 1
    
    # Đọc số lượng từ trong tin nhắn
    m = int(data[idx])
    idx += 1
    
    # Đọc tin nhắn
    message = data[idx].strip().split()
    
    # Dịch tin nhắn
    translated = []
    for word in message:
        if word in dictionary:
            translated.append(dictionary[word])
        else:
            translated.append(word)
    
    return [' '.join(translated)]

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Tìm và trả về danh sách tất cả các file .in trong thư mục đó.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    Giữ nguyên phần này cho các bài sau, trừ khi định dạng input/output thay đổi.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r", encoding='utf-8') as fin, open(outfile, "w", encoding='utf-8') as fout:
        # Đọc dữ liệu từ file input
        data = [line.rstrip('\n') for line in fin]
        # Gọi hàm giải
        res = solve(data)
        # Ghi kết quả ra file output
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    """
    Hàm chính: tìm các file input, xử lý từng file, tạo file output.
    """
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()