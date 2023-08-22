# -*- coding: utf-8 -*-
def max_min(a,b,c,d):
    
    if d>0:
        mx=a
        if mx<b:
            mx=b
        
        if mx<c:
            mx=c
        return mx
    if d<=0:
        mn=a
        if mn>b:
            mn=b
        
        if mn>c:
            mn=c   
        return mn
