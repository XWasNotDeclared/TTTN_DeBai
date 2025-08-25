from decimal import Decimal, getcontext

# tang do chinh xac du lon (100 chu so thap phan + an toan)
getcontext().prec = 200

def solve(data):
    """
    Ham giai bai toan tong cac so lon chinh xac.
    - data: danh sach chuoi so nguyen/thuc (Decimal se xu ly chinh xac)
    - Tra ve: list chua mot dong ket qua la tong
    """
    total = Decimal("0")
    for s in data:
        total += Decimal(s)
    return [total]

def main():
    data = []
    N = int(input().strip())
    for _ in range(N):
        s = input().strip()
        data.append(s)
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()
