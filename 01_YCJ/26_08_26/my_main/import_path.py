import sys  # sys: 인터프리터 환경 정보

for path in sys.path:
    print(path)

# 인터프린터 모듈 접근 순서

# c:\Temp\my_main                                                      (1) 작업 영역

# C:\Users\USER\choigangho\my_company                                  (2) 회사 모듈 (윈도우 환경변수 PYTHONPATH)
# 회사 패키지 이름을 my_company -> gsc_lib 으로 변경 
# Windows 환경변수 -> PYTHONPATH 편집 -> 변수 값 C:\Temp\gsc_lib (변수이름은 그대로, PYTHONPATH)

# C:\Users\USER\AppData\Local\Python\pythoncore-3.14-64\python314.zip  (3) Built-in
# C:\Users\USER\AppData\Local\Python\pythoncore-3.14-64\DLLs
# C:\Users\USER\AppData\Local\Python\pythoncore-3.14-64\Lib
# C:\Users\USER\AppData\Local\Python\pythoncore-3.14-64

# C:\Temp\my_main\.venv                                                (?)

# C:\Temp\my_main\.venv\Lib\site-packages                              (4) pip 