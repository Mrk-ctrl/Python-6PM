li = [56, 56, 65, 56, 56, 324, 67, 6, 23, 6, 87, 3, 78, 4, 2]
repeat = 0
flag = False
dup_list = []

# With Function
for i in li:
    if i not in dup_list:
        repeat = li.count(i)
    else:
        continue

    if repeat > 1:
        print(f"{i} was repeated {repeat} times")
        dup_list.append(i)

# Without Function
for i in range(0, len(li)): 
    for j in range(0, len(li)): 
        if li[i] not in dup_list:
            if li[i] == li[j]:
                count += 1 
        else:
            break
            

    if count > 1:
        print(f"{li[i]} was repeated {count} times")
        dup_list.append(li[i])
        flag = True

    count = 0

if not flag:
    print("No elements were repated")