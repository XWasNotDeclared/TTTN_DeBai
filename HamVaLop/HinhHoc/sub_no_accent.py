def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach string da duoc doc tu input.
    - TODO: Viet logic giai o day.
    - Tra ve: list (hoac iterable) chua cac dong ket qua (string hoac so).
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
    n = int(input().strip())  # so hinh
    data.append(str(n))
    for _ in range(n):
        line = input().strip()
        data.append(line)
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()