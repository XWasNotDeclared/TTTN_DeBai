import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_game_show(data_json, product_id, guesses):
    """
    Giải bài toán đoán giá cho một test case.
    
    Args:
        data_json: dữ liệu JSON chứa thông tin sản phẩm
        product_id: id sản phẩm cần đoán
        guesses: list 4 giá dự đoán của 4 người chơi
    
    Returns:
        int: số thứ tự người thắng (1-4) hoặc -1 nếu không ai thắng
    """
    # Tìm giá thật của sản phẩm
    real_price = None
    for product in data_json:
        if product["id"] == product_id:
            real_price = product["price"]
            break
    
    if real_price is None:
        return -1
    
    # Tìm người thắng: đoán đúng hoặc thấp hơn gần nhất
    winner = -1
    best_guess = -1
    
    for i in range(4):
        guess = guesses[i]
        # Chỉ xét những dự đoán <= giá thật
        if guess <= real_price:
            # Nếu đây là dự đoán tốt hơn (gần giá thật hơn)
            if guess > best_guess:
                best_guess = guess
                winner = i + 1  # Người chơi đánh số từ 1
    
    return winner

def main():
    """
    Hàm chính đọc input từ bàn phím và xử lý
    """
    # Đọc dữ liệu từ file JSON
    try:
        data_json = load_json("./data/datas.json")
    except FileNotFoundError:
        print("Không tìm thấy file ./data/datas.json")
        return
    
    # Đọc số lượng test case
    t = int(input().strip())
    
    results = []
    for _ in range(t):
        # Đọc id sản phẩm
        product_id = int(input().strip())
        
        # Đọc 4 dự đoán
        guesses = list(map(int, input().strip().split()))
        
        # Giải và lưu kết quả
        result = solve_game_show(data_json, product_id, guesses)
        results.append(result)
    
    # In kết quả
    for result in results:
        print(result)

if __name__ == "__main__":
    main()