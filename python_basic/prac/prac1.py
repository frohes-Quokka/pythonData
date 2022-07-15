from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,2))

users = range(1,21) #1부터 20까지 숫자 생성
# print(type(users)) #<class 'range'> range는 리스트가 아니라서 리스트에서 쓰고자 하는 함수를 쓸 수 없음
users = list(users) #range타입을 리스트로 변환
# print(type(users)) #<class 'list'>
print(users)
shuffle(users)
print(users)

winners = sample(users,4) #4명 중에서 1명은 치킨, 3명은 커피
print("--당첨자발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")

# print("--당첨자 발표--")
# chi = sample(lst,1)
# cof = sample(lst,3)
# print("치킨당첨자:" + chi )
# print("커피당첨자:" + cof )
