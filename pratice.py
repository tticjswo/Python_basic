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

# List
subway = [10,20,30]
print(subway.index(20))
subway.append(40)
subway.insert(2,25)
subway.append(10)
subway.count(10)

num_list=[5,2,3,4,6]
print(num_list.sort())
print(num_list)
print(subway)

