def find_sublist(lst):
    total_sum = sum(lst)
    half = total_sum//2
    taken = [False]*len(lst)
    curr_sum = lst[0]
    taken[0] = True
    idx = 0
    flag = False
    for i in range(1, len(lst)):
        if curr_sum < half:
            taken[i] = True
            curr_sum += lst[i]
            flag = True
        else:
            if not flag:
                taken[i] = True
                curr_sum += lst[i]
                flag = True
            continue
    list1 = list2 = []

    for k in range(len(lst)):
        if taken[k]:
            list1.append(lst[k])
        else:
            list2.append(lst[k])
    return list1, list2