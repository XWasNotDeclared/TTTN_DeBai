def do_suc_manh(ki_list):
    result = []
    exploded = False
    for k in ki_list:
        if exploded:
            result.append('?')
        elif k > 100000:
            result.append('?')
            exploded = True
        elif k <= 10:
            result.append('N')
        elif k <= 1000:
            result.append('S')
        elif k <= 100000:
            result.append('SS')
    return result

# Doc so luong test case
T = int(input())
for _ in range(T):
    n = int(input())
    ki_list = list(map(int, input().split()))
    output = do_suc_manh(ki_list)
    print(' '.join(output))
