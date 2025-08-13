def solve(data):
    """
    data: list chứa input đã đọc theo định dạng:
    [N, key1_1, M_1, key2_1, K_1, val1, val2,..., ..., key1_N, M_N, key2_1, K_1, val1, ...]
    
    Trả về: list các dòng output theo định dạng đề bài.
    """
    n = data[0]
    idx = 1

    # Tạo dict ban đầu theo input: dict[key1] = {key2: [list]}
    orig_dict = {}

    for _ in range(n):
        key1 = data[idx]
        idx += 1
        m = data[idx]
        idx += 1
        orig_dict[key1] = {}
        for __ in range(m):
            key2 = data[idx]
            idx += 1
            k = data[idx]
            idx += 1
            vals = data[idx:idx+k]
            idx += k
            orig_dict[key1][key2] = vals

    # Đảo cấp độ dict: dict_new[key2][key1] = list
    from collections import defaultdict
    new_dict = defaultdict(dict)
    for key1, inner in orig_dict.items():
        for key2, vals in inner.items():
            new_dict[key2][key1] = vals

    # Chuẩn bị output:
    # Dòng đầu: số lượng key2 trong new_dict
    result = [str(len(new_dict))]

    # Duyệt từng key2, in theo định dạng đề
    # Do đề không bắt buộc thứ tự, ta in theo thứ tự key2 sắp xếp tăng dần
    for key2 in sorted(new_dict):
        result.append(key2)
        subdict = new_dict[key2]
        result.append(str(len(subdict)))
        for key1 in sorted(subdict):
            vals = subdict[key1]
            result.append(f"{key1} {len(vals)} {' '.join(map(str, vals))}")

    return result


def main():
    # Đọc input từ stdin theo định dạng đề
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    data = [n]
    for _ in range(n):
        key1 = input().strip()
        m = int(input().strip())
        data.append(key1)
        data.append(m)
        for __ in range(m):
            line = input().strip().split()
            key2 = line[0]
            k = int(line[1])
            vals = list(map(int, line[2:2+k]))
            data.append(key2)
            data.append(k)
            data.extend(vals)

    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()