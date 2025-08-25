def solve(data):
    t = data[0]  # so test case
    result = []
    
    for i in range(1, t + 1):
        name = data[i]  # lay ten thu i
        words = name.split()  # tach thanh cac tu
        
        # Lay cac phan cua ten
        ho = words[0]  # Ho (tu dau tien)
        ten_chinh = words[-1]  # ten chinh (tu cuoi cung)
        ten_dem = words[1:-1]  # cac ten dem (tu thu 2 den thu n-1)
        
        # tao ten moi
        new_name_parts = [ten_chinh, ho] + ten_dem
        new_name = " ".join(new_name_parts)
        
        result.append(new_name)
    
    return result

def main():
    data = []
    t = int(input().strip())  # so test case
    data.append(t)
    
    for _ in range(t):
        name = input().strip()  # doc ten
        data.append(name)
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()