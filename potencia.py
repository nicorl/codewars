def dig_pow(n, p):
    # descomponer n y guardar numeros por separado en array
    nums = str(n)
    arrnums, arrpots = [], [] 
    for num in nums:
        arrnums.append(num)
    for x in range(0,len(arrnums)):
        arrpots.append(int(arrnums[x]) ** int((p+x)))
    sumpots = int(sum(arrpots))

    multi = int(nums)
    print(sumpots)
    print(multi)
    for k in range(1,10000000):
        if (sumpots == multi * k):
            return k
    return -1
    

print(dig_pow(46288,3))