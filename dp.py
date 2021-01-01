def coinsChange(V,v):
    dpTable = [float('inf')]*(V+1)
    dpTable[0] = 0
    print('starting table:',dpTable)
    for i in range(1,V+1):
        for vi in v:
            if (i - vi) >= 0:
                dpTable[i] = min(dpTable[i],1+dpTable[i-vi])
        print('i:',i,'vi:',vi,dpTable)
    return dpTable[V]

print(coinsChange(11,[1,2,5]))
