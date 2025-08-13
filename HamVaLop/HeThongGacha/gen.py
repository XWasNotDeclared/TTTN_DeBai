import os

class Item:
    def __init__(self, name, rarity, power):
        self.name = name
        self.rarity = rarity
        self.power = power

def solve(data):
    idx = 0
    N = int(data[idx]); idx += 1
    items_by_name = {}
    all_items = []

    for _ in range(N):
        name = data[idx]; idx += 1
        rarity = int(data[idx]); idx += 1
        power = int(data[idx]); idx += 1
        item = Item(name, rarity, power)
        items_by_name[name] = item
        all_items.append(item)

    max_rarity_item = sorted(all_items, key=lambda x: (-x.rarity, -x.power, x.name))[0]
    sorted_by_power = sorted(all_items, key=lambda x: (-x.power, -x.rarity, x.name))

    Q = int(data[idx]); idx += 1
    res = []
    for _ in range(Q):
        cmd = data[idx]; idx += 1
        if cmd == "FIND":
            name = data[idx]; idx += 1
            if name in items_by_name:
                it = items_by_name[name]
                res.append(f"{it.rarity} {it.power}")
            else:
                res.append("NOT FOUND")
        elif cmd == "MAX_RARITY":
            res.append(max_rarity_item.name)
        elif cmd == "TOP":
            k = int(data[idx]); idx += 1
            names = [sorted_by_power[i].name for i in range(k)]
            res.append(" ".join(names))
    return res

def prepare_working_dir():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        data = fin.read().strip().split()
        res = solve(data)
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()
