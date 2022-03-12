# from random import *

# # print(random()) # 0.0 ~ 1.0미만의 값 생성

# # print(int(random()*10)) # 0 ~ 10 미만의 값 생성
# # print(int(random()*10 +1)) # 1~ 10 이하의 값


# # print(randrange(1,45)) # 1 ~ 45 미만의 값 생성

# # print(randint(1,45)) # 1 ~ 45 이하의 값 생성


 
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 ",date,"일로 선정되었습니다." )

# sentence1 = 'i m boy'
# print(sentence1)
# sentence2 = """
# hellow world
# i m a boy
# """
# print (sentence2)


# jumin = "970905-1023451"

# print("성별 :"+jumin[7])
# print("연 :"+jumin[:2])# 0부터 2미만
# print("월 :"+jumin[2:4])# 2부터 4미만
# print("일 :" + jumin[4:6])# 4부터 7미만
# print("7자리 :" + jumin[7:])


# python ="python is Amazing"
# print (python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("python","java"))

# index = python.index("n")
# print(index) 
# index = python.index("n",index+1) #두번쨰 n을 찾는 것
# print(index)

# print(python.find("java")) # 원하는 값이 없으면 -1
# #print(python.index("java")) # 원하는 값이 없으면 오류
# print(python.count('n'))

# print('a' + 'b')
# print('a','b')

# #방법 1
# print("im %d years old"% 20)
# print("my name is %s" % 'helloworld')
# print('apple starts with %c' % 'a')

# print('i like %s and %s ' % ('blue','black'))

# #방법 2
# print("im {} years old.".format(20))
# print("{} color and {} color".format('blue','red'))
# print("{1} color and {0} color".format('blue','red'))

# #방법 3
# print("i m {age} years old , {color} color is my favorite".format(color = 'red',age = '20'))

# #방법 4
# color = 'red'
# age = '20'
# print(f"i m {age}years old , i like {color}")

#탈출 문자
# print('hello wolrd for \nevery people')
# print('my name  is "henry".')
# print("my name is \"henry\".")
# print("way i am is \\C:")
# print("red \rapple")

# #Quiz
# url= 'http://naver.com'

# result = url.replace('http://','')
# print(result)
# result = result[:result.index(".")]
# print(result)

# password = result[:3] + str(len(result)) + str(result.count('e'))+"!"
# print("생성된 비밀번호는 %s 입니다."%password)

# # List
# subway = [10,20,30]
# print(subway.index(20))
# subway.append(40)
# subway.insert(2,25)
# subway.append(10)
# subway.count(10)

# num_list=[5,2,3,4,6]
# print(num_list.sort())
# print(num_list)
# print(subway)
# num_list.reverse()
# print(num_list)

# #dict
# cab = {3 : "hello",4 : "world"} # key : value
# print(cab[4])
# print(cab.get(5,"poo"))
# print(5)
# print( 3 in cab)
# cab[5] = "bye"
# del cab[3]# 키 삭제
# print(cab)
# print(cab.keys())
# print(cab.values())
# print(cab.items())
# cab.clear()
# print(cab)

# #tuple // 속도가 리스트 보다 빠르지만 변경 할수 가 없다.
# menu = ("A","B")
# print(menu[0])
# print(menu[1])

# (name , age, hobby) =('kim ', 20 , 20)
# print(name)

# #set 집합 // 중복이 안되고 순서가 없음
# my_set ={1,2,3,3,5}
# print(my_set)

# java = {'kim','sang','hyun'}
# python = set(["kim","ki"])

# #교집합 
# print (java & python) # print(java.intersection(python))
# #합집합
# print(java | python) # print(java.union(python))
# #차집합
# print (java - python) # print(java.difference(python))

# python.add('cha')
# print(python)

# java.remove('kim')
# print(java)

#자료구조 변경


# menu = {'coffee', 'milk'}

# print(menu ,type(menu))
# menu= list(menu)
# print(menu , type(menu))
# menu = tuple(menu)
# print(menu, type (menu))

# from random import *

# #st = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
# st = list(range(1,21))
# st = set(st)
# peo = sample(st,3)
# shuffle(peo)
# print('first prize = %d second prize = %d and %d' % (peo[0],peo[1],peo[2]))


# weather = input("whats's the weather ? ")
# if weather == 'rain' :
#     print('rain')
# elif weather =='no_rain':
# #     print('no rain')

# temp = int(input("what temp ?"))
# if temp<=10 & temp >=0:
#     print('hello')
#     print(temp)

# for waiting_num in range(1,6) :
#     print('num : {0}'.format(waiting_num))

# stars = ['man ','woman', 'baby']

