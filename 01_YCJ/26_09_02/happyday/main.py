# import gsc_1.g_1, gsc_1.g_2, gsc_1.g_3
import gsc_1

# gsc_1 -> 디렉토리? .py?       
# 디렉토리면 패키지 방식으로 처리
# 현재 디렉토리에 __init__.py 가 있음?
#   1) 있음 -> 일반 패키지로 처리 -> __init__.py 실행
#   2) 없음 -> name space 패키지로 처리

print(gsc_1.g_1.name)
print(gsc_1.g_2.name)
print(gsc_1.g_3.name)   # error