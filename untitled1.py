#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:11:28 2017

@author: sarthakkapadiya
"""


from codeforces import CodeforcesAPI

def getHistory(handle):
    api = CodeforcesAPI()
    rating_changes = list(api.user_rating(handle))    
    print('Rating history for {}:'.format(handle))
    for rating in rating_changes:
        print(rating.old_rating, end=' -> ')    
    print(rating_changes[-1].new_rating)
    
def getRank(handle):
    api = CodeforcesAPI()
    handles=[handle]
    users = api.user_info(handles)
    print("\n")
    for u in users:
        print('{}, rank: {}'.format(u.handle, u.rank))

def getContestRanking(contest):
    api=Cod1eforcesAPI()
    list1=list(api.contest_standings(contest)['rows'])
    p1art=str(len(list1))
    for p in list1:
        tio=p.party.members[0].handle
        cc=api.user_rating(tio)
        print(str(tio) + " " + str(cc))
            
while(1):
    print("Choose from following optoins:\n")
    print("1. Know Your Rank.")
    print("2. Know Your History Rating.")
    print("3. Know The final Standing Of a Contest.")    
    print("0. Exit.")
    i=input("What do You want?")
    if(i=="0"):
        break
    elif(i=="1"):
        handle=input("Write your Handle:")
        getRank(handle)
    elif(i=="2"):
        handle=input("Write your Handle:")
        getHistory(handle)
    elif(i=="3"):
        contest=eval(input("Write Contest Name:"))
        getContestRanking(contest)
        
        
        
    