# for customer in stars :
#     print( '{0}'.format(customer))

# cus = 'thor'
# person = 'unknown'
# while person != cus :
#     print("{0}, order is ready ".format(cus))
#     person = input("what's your name : ")

# absent = [2,5]
# no_book = [3]
# for student in range(1,11) :
#     if student in absent :
#         continue
#     elif student in no_book :
#         break
#     else :
#         print(student ,'번')

# students =range(1,6)
# print (students)
# students = [i+100 for i in students]
# print(students)

# students = ['kim','thor','root']
# #students = [len(i) for i in students]
# students = [i.upper() for i in students]
# print(students)

# from random import *
# count = 0

# cus = {}
# for i in range(1,51) :
#     cus[i]= int(random()*45 +5) 
#     if cus[i] >=5 and cus[i]<=15 :
#         print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(i,cus[i]))
#         count+=1
#     else :
#         print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i,cus[i]))

# print('총 탑승 승객 : {0}분 '.format(count))



# def profile( name , age=15, *main_lang) :
#     print ("이름 : {0}\t 나이 : {1} ".format(name , age), end=" ")
#     for lang in main_lang :
#         print(lang , end=' ')
#     print()
# profile('kim', 12, 'java','python')

# gun  =10
# def checkpoint(soldiers) :
#     global gun 
#     gun = gun - soldiers
#     print('남은 총 : {0}'.format(gun))

# def checkpoint_return (gun ,soldiers) :
#     gun = gun - soldiers
#     print ('함수 내 남은 총 : %d' %gun)
#     return gun

# print('전체 총 : {0}'.format(gun))
# gun = checkpoint_return(gun,2)
# print('전체 총 : {0}'.format(gun))


# def std_weight(height , sex) :
#     height = height /100
#     if sex == 'man'  :
#         return height * height *22
#     else :
#         return height * height * 21

# height = int(input('plz input your height: '))   
# sex = input('plz input your sex :')
# if sex == 'man' :
#     print("키 {0}cm 남자의 표준 체중은 {1}입니다. ".format(height,std_weight(height,sex)))
# elif sex=='woman' :
#     print("키 {0}cm 여자의 표준 체중은 {1}입니다. ".format(height,std_weight(height,sex)))
# else :
#     print('plz input correct sex')

# scores={"math" : 0 ,"eng" : 1}
# for subject , score in scores.items():
#     print(subject.ljust(8) , str(score).rjust(4))

# for number in range(1,21) :
#     print(" 대기번호 : " +str(number).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 "+ answer +"입니다.")

# print ("{0: >10}".format(500))
# print ("{0:>+10}".format(500))
# print("{0: >-10}".format(500))

# print("{0:_>+40}".format(100000000000000000))
# #{0:(빈자리에 채울 문자)(+/-)(차지할 공간)}

# #소수점 출력
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))

# score_file = open("score.txt","w",encoding = "utf8")
# print("수학 : 0 ",file = score_file)
# print("영어 : 50",file = score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 100")
# score_file.write("\n코딩 :100")
# score_file.close()

from cgitb import html


score_file = open("score.txt","r",encoding = "utf8")
# print(score_file.read())
# score_file.close()

# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")

# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line,end="")
# score_file.close()

# lines = score_file.readlines()
# for line in lines :
#     print(line,end="")
# score_file.close()


# #pickles
# import pickle
# # profile_file = open("profile.pickle","wb")
# # profile = {"이름":"박명수","나이":30,"취미": ["축구","골프","코딩"]}
# # print(profile)
# # pickle.dump(profile,profile_file)
# # profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# import pickle
# with open("profile.pickle","rb") as profile_file :
#     print(pickle.load(profile_file))

# with open("study.txt","w", encoding = "utf8") as study_file :
#     study_file.write("공부 하는중")

# with open("study.txt","r",encoding="utf8") as study_file :
#     print(study_file.read())

# for num in range(1,6) :
#     with open("{0}주차.txt".format(num),"w",encoding='utf8') as document :
#         document.write(
#             """- {0} 주차 주간보고 - 
# 부서 : 
# 이름 :
# 업무 요약 :
#             """.format(num))

# #class
# class Unit :
#     def __init__(self, name , hp ,speed) :
#         self.name = name
#         self.hp =hp
#         self.speed  = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name,location,self.speed))

# class AttackUnit(Unit) :
#     def __init__(self, name , hp ,speed , damage) :
#         Unit.__init__(self,name,hp,speed)
#         self.damage = damage
       
#     def attack(self,location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 :{2}]".format(self.name,location,self.damage))

