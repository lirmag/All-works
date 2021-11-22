def delete_nth(order,max_e):
    index = 0
    for elem in order:
        index += 1
        if (order.count(elem)) > max_e:
            for ind in range(len(order) - 1, index - 1, -1):
                a = order.count(elem)
                if elem == order[ind]:
                    a -= 1
                    del order[ind]
                if a == max_e:
                    break
    return order
print(delete_nth([4, 29, 4, 2, 29, 29, 2, 16, 16, 2, 16, 2, 16, 16, 16, 29, 29, 4, 2, 2, 2, 29, 16, 16, 16, 4, 48, 48, 4, 4, 16, 2, 2],5))