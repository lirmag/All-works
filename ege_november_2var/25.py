for i in range(2000000,3000001):
   d = 1
   k = 0
   while d * d <= i:
       if i % d == 0:
           if i // d - d <= 115:
               k += 1
           if k == 3:
               print(i)
               break
       d += 1