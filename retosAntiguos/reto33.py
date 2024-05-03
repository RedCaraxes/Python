"""
/*
 * Dado un listado de números, encuentra el SEGUNDO más grande
 */
"""

def second_matrix(list1):
    for i in range (len(list1)-1):
        for j in range (len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1]=list1[j+1], list1[j]
    return list1[1]
    
n=second_matrix([2, 4, 1, 8, 0])
print(n)
m=second_matrix([3, 4, 1, 8, 11])
print(m)