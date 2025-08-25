def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach cac dong van ban da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua theo dinh dang "<tu> <so_lan>".
    """
    n = int(data[0])
    word_count = {}
    
    # Dem tan suat tung tu
    for i in range(1, n + 1):
        line = data[i]
        words = line.split()
        for word in words:
            # Chi lay cac tu chi chua chu cai Latin
            if word.isalpha():
                word_count[word] = word_count.get(word, 0) + 1
    
    # Sap xep theo yeu cau:
    # 1. Giam dan theo tan suat
    # 2. Neu tan suat bang nhau, sap theo thu tu tu dien tang dan
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