import math

def solve(data):
    """
    Giai bai cong 2 phan so
    """
    t = data[0]
    idx = 1
    result = []
    
    for _ in range(t):
        a, b, c, d = data[idx:idx+4]
        idx += 4
        
        # Tinh tong: a/b + c/d = (a*d + c*b)/(b*d)
        tu = a * d + c * b
        mau = b * d
        
        # Rut gon
        if tu == 0:
            result.append("0")
        else:
            # Xu ly dau am
            if mau < 0:
                tu = -tu
                mau = -mau
            
            # Tim GCD va rut gon
            gcd = math.gcd(abs(tu), abs(mau))
            tu //= gcd
            mau //= gcd
            
            if mau == 1:
                result.append(str(tu))
            else:
                result.append(f"{tu}/{mau}")
    
    return result

def main():
    data = []
    t = int(input().strip())
    data.append(t)
    
    for _ in range(t):
        line = list(map(int, input().split()))
        data.extend(line)
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()