while 1:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    cnt = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            k = x - i - j
            if j < k <= n:
                cnt += 1
    print(cnt)