class Item:
    def __init__(self, name, rarity, power):
        self.name = name
        self.rarity = rarity
        self.power = power

def solve(data):
    idx = 0
    N = data[idx]; idx += 1
    items = {}
    for _ in range(N):
        name = data[idx]; idx += 1
        rarity = data[idx]; idx += 1
        power = data[idx]; idx += 1
        items[name] = Item(name, rarity, power)

    Q = data[idx]; idx += 1
    result = []

    sorted_by_rarity = sorted(
        items.values(),
        key=lambda x: (-x.rarity, -x.power, x.name)
    )
    sorted_by_power = sorted(
        items.values(),
        key=lambda x: (-x.power, -x.rarity, x.name)
    )

    for _ in range(Q):
        query = data[idx]; idx += 1
        if query == "FIND":
            name = data[idx]; idx += 1
            if name in items:
                result.append(f"{items[name].rarity} {items[name].power}")
            else:
                result.append("NOT FOUND")
        elif query == "MAX_RARITY":
            result.append(sorted_by_rarity[0].name)
        elif query == "TOP":
            k = data[idx]; idx += 1
            top_items = sorted_by_power[:k]
            result.append(" ".join(item.name for item in top_items))
    return result

def main():
    data = []
    N = int(input())
    data.append(N)
    for _ in range(N):
        name, rarity, power = input().split()
        data.append(name)
        data.append(int(rarity))
        data.append(int(power))
    Q = int(input())
    data.append(Q)
    for _ in range(Q):
        parts = input().split()
        if parts[0] == "FIND":
            data.append("FIND")
            data.append(parts[1])
        elif parts[0] == "MAX_RARITY":
            data.append("MAX_RARITY")
        elif parts[0] == "TOP":
            data.append("TOP")
            data.append(int(parts[1]))
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
