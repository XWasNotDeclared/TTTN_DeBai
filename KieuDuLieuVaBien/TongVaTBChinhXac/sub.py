from decimal import Decimal, getcontext

# tăng độ chính xác đủ lớn (100 chữ số thập phân + an toàn)
getcontext().prec = 200

def solve(data):
    """
    Hàm giải bài toán tổng các số lớn chính xác.
    - data: danh sách chuỗi số nguyên/thực (Decimal sẽ xử lý chính xác)
    - Trả về: list chứa một dòng kết quả là tổng
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
