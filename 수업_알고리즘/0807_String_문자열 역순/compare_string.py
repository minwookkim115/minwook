s1 = "abc"
s2 = "abc"
s5 = s1[:2] + "c"  # 통으로 짜르면 같은거로 보는데 / 짤라서 넣으면 새로운거로 봄

print(s1, s2, s5)

if s1 == s5:
    print("s1==s5")  # 출력 / s1과 s5는 내용이 같음 / 문자 그자체가 같음
else:
    print("s1!=5")

if s1 is s5:
    print("s1 is s5")
else:
    print("s1 is not s5")  # 출력 / s1과 s5는 다른곳을 가르키고 있음

if s1 == s2:
    print("s1==s2")  # 출력 / s1과 s2는 내용이 같음 / 문자 그자체가 같음
else:
    print("s1!=2")

if s1 is s2:
    print("s1 is s2")  # 출력 / s1과 s2는 같은곳을 가르키고 있음
else:
    print("s1 is not s2")
