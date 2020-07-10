# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 02:48:26 2020

@author: Necro
"""




def helper_atoi(str):
    def main_atoi(X):
        maxint=2147483647
        minint=-2147483648
    
        my_dict={'-':'-',
                 
                 '+':'+',
                 '0':'0',
                 '1':'1',
                 '2':'2',
                 '3':'3',
                 '4':'4',
                 '5':'5',
                 '6':'6',
                 '7':'7',
                 '8':'8',
                 '9':'9',
                 }
        Y=''
        for i in range(len(X)):
            if X[i]=='-' or X[i]=='+':
                if X[i] in my_dict:
                    my_dict.pop('-')
                    my_dict.pop('+')
                    if len(Y)==0:
                        Y+=(X[i])
                        continue
            
            if X[i] in my_dict:
                Y+=(my_dict[X[i]])
            else:
                break
    
        try:
            Ans_int=int(Y)
        except ValueError:   
            return 0
        if Ans_int>maxint:
            return(maxint)
        if Ans_int<minint:
            return(minint)
        return (Ans_int)
    

    L=str.lstrip(' ')
    return(main_atoi(L))
def main():
    test_dict={"    -88827   5655  U":-88827,
               "42":42,
               "   -42":-42,
               "4193 with words":4193,
               "words and 987":0,
               "-91283472332":-2147483648,
               }
    for k,v in test_dict.items():
        if helper_atoi(k)==v:
            print("Test for ","\"",k,"\""," passed!.")
        else:
            print("Test for ","\"",k,"\""," failed!.")
               
    
    
if __name__ == '__main__':

    main()
    
    
