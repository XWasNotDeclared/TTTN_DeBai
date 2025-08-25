# File: sub.py
def solve(data):
    """
    Ham giai bai toan chuyen doi mui gio.
    - data: danh sach chua input da duoc doc
    - Tra ve: list chua cac dong ket qua
    """
    idx = 0
    n = data[idx]
    idx += 1
    
    # Doc thoi gian Ha Noi (HH:MM)
    hanoi_time = data[idx]
    idx += 1
    
    # Tach gio va phut
    hh, mm = map(int, hanoi_time.split(':'))
    hanoi_minutes = hh * 60 + mm  # Chuyen sang phut de tinh toan
    
    result = []
    
    for _ in range(n):
        city_name = data[idx]
        offset = data[idx + 1]
        idx += 2
        
        # Tinh thoi gian moi
        new_minutes = hanoi_minutes + offset * 60
        
        # Xu ly vong 24 gio
        new_minutes = new_minutes % (24 * 60)
        if new_minutes < 0:
            new_minutes += 24 * 60
            
        # Chuyen ve gio:phut
        new_hh = new_minutes // 60
        new_mm = new_minutes % 60
        
        # Format output
        time_str = f"{new_hh:02d}:{new_mm:02d}"
        result.append(f"{city_name} {time_str}")
    
    return result

def main():
    data = []
    
    # Doc so luong thanh pho
    n = int(input().strip())
    data.append(n)
    
    # Doc thoi gian Ha Noi
    hanoi_time = input().strip()
    data.append(hanoi_time)
    
    # Doc thong tin tung thanh pho
    for _ in range(n):
        line = input().strip().split()
        city_name = line[0]
        offset = int(line[1])
        data.extend([city_name, offset])
    
    # Giai va in ket qua
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()