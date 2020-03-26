# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:25:01 2020

@author: zeh0814
"""

 
def main(x, target):
    import functools
    import math
    #比较字符串中使用（'+','-','*','/'）的总个数，输出个数较少的
    def CompareLen(str1,str2):
        sum1,sum2 = 0,0
        for i in {'+','-','*','/'}:
            sum1 = sum1 + str1.count(i)
            sum2 = sum2 + str2.count(i)
        if sum1 < sum2:
            return str1
        else:
            return str2
        
    @functools.lru_cache(None)
    #递归+动态规划
    def dp(t):
        if t==0:
            return ''
        if t < x: #目标值小于除数
            str1 = (str(x) + '/' + str(x) + '+') * t
            str1 = str1[:-1]
            str2 = str(x) + ('-' + str(x) + '/' + str(x)) * (x-t)
            return CompareLen(str1,str2)
        
        lo = int(math.log(t,x))  
        po = pow(x, lo)  
        
        str3 = (str(x) + '*') * lo
        str3 = str3[:-1]
        if t == po: #target恰好是x的指数,直接输出
            return str3
        res = str3 + '+' + dp(t-po) #target不是x的指数，相差（target-po）或者（po*x-t）
        left = po * x - t
        if left < t: #只需讨论left < t，否者直接取res
            if '-' not in dp(left):
                str4 = str3 + '*' + str(x) + '-' + dp(left)
            else:
                s = dp(left)
                s = s.replace('-','+')
                str4 = str3 + '*' + str(x) + '-' + s
            res = CompareLen(res,str4) #比较使用符号的总数
        if res[-1] not in {'+','-','*','/'}:    
            return res
        else:
            return res[:-1]
    return dp(target)

x,target = map(int,input().split())
print(main(x,target))