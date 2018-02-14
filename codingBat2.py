#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: codingBat2.py
# Anthony Waldsmith
# 07/24/2016
# Python Version 3.4
# Description: Extra Credit

# Optional import for versions of python <= 2
from __future__ import print_function

def cigar_party(cigars, is_weekend):
  if cigars < 40:
    return False
  
  if not is_weekend:
    if cigars > 60:
      return False
      
  return True

def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count

def has22(nums):
  first = False
  second = False
  for i in nums:
    if i == 2:
      if first == True:
        second = True
      else:
        first = True
      if first == True and second == True:
          return True
    else:
      first = False
      second = False
  return False

def sum67(nums):
  ignoring = False
  sum = 0
  for i in nums:
    if i == 6:
      ignoring = True
    
    if ignoring == False:
      sum += i
      
    if i == 7:
      ignoring = False
  return sum
