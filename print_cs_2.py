# -*- coding: utf-8 -*-
# Program Name: print_cs_2.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: Program to take user input of a character, then use that to create "CS" in ASCII PUNK

# Optional import for versions of python < 3
from __future__ import print_function

# Get user input
char = input("Input a character: ")

# Substring the first character of the string.
char = char[0:1]

print("*"*60)

print("              %s %s %s             %s %s %s        " %(char,char,char,char,char,char))
print("            %s                 %s       %s          " %(char,char,char))
print("           %s                  %s                  " %(char,char))
print("           %s                  %s                  " %(char,char))
print("           %s                    %s %s %s          " %(char,char,char,char))
print("           %s                          %s          " %(char,char))
print("            %s                 %s       %s         " %(char,char,char))
print("              %s %s %s             %s %s %s        " %(char,char,char,char,char,char))

print("*"*60)

"""
Input a character: #
************************************************************
              # # #             # # #        
            #                 #       #          
           #                  #                  
           #                  #                  
           #                    # # #          
           #                          #          
            #                 #       #         
              # # #             # # #        
************************************************************
"""
