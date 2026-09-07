import sys
from pathlib import Path

# 상위 폴더(test_package)를 파이썬 모듈 검색 경로(sys.path)에 추가 -> 후순위
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))
    
    
## 원래는 모듈 접근 우선순위 2번으로
#  (위의 1~7 line 제거)
"""
리눅스
export PYTHONPATH="/c/Users/USER/choigangho/temp/my_package/test_package"
python main.py

윈도우
$env:PYTHONPATH="C:/Users/USER/choigangho/temp/my_package/test_package"
python main.py
"""


## DM, GH 팀의 __init__.py에서 허용한 모듈만 가져오기
import DM.dm_module_2   # __init__.py 가 없으므로 명시적 import
import GH               # 명시적으로 안해도 알아서 import

# 모듈 내 함수 실행 예시
DM.dm_module_2.run()
GH.gh_module_2.run()