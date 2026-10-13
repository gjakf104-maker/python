'''
#변수 선언
dic = {
    "name" : "김유신",
    "age" : 17 ,
    "number" : "010-1234-5678" ,
    "major" : ["science","computer"]
    }
print("name: ", dic["name"])
print("age: ", dic["age"])
print("number: ", dic["number"])
print("major: ", dic["major"])
print()


dic['name'] = "이순신"
print("name: ", dic["name"])
print(dic)
print()
print( dic["major"][0])


# 딕셔너리 선언
student1 = {
    "name" : "홍길동",
    "age" : 27,
    "addr" : "seoul" ,
    "major" : "statisitics",
    "number" : "010-1234-1234"}

# 입력
key = input(">> 원하는 정보는 :")

#입력힌 키값이 있으면 출력 하고
if key in student1:
    print(student1[key])
else:
    print("원하는 정보가 없습니다.")
# 딕셔너리 선언
student1 = {
    "name" : "홍길동",
    "age" : 27,
    "addr" : "seoul" ,
    "major" : "statisitics",
    "number" : "010-1234-1234"}

# 입력
value = student1.get("name")
print("값 :", value)

if value == "None":
    print("존재하지 않은 키에 접근")




student1 = {
    "name" : "홍길동",
    "age" : 27,
    "addr" : "seoul" ,
    "major" : "statisitics",
    "number" : "010-1234-1234"}
for key in student1:
    print(key,":", student1[key]) 
'''


# 학생들에 리스트 선언
students = [
    {"name" : "이순신", "korean" : 88, "english" : 78, "math" : 40 },
    {"name" : "김유신", "korean" : 98, "english" : 68, "math" : 50 },
    {"name" : "율  곡", "korean" : 68, "english" : 58, "math" : 60 },
    {"name" : "강감찬", "korean" : 58, "english" : 48, "math" : 60 },
    {"name" : "황  희", "korean" : 78, "english" : 38, "math" : 70 },
    {"name" : "궁  예", "korean" : 98, "english" : 28, "math" : 90 },
    ]

#학생을 한명씩 출력
print("이  름", "총  점", "평  균", sep = "\t")

for stud in students:
    total_sum = stud["korean"] + stud["english"] + stud["math"]
    avg = total_sum/3
    print(stud["name"], total_sum, avg)
