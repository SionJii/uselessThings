N_0 = 1
D_0 = 1
N_1 = 3
D_1 = 2
N = 0
D = 0

for i in range(1, 1001):
    N = 2*N_1+N_0
    D = 2*D_1+D_0

    N_0 = N_1
    N_1 = N
    D_0 = D_1
    D_1 = D

    print(i, "번째 스텝", 2**(1/2)-N/D)
