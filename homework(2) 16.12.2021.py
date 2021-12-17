length = int(input())
man = 0
mix = 0
count = 0
s_count = 0
ans = 0
s_ans = 0
for x in range(1,length + 1):
    count += 1
    s_count += 1
    num = input()
    if man == 0:
        man = int(num)
    if int(num) <= man:
        man = int(num)
        ans = count
    if int(num) > mix:
        mix = int(num)
        s_ans = s_count
print(ans,s_ans)