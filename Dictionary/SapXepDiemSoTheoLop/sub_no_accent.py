def solve(data):
    """
    data: list chua du lieu da doc tu input theo format:
      - data[0] = N (so hoc sinh)
      - sau do moi hoc sinh co:
        + 1 dong ten (string)
        + 1 dong so mon M (int)
        + M dong mon hoc va diem so (string va int)
    => do dau vao tron giua string va int nen can xu ly hoi khac.

    Tra ve list cac dong output.
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
        # sap xep theo diem tang dan
        subjects.sort(key=lambda x: x[1])
        # ghi ket qua
        res.append(name)
        for s, sc in subjects:
            res.append(f"{s} {sc}")

    return res

def main():
    # Doc input theo dinh dang de, du lieu hon hop string va int, nen doc thu cong
    N = int(input().strip())
    data = [N]
    for _ in range(N):
        name = input().strip()
        M = int(input().strip())
        data.append(name)
        data.append(M)
        for __ in range(M):
            line = input().strip().split()
            # line[0] = mon hoc (string), line[1] = diem (int)
            data.append(line[0])
            data.append(int(line[1]))

    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
