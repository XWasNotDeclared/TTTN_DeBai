import json

def load_pokemon_data():
    """
    Doc du lieu Pokemon tu file JSON
    """
    try:
        with open("./data/datas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["pokemon"]
    except FileNotFoundError:
        print("Không tìm thấy file ./data/datas.json")
        return []

def simulate_battle(pokemon1, pokemon2):
    """
    Mo phong tran chien giua 2 Pokemon
    
    Args:
        pokemon1, pokemon2: dict chua thong tin Pokemon
    
    Returns:
        int: id cua Pokemon thang
    """
    # Tao ban sao de khong thay doi du lieu goc
    p1 = pokemon1.copy()
    p2 = pokemon2.copy()
    p1_hp = p1["hp"]
    p2_hp = p2["hp"]
    
    # Xac dinh ai danh truoc (spd cao hon, neu bang thi id nho hon)
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
    else:  # spd bang nhau
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
    
    # Mo phong tran dau
    turn = 1
    while True:
        if turn % 2 == 1:  # Luot le: first_attacker danh
            damage = max(1, first_attacker["atk"] - second_attacker["def"])
            second_hp -= damage
            if second_hp <= 0:
                return first_attacker["id"]
        else:  # Luot chan: second_attacker danh
            damage = max(1, second_attacker["atk"] - first_attacker["def"])
            first_hp -= damage
            if first_hp <= 0:
                return second_attacker["id"]
        turn += 1

def main():
    # Doc du lieu Pokemon
    pokemon_list = load_pokemon_data()
    if not pokemon_list:
        return
    
    # Tao dictionary de truy xuat nhanh Pokemon theo id
    pokemon_dict = {p["id"]: p for p in pokemon_list}
    
    # Doc so luong tran chien
    t = int(input())
    
    # Xu ly tung tran chien
    for _ in range(t):
        a, b = map(int, input().split())
        pokemon1 = pokemon_dict[a]
        pokemon2 = pokemon_dict[b]
        
        winner_id = simulate_battle(pokemon1, pokemon2)
        print(winner_id)

if __name__ == "__main__":
    main()