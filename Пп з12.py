mfs = int(input())
hmn = int(input())
mmn = int(input())
hfalarm = mfs // 60
mfalarm = mfs % 60
alarmringh = hmn + hfalarm
alarmringm = mmn + mfalarm
if alarmringm >= 60:
    alarmringm -= 60
    alarmringh += 1
print(alarmringh)
print(alarmringm)
