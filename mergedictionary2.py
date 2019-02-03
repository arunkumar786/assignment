#!/bin/python
def merge_dictionary(D1):
    D1 = D1
    inner_list_dict = []; append_list = []

    for i,j in D1.items():
        if type(j) == dict:
            inner_list_dict.append(j)

    for i,j in inner_list_dict[0].items():
        if type(j) == list:
            append_list = append_list + j

    return append_list

def final_merge(D1,D2):

    D1_list = merge_dictionary(D1)
    D2_list = merge_dictionary(D2)
    merged_list = D1_list + D2_list
    D1.update(D2)


    D1['b']['d'] = merged_list

    return D1

D1 = {'a':1,'b':{'c':3,'d':[4,5,6]}, 'f':7}
D2 = {'a':1,'c':9 ,'b':{'d':[8]}}

final_dict = final_merge(D1,D2)

print "Merged Dictionary is", final_dict
