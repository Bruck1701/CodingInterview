from collections import Counter

def migratoryBirds(arr):
    hashmap = [(k,v) for k,v in sorted(Counter(arr).items(),reverse=True,key=lambda x:x[1])  ]

    min_value = hashmap[0][1]
    min_bird = hashmap[0][0]

    for el in hashmap:
        if el[1]==min_value and el[0]<min_bird:
            min_bird = el[0]
        
    return min_bird

print(migratoryBirds([1, 4, 4, 4, 5, 3]))