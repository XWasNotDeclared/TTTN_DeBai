def process_word(word):
    """Xử lý 1 từ theo quy tắc nhấp nhô."""
    res = []
    upper = True
    for ch in word:
        if upper:
            res.append(ch.upper())
        else:
            res.append(ch.lower())
        upper = not upper
    return "".join(res)

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: list, phần tử đầu tiên là số test case T,
      sau đó mỗi test case là một chuỗi tên.
    - Trả về: list các kết quả chuỗi.
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        name = data[idx]
        idx += 1
        words = name.split()
        processed = [process_word(w) for w in words]
        result.append(" ".join(processed))
    return result

def main():
    t = int(input().strip())
    data = [t]
    for _ in range(t):
        s = input().rstrip("\n")
        data.append(s)
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
