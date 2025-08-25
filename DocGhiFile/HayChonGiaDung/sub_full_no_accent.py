import json
import os

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_game_show(data_json, product_id, guesses):
    """
    Giai bai toan doan gia cho mot test case.
    
    Args:
        data_json: du lieu JSON chua thong tin san pham
        product_id: id san pham can doan
        guesses: list 4 gia du doan cua 4 nguoi choi
    
    Returns:
        int: so thu tu nguoi thang (1-4) hoac -1 neu khong ai thang
    """
    # Tim gia that cua san pham
    real_price = None
    for product in data_json:
        if product["id"] == product_id:
            real_price = product["price"]
            break
    
    if real_price is None:
        return -1
    
    # Tim nguoi thang: doan dung hoac thap hon gan nhat
    winner = -1
    best_guess = -1
    
    for i in range(4):
        guess = guesses[i]
        # Chi xet nhung du doan <= gia that
        if guess <= real_price:
            # Neu day la du doan tot hon (gan gia that hon)
            if guess > best_guess:
                best_guess = guess
                winner = i + 1  # Nguoi choi danh so tu 1
    
    return winner

def main():
    """
    Ham chinh doc input tu ban phim va xu ly
    """
    # Doc du lieu tu file JSON
    try:
        data_json = load_json("./data/datas.json")
    except FileNotFoundError:
        print("Khong tim thay file ./data/datas.json")
        return
    
    # Doc so luong test case
    t = int(input().strip())
    
    results = []
    for _ in range(t):
        # Doc id san pham
        product_id = int(input().strip())
        
        # Doc 4 du doan
        guesses = list(map(int, input().strip().split()))
        
        # Giai va luu ket qua
        result = solve_game_show(data_json, product_id, guesses)
        results.append(result)
    
    # In ket qua
    for result in results:
        print(result)

if __name__ == "__main__":
    main()