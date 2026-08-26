def add(a, b):
    return a + b

# print(f"테스트: {add(2, 3)}")
    
# module은 통상적으로 "정의" 역할만 수행해야 함
# print(f"테스트: {add(2, 3)}")     # 해당 코드가 14 라인에 없고, 7번 라인에 있었다고 가정 후
# __name__ == '__main__': 유무를 비교하여 이해

# 현재 작업 공간(__name__)이 main(HEAD, main.py가 아님!!!)이면 현재 스크립트의 실행 기능만 실행한다.

if __name__ == '__main__':   # 실행(run) 공간이 현재 작업 공간이면 아래 실행
    print(f"테스트: {add(2, 3)}")