def process_word(word):
    """Xu ly 1 tu theo quy tac nhap nho."""
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
    Ham giai bai toan chinh.
    - data: list, phan tu dau tien la so test case T,
      sau do moi test case la mot chuoi ten.
    - Tra ve: list cac ket qua chuoi.
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
