import os

class Pokemon:
    def __init__(self, ten, loai, cp, hp):
        self.__ten = ten
        self.__loai = loai
        self.__cp = cp
        self.__hp = hp
    
    # Getter methods
    def getTen(self):
        return self.__ten
    
    def getLoai(self):
        return self.__loai
    
    def getCp(self):
        return self.__cp
    
    def getHp(self):
        return self.__hp
    
    # Setter methods
    def setTen(self, ten):
        self.__ten = ten
    
    def setLoai(self, loai):
        self.__loai = loai
    
    def setCp(self, cp):
        self.__cp = cp
    
    def setHp(self, hp):
        self.__hp = hp
    
    def xepHang(self):
        if self.__cp >= 3000:
            return "Huyen thoai"
        elif self.__cp >= 2000:
            return "Manh me"
        elif self.__cp >= 1000:
            return "Binh thuong"
        else:
            return "Yeu"
    
    def coTheChien(self):
        return self.__hp > 0
    
    def sauChien(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
    
    def inThongTin(self):
        return f"Ten: {self.__ten}, Loai: {self.__loai}, CP: {self.__cp}, HP: {self.__hp}, Hang: {self.xepHang()}"

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách string đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả.
    """
    idx = 0
    n = int(data[idx])
    idx += 1
    
    # Tạo danh sách Pokemon
    pokemons = {}
    result = []
    
    # Đọc thông tin N Pokemon
    for _ in range(n):
        parts = data[idx].split()
        ten = parts[0]
        loai = parts[1]
        cp = int(parts[2])
        hp = int(parts[3])
        pokemon = Pokemon(ten, loai, cp, hp)
        pokemons[ten] = pokemon
        result.append(pokemon.inThongTin())
        idx += 1
    
    # Đọc số trận chiến
    m = int(data[idx])
    idx += 1
    
    # Xử lý M trận chiến
    for _ in range(m):
        parts = data[idx].split()
        ten_pokemon = parts[0]
        damage = int(parts[1])
        if ten_pokemon in pokemons:
            pokemons[ten_pokemon].sauChien(damage)
        idx += 1
    
    # In trạng thái sau chiến
    for ten, pokemon in pokemons.items():
        hp = pokemon.getHp()
        co_the_chien = "YES" if pokemon.coTheChien() else "NO"
        result.append(f"{ten}: HP = {hp}, Co the chien = {co_the_chien}")
    
    return result

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Tìm và trả về danh sách tất cả các file .in trong thư mục đó.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r", encoding='utf-8') as fin, open(outfile, "w", encoding='utf-8') as fout:
        # Đọc dữ liệu từ file input
        data = fin.read().strip().split('\n')
        # Gọi hàm giải
        res = solve(data)
        # Ghi kết quả ra file output
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    """
    Hàm chính: tìm các file input, xử lý từng file, tạo file output.
    """
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()