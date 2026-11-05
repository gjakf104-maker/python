'''
def create_student(name, korean, english, math):
    return {"name": name, "korean" : korean, "english" : english,"math" : math}

def student_sum(student):
    return student["korean"] + student["english"] + student["math"]

def student_avg(student):
    return student_sum(student)/3

def student_print(student):
    return "{}\t{}\t{}".format(student["name"],
                               student_sum(student),
                               student_avg(student))

student = [
        create_student("홍길동", 78, 80, 90),
        create_student("이순신", 88, 80, 93),
        create_student("권율", 78, 89, 95),
        create_student("김유신", 90, 80, 90)
        ]

print("이름", "총점", "평균", sep="\t")
for std in student:
    print(student_print(std))
'''

class Student:
    def __init__(self):
        pass

student = Student()

print(isinstance(student,Student))
