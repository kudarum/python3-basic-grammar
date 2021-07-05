# 패키지
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모둘 내부에서만 사용
# __init__.py 라는 것은 Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성을 추천

# 예제1
import sys
from sub.sub1 import module1 as m1
from sub.sub2 import module2 as m2

# 사용
m1.mod1_test1()
m1.mod1_test2()
m2.mod2_test1()
m2.mod2_test2()

# 예제3

from sub.sub1 import *
