# 깊은 복사
import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999

print(original_list, deep_copied_list)
# [1, 2, [1, 2]] [1, 2, [999, 2]]
# deep_copied_list가 영향을 주지 않음
# 리스트 안에 리스트도 완벽하게 복사