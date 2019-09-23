# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:47:34 2019

@author: jiang
"""
'''Q6: There are two arrays, Name and LateTime, which contain 
the name of students and their times late for school 
respectively. Sort the LateTime sequence and sort the Name 
sequence according to the sorted LateTime sequence and print 
out the students and their times late for school line by line
in order.
'''


Name=['a','b','c','d','e','f','g']   
LateTime=[3,1,2,3,1,2,3]


def bubble(n,score):
    swap=True
    while swap==True:
        swap=False
        for i in range(0,len(score)-1):
            if score[i]>score[i+1]:#1 point
                temp=score[i+1]#1 point
                tempn=n[i+1]#1 point
                score[i+1]=score[i]#1 point
                n[i+1]=n[i]#1 point
                score[i]=temp#1 point
                n[i]=tempn#1 point
                swap=True
    return n,score

Name,LateTime=bubble(Name,LateTime) #1 point
for i in range(len(Name)):
    print(Name[i]+' '+str(LateTime[i]))#1 point