#     def damaged(self, damage) :
#         self.hp -= damage 
#         print("{0} : {1} 데미지를 입었습니다. \n현재 체력은 {2} 입니다.".format(self.name,damage,self.hp))
#         if self.hp <=0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self,name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name,location,self.flying_speed))


# class FlyableAttackUnit(AttackUnit,Flyable) :
#     def __init__(self,name,hp,damage,flying_speed) :
#         AttackUnit.__init__(self,name,hp,0,damage)
#         Flyable.__init__(self,flying_speed)
#     def move(self,location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name,location)

# class BuildingUnit(Unit) :
#     def __init__(self,name, hp,location) :
#         Unit.__init__(self,name,hp,0)
#         super().__init__(name,hp,0)
#         self.location= location


# supply_depot = BuildingUnit("서플라이 디폿",500,"7시")
    

# vulture = AttackUnit("벌처",80,10,20)
# battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

# vulture.move('11시')
# battlecruiser.move('11시')




# class House :
#     def __init__(self,location,house_type,deal_type, price,completion_year) :
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#     def show_detail(self) :
#         print ('{0} {1} {2} {3} {4}'.format(self.location, self.house_type, self.deal_type,self.price, self.completion_year))
#         pass


# A1 = House("강남","아파트","매매",'10억',2010)
# O1 = House("마포","오피스텔","전세",'5억',2000)
# B1 = House("송파","빌라","월세",'500/50',2000)

# HouseList = []
# HouseList.append(A1)
# HouseList.append(O1)
# HouseList.append(B1)

# print('총 {}대의 매물이 있습니다.'.format(len(HouseList)))
# for house in HouseList :
#     house.show_detail()

#예외 처리

# try:
#     print ("나누기 전용 계싼기 ")
#     nums = []
#     nums.append(int(input('숫자르 입력하세요 : ')))
#     nums.append(int(input('숫자르 입력하세요 : ')))
#     nums.append(int(nums[0]/nums[1]))
#     print('{0} / {1} = {2}'.format(nums[0],nums[1],nums[2]))

# except ValueError :
#     print('에러! 잘못된 값을 읿력하였습니다.')

# except ZeroDivisionError as err:
#     print(err)

# except Exception as err:
#     print('알수 없는 오류가 발생하였습니다.')
#     print(err)


#error 발생

# try :
#     print('한자리 숫자 나누기 전용 계산기 입니다.')
#     num1 = int(input('첫번째 숫자 : '))
#     num2 = int(input('두번쨰 숫자 :'))
#     if num1>=10 or num2>=10 :
#         raise ValueError
#     print ("{0}/ {1} = {2}".format(num1,num2,int(num1/num2)))

# except ValueError :
#     print('잘못된 값을 입력하였습니다.')

#사용자 정의 예외 처리

# class BigNumberError(Exception) :
#     def __init__(self,msg) :
#         self.msg = msg

#     def __str__(self) :
#         return self.msg

# try :
#     print('한자리 숫자 나누기 전용 계산기 입니다.')
#     num1 = int(input('첫번째 숫자 : '))
#     num2 = int(input('두번쨰 숫자 :'))
#     if num1>=10 or num2>=10 :
#         raise BigNumberError('입력값 : {0}, {1}'.format(num1,num2))
#     print ("{0}/ {1} = {2}".format(num1,num2,int(num1/num2)))

# except BigNumberError as err :
#     print('잘못된 값을 입력하였습니다.')
#     print(err)

# finally :
#     print('감사합니다')

# class SoldOutError(Exception) :
#     def __init__(self,msg) :
#         self.msg = msg

#     def __str__(self):
#         return self.msg
    
# try:
#     chicken =10 
#     waiting = 1
#     while(True) :
#         print("[남은 치킨] : {0}".format(chicken))
        

#         order = int(input('치킨 몇마리 주문 하시겠습니까? : '))
#         if order <= 0 :
#             raise ValueError
#         if order > chicken : 
#             print("재료가 부족합니다.")
        
#         else :
#             print("[대기 번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order))
#             waiting+=1
#             chicken-=order
#         if chicken ==0 :
#             raise SoldOutError('재고가 소진되어 더이상 주문을 받지 않습니다.')

# except ValueError :
#     print('잘못된 값을 입력하셨습니다.')

# except SoldOutError as err:
#     print(err)
    

# import theather_module as mv
# mv.price(3) 
# mv.price_morning(4)
# mv.price_soldier(5)

# from theather_module import *

# price(3)
# price_morning(4)

# from travel import *

# trip_to = thailand.ThailandPackage()

# # trip_to.detail()
# from travel import *
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


#input : 사용자 입력을 받는 함수

# import random
# print(dir())

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))


#time
# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

from byme import byMePackage

byMePackage.print_byme()