import random 

#충돌수정
print("로또 번호 다섯 개 추첨합시다 !^^")

for i in range(5) :
    lotto = random.sample(range(1,46),6)
    print(lotto)


