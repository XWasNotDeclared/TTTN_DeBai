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


def main():
    data = []
    
    # Dùng input() thay cho sys.stdin
    n = int(input())
    data.append(str(n))
    for _ in range(n):
        data.append(input())
    m = int(input())
    data.append(str(m))
    data.append(input())  # tin nhắn
    
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()