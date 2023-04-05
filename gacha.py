# 전체 (경우의수 - (1 - 성공확률)^시행횟수)*100 = 전체 경우의 수 - 하나도 안 나올 경우의 수
chance = float(input('확률 입력(%): '))
trial = int(input('시행횟수 입력: '))


def get_chance(chance, trial):
    return((1-(1-chance/100)**trial)*100)


print(f"당첨 확률: {get_chance(chance, trial)}")
