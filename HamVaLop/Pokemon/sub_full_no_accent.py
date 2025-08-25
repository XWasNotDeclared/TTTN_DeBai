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

    # Xep hang
    def xepHang(self):
        if self.__cp >= 3000:
            return "Huyen thoai"
        elif self.__cp >= 2000:
            return "Manh me"
        elif self.__cp >= 1000:
            return "Binh thuong"
        else:
            return "Yeu"

    # Co the chien
    def coTheChien(self):
        return self.__hp > 0

    # Sau chien
    def sauChien(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

    # In thong tin
    def inThongTin(self):
        return f"Ten: {self.__ten}, Loai: {self.__loai}, CP: {self.__cp}, HP: {self.__hp}, Hang: {self.xepHang()}"

def main():
    n = int(input())
    pokemons = []
    ten_map = {}

    # Nhap thong tin Pokemon
    for _ in range(n):
        parts = input().split()
        ten, loai, cp, hp = parts[0], parts[1], int(parts[2]), int(parts[3])
        p = Pokemon(ten, loai, cp, hp)
        pokemons.append(p)
        ten_map[ten] = p
        print(p.inThongTin())

    # Nhap so tran chien
    m = int(input())
    for _ in range(m):
        parts = input().split()
        ten_pokemon, damage = parts[0], int(parts[1])
        if ten_pokemon in ten_map:
            ten_map[ten_pokemon].sauChien(damage)

    # In trang thai sau chien
    for p in pokemons:
        co_the_chien = "YES" if p.coTheChien() else "NO"
        print(f"{p.getTen()}: HP = {p.getHp()}, Co the chien = {co_the_chien}")

if __name__ == "__main__":
    main()
