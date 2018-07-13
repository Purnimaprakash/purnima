for i in range(10):
    for j in range(3,i-1):
        if i%j==0: break
    else:
        print (i)

