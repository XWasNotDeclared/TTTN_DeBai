def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách string đã được đọc từ input.
    - TODO: Viết logic giải ở đây.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    """
    PI = 3.14159
    n = int(data[0])
    idx = 1
    result = []
    
    for _ in range(n):
        line = data[idx].split()
        shape_type = line[0]
        
        if shape_type == "RECT":
            w = int(line[1])
            h = int(line[2])
            area = w * h
            perimeter = 2 * (w + h)
        elif shape_type == "CIRCLE":
            r = int(line[1])
            area = PI * r * r
            perimeter = 2 * PI * r
        
        result.append(f"{area:.2f} {perimeter:.2f}")
        idx += 1
    
    return result

def main():
    data = []
    n = int(input().strip())  # số hình
    data.append(str(n))
    for _ in range(n):
        line = input().strip()
        data.append(line)
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()