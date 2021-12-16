length = int(input())
minimum = 0
maximum = 0
count = 0
s_count = 0
ans = 0
s_ans = 0
for x in range(1,length + 1):
    count += 1
    s_count += 1
    num = input()
    if minimum == 0:
        minimum = int(num)
    if int(num) <= minimum:
        minimum = int(num)
        ans = count
    if int(num) > maximum:
        maximum = int(num)
        s_ans = s_count
print(ans,s_ans)