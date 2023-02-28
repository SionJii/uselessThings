while True:
    a, b = map(int, input().split())
    if a - b < 0:
        print('No')
    elif a - b > 0:
        print('Yes')
    else:
        break
