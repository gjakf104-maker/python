'''menu = 0
name = ""

print("=====================================")
Friend = ["홍길동", "김유신","오상민"]
print("1. 친구목록 보기 \n2. 친구 추가하기 \n3. 친구 삭제하기 \n4. 친구이름 변경 \n5. 종료하기")
menu = int(input("메뉴를 선택: "))
while True:
    
    if menu == 1:
        print(Friend)
        break
    elif menu == 2:
        name = input("친구 이름 입력:")
        Friend.append(name)
        print(Friend)
        break  
    elif menu == 3:
        print(Friend)
        name = input("삭제할 친구 이름 입력:")
        Friend.remove(name)
        print(Friend)
        break
    elif menu == 4:
        print(Friend)
        name = input("변경할 친구 이름 입력:")
        Friend.remove(name)
        Cname = input("새로운 이름을 입력")
        Friend.append(Cname)
        print(Friend)
        break
        

    else:
       print("종료합니다")
       break
'''
menu = 0 #사용자가 선택하는 번호를 담을 변
friends = [] #친구 저장할 때 리스트에 추가

while menu != 5:
    print("==============================")
    print("1. 친구목록 보기")
    print("2. 친구 추가하기")
    print("3. 친구 삭제하기")
    print("4. 친구이름 변경")
    print("5. 종료하기")

    menu = int(input("메뉴를 선택하시오 "))

    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("추가하고자 하는 이름을 입력 :")
        friends.append(name)
    elif menu == 3:
        del_name = input("삭제할 친구 이름 입력 :")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("삭제하고자 하는 이름이 없습니다.")
    elif menu == 4:
        edit_name = input("변경하고자 하는 이름 :")
        if edit_name in friends:
            index = friends.index(edit_name)
            new_name = input("새로운 이름을 입력 :")
            friends[index] = new_name
    else:
        print("종료!!!!!!!!!!!!!")
 ######################################################################       

        
               
          
    


























