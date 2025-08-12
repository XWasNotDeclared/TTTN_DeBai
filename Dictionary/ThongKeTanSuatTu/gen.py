import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách các dòng văn bản đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả theo định dạng "<từ> <số_lần>".
    """
    n = int(data[0])
    word_count = {}
    
    # Đếm tần suất từng từ
    for i in range(1, n + 1):
        line = data[i]
        words = line.split()
        for word in words:
            # Chỉ lấy các từ chỉ chứa chữ cái Latin
            if word.isalpha():
                word_count[word] = word_count.get(word, 0) + 1
    
    # Sắp xếp theo yêu cầu:
    # 1. Giảm dần theo tần suất
    # 2. Nếu tần suất bằng nhau, sắp theo thứ tự từ điển tăng dần
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    result = []
    for word, count in sorted_words:
        result.append(f"{word} {count}")
    
    return result

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
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r", encoding="utf-8") as fin, open(outfile, "w", encoding="utf-8") as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        data = lines
        
        # Gọi hàm giải
        res = solve(data)
        
        # Ghi kết quả ra file output
        fout.write("\n".join(res) + "\n")

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