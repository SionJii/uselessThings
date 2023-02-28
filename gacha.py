# 전체 (경우의수 - (1 - 성공확률)^시행횟수)*100 = 전체 경우의수 - nCr*(p^r)*(1-p)^(n-r) (r=0) 하나도 안 나올 경우의수
chance = float(input('확률 입력'))
trial = int(input('시행횟수 입력'))


def get_chance(chance, trial):
    return((1-(1-chance/100)**trial)*100)


print(f"당첨 확률: {get_chance(chance, trial)}")

'''
def get_needed_trial(chance, target_chance):
    trial = 1
    while target_chance > get_chance(chance, trial):
        trial += 1
    return(trial)


print(get_needed_trial(0.00077, 99))
'''
