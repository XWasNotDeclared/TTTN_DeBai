import os

def solve(data):
    """
    Hàm giải bài toán tìm dãy con lý tưởng.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa kết quả (string).
    """
    n = data[0]
    arr = data[1:n+1]
    
    if n == 1:
        return [str(arr[0])]
    
    # Tìm tất cả các dãy con liên tiếp tăng dần
    best_sum = float('-inf')
    best_subsequence = []
    
    i = 0
    while i < n:
        # Bắt đầu một dãy con mới từ vị trí i
        current_subsequence = [arr[i]]
        current_sum = arr[i]
        j = i + 1
        
        # Mở rộng dãy con tăng dần
        while j < n and arr[j] > arr[j-1]:
            current_subsequence.append(arr[j])
            current_sum += arr[j]
            j += 1
        
        # Kiểm tra xem dãy con hiện tại có tốt hơn không
        if len(current_subsequence) > 1:  # Chỉ xét dãy con có ít nhất 2 phần tử
            if current_sum > best_sum:
                best_sum = current_sum
                best_subsequence = current_subsequence[:]
        
        # Di chuyển đến phần tử tiếp theo
        if j == i + 1:  # Không có dãy tăng nào từ vị trí i
            i += 1
        else:
            i = j
    
    # Nếu không tìm thấy dãy con tăng nào, trả về số lớn nhất
    if not best_subsequence:
        max_value = max(arr)
        return [str(max_value)]
    
    # Trả về dãy con lý tưởng
    return [' '.join(map(str, best_subsequence))]

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
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input
        data = list(map(int, fin.read().strip().split()))
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