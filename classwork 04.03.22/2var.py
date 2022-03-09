c = open('24-179.txt','r')
lines = c.readlines()
k = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ans = []
for line in lines:
    a = []
    for index in range(0,len(line)):
        count = 0
        if line[index] == 'A':
            count += 1
            string = line[index + 1:index + 27]
            for ind in range(0,len(string)):
                if (string[ind] == k[ind]) or (string[ind] == string[ind - 1]):
                    count += 1
                else:
                    a.append(count)
                    break
    ans.append(max(a))
print(max(ans))
