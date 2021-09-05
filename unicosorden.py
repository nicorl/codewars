iterable = 'AAABBBCCCaabacbacbacb'

def unique_in_order(iterable):
    sol = []
    if len(iterable) == 0:
        return sol
    if len(iterable) == 1:
        sol.append(iterable)
        return sol
    if len(iterable) > 1:
        sol.append(iterable[0])
        for x in range(0,len(iterable)):
            if iterable[x] == sol[len(sol)-1]:
                #sol.append(iterable[x])
                pass
            else:
                sol.append(iterable[x])
        return sol

print(unique_in_order(iterable))