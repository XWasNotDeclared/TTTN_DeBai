import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def simulate_battle(pokemon1, pokemon2):
    """
    Mô phỏng trận chiến giữa 2 Pokemon
    
    Args:
        pokemon1, pokemon2: dict chứa thông tin Pokemon
    
    Returns:
        int: id của Pokemon thắng
    """
    # Tạo bản sao để không thay đổi dữ liệu gốc
    p1 = pokemon1.copy()
    p2 = pokemon2.copy()
    p1_hp = p1["hp"]
    p2_hp = p2["hp"]
    
    # Xác định ai đánh trước (spd cao hơn, nếu bằng thì id nhỏ hơn)
    if p1["spd"] > p2["spd"]:
        first_attacker = p1
        second_attacker = p2
        first_hp = p1_hp
        second_hp = p2_hp
    elif p1["spd"] < p2["spd"]:
        first_attacker = p2
        second_attacker = p1
        first_hp = p2_hp
        second_hp = p1_hp
    else:  # spd bằng nhau
        if p1["id"] < p2["id"]:
            first_attacker = p1
            second_attacker = p2
            first_hp = p1_hp
            second_hp = p2_hp
        else:
            first_attacker = p2
            second_attacker = p1
            first_hp = p2_hp
            second_hp = p1_hp
    
    # Mô phỏng trận đấu
    turn = 1
    while True:
        if turn % 2 == 1:  # Lượt lẻ: first_attacker đánh
            damage = max(1, first_attacker["atk"] - second_attacker["def"])
            second_hp -= damage
            if second_hp <= 0:
                return first_attacker["id"]
        else:  # Lượt chẵn: second_attacker đánh
            damage = max(1, second_attacker["atk"] - first_attacker["def"])
            first_hp -= damage
            if first_hp <= 0:
                return second_attacker["id"]
        turn += 1

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính.
    
    Args:
        data_json: dữ liệu JSON đã load.
        input_data: dữ liệu input từ file .in, dạng list các dòng.
    
    Returns:
        list: danh sách kết quả (id Pokemon thắng) tương ứng với từng trận đấu.
    """
    pokemon_list = data_json["pokemon"]
    pokemon_dict = {p["id"]: p for p in pokemon_list}
    
    results = []
    t = int(input_data[0])
    
    for i in range(1, t + 1):
        a, b = map(int, input_data[i].split())
        pokemon1 = pokemon_dict[a]
        pokemon2 = pokemon_dict[b]
        
        winner_id = simulate_battle(pokemon1, pokemon2)
        results.append(winner_id)
    
    return results

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Trả về danh sách file .in trong thư mục.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile, data_json):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    
    Args:
        infile: tên file input
        data_json: dữ liệu từ JSON
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Processing {infile} -> {outfile} ...")
    
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu file .in theo định dạng bài
        input_data = [line.strip() for line in fin]
        
        # Gọi hàm solve
        res = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    # 1. Load dữ liệu JSON
    data_json = load_json("./data/datas.json")
    
    # 2. Chuẩn bị danh sách file input
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    
    # 3. Xử lý từng file
    for infile in sorted(in_files):
        process_file(infile, data_json)

if __name__ == "__main__":
    main()