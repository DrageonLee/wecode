def even_num() :
    nums = [i for i in range(1,51)]
    even_nums=[]
    for i in nums :
        if i%2 == 0:
            even_nums.append(i)
    return even_nums
            

print(even_num())