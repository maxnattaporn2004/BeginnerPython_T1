num = int(input())
base = 1
space = " "
if 3 <= num <= 99:
    for i in range(num):
        i+=1
        if num //1.5 == i:
            print(space*(num-i)+"#"*(base-i)+"♦"+"#"*(base-i))
        else:
            print(space*(num-i)+"#"*base)
        base +=2

