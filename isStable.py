#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:38:57 2022

@author: RobbieParrish
Purpose: Test out a pseudocode of an algorithm for Analysis of Algorithms

Algorithm to test whether a configuration (produced in the style of 
the Gale Shapeley Stable Matching Problem) of Hospitals matched to Residents
is a stable matching. 

Returns "Yes" if the 

"""

H = [[2, 0, 1], #hosp 0 preferences
     [0, 2, 1], #hosp 1 preferences
     [1, 2, 0]] #hosp 2 preferences

R = [[1, 0, 2], #res 0 preferences
     [1, 2, 0], #res 1 preferences
     [2, 0, 1]] #res 2 preferences

M = [1, 0, 2]   # Hosp0's matched res, Hosp1's matching, hosp2's matching

def isStable(H, R, M):
    
    n = len(H)
    
    for hosp in range(n):
        matchedRes = (M[hosp])
        
        print("Check res" , matchedRes , "'s preferences to find out if they prefer any hospitals over hosp" , hosp)
        
        for rankingH in range(n):
            rankedHosp = R[matchedRes][rankingH]
            if ( rankedHosp != hosp):
                print(rankedHosp)
                print(hosp)
                print("rankedHosp != (hosp) " , (rankedHosp != (hosp)))
                rankedHospAssignedMatch = M[rankedHosp]
                print("res" , matchedRes , " prefers hosp" , rankedHosp , " over hosp", hosp , ", its assigned matching ")
                    
                print("Check hosp" , rankedHosp , "'s preferences to find out if they prefer res", matchedRes , "over their assignment ")
                
                for rankingR in range(n):
                    rankedRes = H[rankedHosp][rankingR]
                    if (rankedRes == matchedRes):
                        print("res", matchedRes , " and hosp" , rankedHosp , " prefer each other, so matching is unstable")
                        return "RESULT: No, the matching is not stable"
                    if(rankedRes == rankedHospAssignedMatch):
                        print("hosp", rankedHosp , " prefers its assignment, not an unstable pair")
                        break 
            else:
                print("res", matchedRes , " prefers its assignment, not an unstable pair")
                break
        
    return "RESULT: Yes, the matching is stable"


print(isStable(H, R, M))
        
