def solve(data):
    """
    data: list chứa dữ liệu đã đọc từ input theo format:
      - data[0] = N (số học sinh)
      - sau đó mỗi học sinh có:
        + 1 dòng tên (string)
        + 1 dòng số môn M (int)
        + M dòng môn học và điểm số (string và int)
    => do đầu vào trộn giữa string và int nên cần xử lý hơi khác.

    Trả về list các dòng output.
    """

    res = []
    idx = 0
    N = data[idx]
    idx += 1

    for _ in range(N):
        name = data[idx]
        idx += 1
        M = data[idx]
        idx += 1
        subjects = []
        for __ in range(M):
            subj = data[idx]
            score = data[idx+1]
            idx += 2
            subjects.append((subj, score))
        # sắp xếp theo điểm tăng dần
        subjects.sort(key=lambda x: x[1])
        # ghi kết quả
        res.append(name)
        for s, sc in subjects:
            res.append(f"{s} {sc}")

    return res

def main():
    # Đọc input theo định dạng đề, dữ liệu hỗn hợp string và int, nên đọc thủ công
    N = int(input().strip())
    data = [N]
    for _ in range(N):
        name = input().strip()
        M = int(input().strip())
        data.append(name)
        data.append(M)
        for __ in range(M):
            line = input().strip().split()
            # line[0] = môn học (string), line[1] = điểm (int)
            data.append(line[0])
            data.append(int(line[1]))

    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
