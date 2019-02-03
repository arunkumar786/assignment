#!/bin/python
def merge_dictionary(D1,D2):
    D1 = D1 

    D2 = D2

    for i,j in D1.items():
        for k,l in D2.items():
            if type(j) == list and type(l) == list:
                m = j + l
                n = {}
                n[k] = m


    D1.update(D2)


    D1['e'] = n['e']

    return D1

D1 = {'a':1,'b':2, 'd':4, 'e':[5,6,8]}
D2 = {'c':3,'d':11,'e':[9,10]}

final_dict = merge_dictionary(D1,D2)

print "Merged Dictionary is", final_dict
