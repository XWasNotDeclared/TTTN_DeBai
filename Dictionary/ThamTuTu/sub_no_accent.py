def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach cac dong da duoc doc tu input.
    - TODO: Viet logic giai o day.
    - Tra ve: list (hoac iterable) chua cac dong ket qua (string hoac so).
    """
    idx = 0
    n = int(data[idx])
    idx += 1
    
    # Doc bang tra cuu
    dictionary = {}
    for _ in range(n):
        line = data[idx].strip()
        parts = line.split(' ', 1)  # Tach thanh toi da 2 phan
        x = parts[0]  # tu viet tat
        y = parts[1]  # tu day du
        dictionary[x] = y
        idx += 1
    
    # Doc so luong tu trong tin nhan
    m = int(data[idx])
    idx += 1
    
    # Doc tin nhan
    message = data[idx].strip().split()
    
    # Dich tin nhan
    translated = []
    for word in message:
        if word in dictionary:
            translated.append(dictionary[word])
        else:
            translated.append(word)
    
    return [' '.join(translated)]


def main():
    data = []
    
    # Dung input() thay cho sys.stdin
    n = int(input())
    data.append(str(n))
    for _ in range(n):
        data.append(input())
    m = int(input())
    data.append(str(m))
    data.append(input())  # tin nhan
    
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()