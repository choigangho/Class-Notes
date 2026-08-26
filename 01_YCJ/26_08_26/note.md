*/ step 1 가상환경 */
1. pip 업데이트                       -> python -m pip install --upgrade pip
   가상환경 내부의 pip를 따로 업데이트 -> .venv\Scripts\python -m pip install --upgrade pip
2. 가상환경 생성                      -> python -m venv .venv 
3. 프로젝트에서 사용할 Python 인터프리터를 .venv의 Python으로 선택
   -> Ctrl + Shift + p -> 파이썬 인터프린터 선택 -> 인터프린터 작업경로로 

*/ step 2 main.py */
1. 파일만 생성

*/ step 3 import_path.py */
1. 인터프린터 모듈 접근 순서, 환경변수 이름 변경 실습

*/ step 4 calc.py & main.py */
1. calc.py과 main.py으로 __name__ == '__main__' 이해

*/ step 5 강의자료 lab 실습 후 이해 */