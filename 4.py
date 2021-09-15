for i in range(10, 100):
    numdoz = i // 10
    numunit = i % 10
    answer = (numdoz * numunit) * 2
    if answer == i:
        print(i)
