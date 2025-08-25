import json

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    
    Args:
        file_path (str): duong dan toi file JSON.
    
    Returns:
        dict hoac list: du lieu JSON.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, data_input):
    """
    Ham giai bai toan chinh.
    
    Args:
        data_json: du lieu da load tu file JSON.
        data_input: du lieu nhap tu ban phim (list, str, so, tuy bai).
    
    Returns:
        list: danh sach cac ket qua (string hoac so) cho moi test case.
    """
    # TODO: Viet logic xu ly bai toan o day
    # Vi du:
    # - Loc hoac tinh toan dua tren data_json
    # - Su dung data_input lam input tu nguoi dung
    # - Luu ket qua tung test case vao list
    results = []
    
    return results

def main():
    # 1. Load du lieu JSON
    data_json = load_json("./data/file.json")  # doi duong dan file neu can
    
    # 2. Nhap du lieu tu ban phim
    # Vi du: nhap t so test case va du lieu kem theo
    t = int(input().strip())
    data_input = []
    for _ in range(t):
        # tuy bai: nhap tung dong, split, map sang int/float...
        line = input().strip()
        data_input.append(line)
    
    # 3. Goi ham solve
    res = solve(data_json, data_input)
    
    # 4. In ket qua
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()
