def solve(data):
    """
    - data[0]: so test case T
    - data[1..]: cac so nguyen lan luot theo test case
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        if n == 0:
            result.append("Zero")
        elif n > 0 and n % 3 == 0:
            result.append("Group A")
        elif n < 0 and n % 5 == 0:
            result.append("Group B")
        else:
            result.append("Others")
    return result



def main():
    data = []
    t = int(input().strip())  # so test case
    data.append(t)
    for _ in range(t):
        #a, b = map(int, input().split())
        n= int(input().strip())
        data.append(n)
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()