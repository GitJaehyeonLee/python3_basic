# Python 의 변수 선언

# 자료형을 가리지 않는다.
# 다른언어
# int num = 1
# var name = "Mike"

num = 1
name = "Mike"
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 자료형 변환도 자유롭게 진행된다.
num = name
print(num, type(num))

chr_num = '1'
num = int(chr_num)
print(chr_num, type(chr_num))
print(num, type(num))

# Python 3.6 부터 형 선언시 타입 참고 정보를 줄수 있다. : 실제로는 강제 형을 가지지 않기 때문에 의미 없다...
num: int = 1
name: str = '1'
test: int = "1234"

print(num, type(num))
print(name, type(name))
print(test, type(test))
