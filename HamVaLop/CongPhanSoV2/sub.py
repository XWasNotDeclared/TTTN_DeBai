import math

def solve(data):
    """
    Giải bài cộng nhiều phân số
    """
    idx = 0
    t = data[idx]
    idx += 1
    result = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        # Khởi tạo tổng = 0/1
        sum_tu = 0
        sum_mau = 1
        
        for i in range(n):
            a = data[idx]
            b = data[idx + 1]
            idx += 2
            
            # Cộng a/b vào tổng hiện tại
            # sum_tu/sum_mau + a/b = (sum_tu*b + a*sum_mau)/(sum_mau*b)
            new_tu = sum_tu * b + a * sum_mau
            new_mau = sum_mau * b
            
            sum_tu = new_tu
            sum_mau = new_mau
        
        # Rút gọn kết quả cuối
        if sum_tu == 0:
            result.append("0")
        else:
            # Xử lý dấu âm
            if sum_mau < 0:
                sum_tu = -sum_tu
                sum_mau = -sum_mau
            
            # Tìm GCD và rút gọn
            gcd = math.gcd(abs(sum_tu), abs(sum_mau))
            sum_tu //= gcd
            sum_mau //= gcd
            
            if sum_mau == 1:
                result.append(str(sum_tu))
            else:
                result.append(f"{sum_tu}/{sum_mau}")
    
    return result

def main():
    data = []
    t = int(input().strip())
    data.append(t)
    
    for _ in range(t):
        n = int(input().strip())
        data.append(n)
        
        for i in range(n):
            a, b = map(int, input().split())
            data.extend([a, b])
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()