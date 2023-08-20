s1 = "abc"
s2 = "abd"
s3 = "ABC"
s4 = "abcd"
s5 = "abC"

print(s1 < s2)  # True
print(s1 > s2)  # False
print(s1 == s2)  # False

print(s1 < s3)  # False
print(s1 > s3)  # True

print(s1 < s4)  # True
print(s1 > s4)  # False

print(s1 < s5)  # False
print(s1 > s5)  # True

# 대문자가 소문자보다 작다(먼저)