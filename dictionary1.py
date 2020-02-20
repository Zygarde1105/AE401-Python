# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:49:38 2020

@author: Richard_Surface1
"""

print('##############################################')
print('############ welcome to skr system ###########')
print('##############################################')
print('##you will be English master if you use this##')
dic = {'apple':'蘋果','orange':'橘子'}

while True:
    print('1.add vocabulary')
    print('2.list all vocabulary')
    print('3.E to C')
    print('4.C to E')
    print('5.test score')
    print('6.out of the system')
    sol = input('what do you want to do:')
    
    if sol =='1':
        
        while True:
            print('type voc.  press 0 to out.')
            voc = input('type voc:')
            if voc == '0':
                break
            if voc not in dic:
                b = input('輸入意思(中文):')
                dic[voc] = b
            else:
                print('it is already in dictionary')
                
    elif sol =='2':
        dd = sorted(dic)
        for i in dd:
            print(i,'is',dic[i])
    elif sol =='3':
        c = input('type voc.  press 0 to quit.')
        if c =='0':
            break
        if c in dic:
            print(dic[c])
        else:
            print('it is not in dictionary')
    elif sol =='4':
        d = input('type meaning.  press 0 to quit.')
        if d == '0':
            break
        for k,v in dic.items():
            if v == d:
                print(v,'的英文是',k)
        else:
            print("sorry it didn't find it in dictionary")
    elif sol =='5':
        score = 0
        print('total is',len(dic),'points')
        for k,v in dic.items():
            ans = input(v+':')
            if ans == k:
                score += 1
                print('correct!',score,'points now')
            else:
                print('wrong!',score,'points now')
    elif sol =='6':
        break
    else:
        print('type again')