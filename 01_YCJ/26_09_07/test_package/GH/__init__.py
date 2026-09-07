# 명시적으로 외부에 노출할 모듈 지정
from . import gh_module_2


# 외부에서 'from GH import *' 사용 시 gh_module_2만 노출되도록 제한
__all__ = ['gh_module_2']