num1, num2 = [int(x) for x in input().split(' ')]
while num2 and num1 > 0:
    lst = [x for x in range(num1, num2+1)] if num2 > num1 else [x for x in range(num2, num1 +1)]
    asw = ' '.join(str(x) for x in lst)
    asw+= ' Sum={}'.format(sum(lst))
    print(asw)
    num1, num2 = [int(x) for x in input().split(' ')]
    
