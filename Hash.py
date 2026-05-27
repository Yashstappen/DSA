class HashTable:
    N = [5,3,2,2,1,7,2,5,3,4,6,8,9,1,2,3,4,5,6,7,8,9]
    M = [45,2,1,4,6,8,3,23,5,7,9,10,11,12,13,14,15,16,17,18,19,20]

    hash_table = {}
    for i in N:
        hash_table[i] = hash_table.get(i,0)+1
    for i in M:
        print(i,hash_table.get(i,0))