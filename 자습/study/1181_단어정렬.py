import sys

N = int(input())

str_l = [sys.stdin.readline().strip() for _ in range(N)]

sub_l = list(set(str_l))
sub_l.sort()
a_l = sorted(sub_l, key=lambda a: len(a))

print("\n".join(a_l))