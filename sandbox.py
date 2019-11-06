#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:54:35 2019

@author: ujalashanker
"""

s = 'ctc'
n = len(s) - 1
h = 0
for c in s:
    h += ord(c) * (7**n)
    n -= 1
    
print (h)