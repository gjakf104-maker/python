menu = 0


while True:
    print("===================")
    print("1. 친구 목록 보기")
    print("2. 친구 목록 추가")
    print("3. 친구 이름 삭제")
    print("4. 친구 이름 변경")
    print("5. 종 료 하 기")

    menu = int(input("메뉴를 선택하십시요 : "))

    if menu == 1:
        f = open("c://pythondata//fri1.txt", "r")
        fri = f.readlines()
        f.close()
        if not fri:
            print("저장된 친구항목이 없습니다.")
        else:
            print(fri)
            
    elif menu == 2:
        name = input("추가할 이름 입력: ")
        f = open("c://pythondata//fri1.txt", "w")
        f.write(name)
        f.close()
        print(f"{name}이 추가되었습니다")
        

    elif menu == 3:
        f = open("c://pythondata//fri1.txt","r")
        fri = f.readlines()
        del_name = input("삭제할 이름 입력: ")
        if del_name not in fri:
            print("삭제할 이름이 없습니다")
        elif del_name in fri:
            f = open("c://pythondata//fri1.txt","w")
            place = f.read()
            place.replace(del_name,"")
            f.close()
            print(f"{del_name}이 삭제되었습니다")
            
    elif menu == 4:
        c_name = input("변경할 친구이름 입력: ")
        f = open("c://pythondata//fri1.txt","r")
        fri = f.readlines()
        f.close()
        if c_name not in fri:
            print("변경할 이름이 없습니다")
        else:
            edit_name = input("추가할 이름 추가")
            f = open("c://pythondata//fri1.txt","a")
            f.write(edit_name)
            print(f"{edit_name}이 추가되었습니다")
            f.close()
            
    
    else:
        break
