for L in range(2,30):
    print(f'L={L}')
    for k in range(1, L - 1):
        print('\tk=%2d' % k, end='')
        seen = set()
        idx = 0
        while True:
            print(' %2d' % idx, end='')
            if idx in seen:
                break
            seen.add(idx)
            idx = (idx + k) % L
        print()
