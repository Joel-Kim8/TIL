# # 1. 기초 자료형
# number = 3 #숫자
# # print (number)
# # print(type(number))
# string = '문자열' # 문자열
# # print(string)
# # print(type(string))
# boolean = True  # Boolean
# # print(boolean)
# # print(type(boolean))

# string_number = '3'  # 형 변환
# # print(string_number + 5)
# # print(int(string_number)+5)


# #2. f-string (string interpolation - 문자열 안에 변수 삽입)
# name = '김영균'
# print('제 이름은' + name + '입니다.')
# print(f'제 이름은 {name}입니다.')

# # 3. List
# my_list = ['python', 'html', 'markdown']
# print(my_list[2], my_list)
# my_list[2] = 'java'
# print(my_list[2], (my_list))

# #4. Dictionary
# #딕셔너리 선언
# age_dict = {
#     '김영균': 27,
#     '아아아': 55,
# }


# # 딕셔너리 요소(원소) 접근
# # print(age_dict(['김영균'])
# # print(age_dict['아아아'])
# # print(age_dict.get('김영균'))

# # 딕셔너리 요소 변경
# age_dict['김영균'] = 18
# # print(age_dict['김영균'])

# # 기초 연산자
# # print(3+5)
# # print(5-3)
# # print(3*5)
# # print(100/5) #나누기
# # print(100//3) #몫
# # print(100%3) #나머지
# # print(2**5) #제곱

# #비교연산자
# print(5==5) 
# print(5=='3')
# print(5!=3)
# print(5>=3)
# print(5<3)


# #조건문

# n= 11
# #1. 주어진 양수 n이 홀수, 짝수인지 판단하여 출력하는 코드를 작성해라.
# if n%2 ==1:
#     print('홀수')
# else : 
#     print('짝수')

# #2. 주어진 숫자 n이 양수인지, 0인지, 음수인지 판단하여 출력하는 코드


# 반복문
# numbers = [1,2,3]
# for i in numbers:
#     print(i)

numbers = range(1,10)
for i in numbers:
    if i%2:
        print(f'숫자 {i}는 홀수네요!')
    else:
        print('짝수는 싫어')
