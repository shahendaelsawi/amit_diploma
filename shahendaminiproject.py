# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:01:31 2022

@author: Shahenda
"""
def add (*args):
    z=0
    for arg in args:
        z=z+arg
    return z

def sub(*values):
    m=0
    for value in values:
        m=value-m
    return m
def mult(*nums):
    n=1
    for num in nums:
        n=num*n
    return  n   
def div(*arqam):
    d=1
    for raqam in arqam:
        d=raqam/d
    return d