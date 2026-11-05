'''while True:
    try:
        age = int(input("나이를 입력하시오:"))
     
    except ValueError:
        print("값을 다시 입력하세여")
        
'''
def safe_get_element(lst, index):
    try:
        result = lst[index]
    except TypeError:
        print("인덱스는 정수")
    except IndexError:
        print("인덱스 밖임")
    except 
