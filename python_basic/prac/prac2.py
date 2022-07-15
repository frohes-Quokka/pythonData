# weather = input("오늘의 날씨 ")
# if weather == "비" or weather == "눈":
#     print("우산챙겨")
# elif weather == "미세먼지":
#     print("마스크챙겨")
# else:
#     print("나가자!")

# temp = int(input("오늘의 기온 "))
# if 30 <= temp:
#     print("너무더워! 외출금지!")
# elif 10<= temp <30:
#     print("날씨좋네~")
# elif 0 <= temp and temp <10:
#     print("외투챙기자~")
# else:
#     print("너무 춥다! 외출금지!")

# for waiting_no in [0,1,2,3,4]:
#     print("waiting list : {0}".format(waiting_no))

# for waiting_no in range(1,6): #[0,1,2,3,4,5]
#     print("waiting list : {0}".format(waiting_no))    

# starbucks = ["Ironman","Thor","Loki","Spiderman"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))


#while
# customer1 = "Thor"
# index1 = 5
# while index1 >= 1:
#     print("{0}님, 커피가 준비되었습니다. 폐기처분까지 {1}번 남았어요.".format(customer1, index1))
#     index1 -= 1
#     if index1 ==0:
#         print("커피는 폐기처분되었습니다.")

# customer2 = "Ironman"
# index2 = 1
# while True:
#     print("{0}님, 커피가 준비되었습니다. 호출{1}회".format(customer2, index2))
#     index2 += 1  #무한루프 돌때 ctrl C 누르면 멈춤
#     break

# customer3 = "Loki"
# person = "unknown"

# while person != customer3:
#     print("{0}님, 커피가 준비되었습니다.".format(customer3))
#     person = input("닉네임이 어떻게 되세요? ")

# if person == customer3:
#     print("어서요세요 {0}님!".format(customer3))

# absent = [1,3,4] #1,3,4번 학생들은 결석함
# no_book = [7,8] #7,8번 학생들은 책을 안가져옴
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("책이없어? {0}번학생 교무실로 따라오세요".format(student))
#         break
#     print("{0}번학생, 책 읽어봐".format(student))

#출석번호가 1, 2, 3, 4 앞에 100을 붙이기로 함 --> 101, 102, 103, 104
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students) #[101, 102, 103, 104, 105]

#학생 이름을 대문자로 변환
student = ["ironman","spiderman","thor","iamgroot"]
student = [i.upper() for i in student]
print(student) #['IRONMAN', 'SPIDERMAN', 'THOR', 'IAMGROOT']

#학생 이름을 길이로 변환
studenten = ["ironman","spiderman","thor","iamgroot"]
studenten = [len(i) for i in studenten]
print(studenten)  #[7, 9, 4, 8]