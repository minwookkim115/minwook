numbers=[1, 2, 3]

# sort 메서드 => 객체.sort
print(numbers.sort()) # None => 복사본을 만들지 않았다.

numbers = [3, 2, 1]
# sorted 함수 => sorted()
print(sorted(numbers)) # [1, 2, 3] => 복사본을 만들어서 리턴
print(numbers) # [3, 2, 1] => 원본은 바뀌지 않았다.