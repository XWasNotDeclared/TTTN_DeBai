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

def main():
    data = []
    n = int(input().strip())
    data.append(str(n))
    for _ in range(n):
        line = input().strip()
        data.append(line)
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()