'''#핸드폰 번호 관련

friends = {}
#{name, number}
while True:
    print("1. 친구목록 보기")
    print("2. 친구 추가 하기")
    print("3. 친구 삭제 하기")
    print("4. 친구이름 변경")
    print("5. 종료하기")

    menu = int(input("메뉴를 선택: "))

    if menu == 1:
        
        if not friends:
            print("등록된 친구가 없습니다.")
        else:
            for name, number in friends.items():
                print(f"이름: {name}, 번호: {number}")

    if menu == 2:
        name = input("추가할 이름을 입력:")
        number = input("추가할 번호를 입력:")
        friends[name] = number


    if menu == 3:
        
        del_name = input("삭제하고자 하는 이름")
        if del_name not in friends:
            print("삭제하고자 하는 이름이 없습니다.")
        else:
            del friends[del_name]
            print(f"{del_name}이 삭제되었습니다.")

    if menu == 4:
        edit_name = input("변경하고자 하는 이름:")
        if edit_name in friends:
            del friends[edit_name]
        new_name = input("추가할 사람:")
        number = input("번호 입력:")
        friends[new_name] = number


    if menu == 5:
        print("종료합니다 ㅂㅇ")
        break
'''
#학생 성적 관리 프로그램

scores = {}
menu = 0

print("1. 전체 성적 보기")
print("2. 성적 입력")
print("3. 학생 검색")
print("4. 성적 삭제")
print("5. 종료합니다 ㅂㅇ")

while True:
    menu = int(input("메뉴 입력:"))
    if menu == 1:
        if not scores:
            print("아직 성적 입력전입니다.")
        else:
            for name, score in scores.items():
                print(f"이름: {name}, 점수: {score}")
    if menu == 2:
        new_name = input("이름을 입력:")
        new_score = int(input("성적을 입력:"))
        scores[new_name] = new_score
        print(f"{new_name}의 {new_score}가 추가되었습니다")
        
    if menu == 3:
        search = input("검색할 학생의 이름:")
        if search not in scores:
            print("학생을 찾을 수 없습니다.")
        else:
            print(f"{search}의 점수: {scores[search]}")
#성적 삭제
    if menu == 4:
        del_name = input("삭제할 이름 입력:")
        if del_name not in scores:
            print("삭제할 이름이 없슫다")
        else:
            del scores[del_name]
        
        
    

    if menu == 5:
        print("종료 ㅂㅇ")
        break
               
























