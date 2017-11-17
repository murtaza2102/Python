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
def get_all_user_handles(ranklist_rows):
    return set(m.handle for row in ranklist_rows for m in row.party.members)


def filter_by_organization(ranklist_row, handle_to_user_mapping, organization):
    return (r for r in ranklist_row if handle_to_user_mapping[r.party.members[0].handle].organization == organization)


def filter_by_country(ranklist_row, handle_to_user_mapping, country):
    return (r for r in ranklist_row if handle_to_user_mapping[r.party.members[0].handle].country == country)


def main():
    api = CodeforcesAPI()

    ranklist = api.contest_standings(613, count=10000)
    ranklist_rows = list(ranklist['rows'])

    users = {u.handle: u for u in api.user_info(list(get_all_user_handles(ranklist_rows)))}

    print("Users from Ural FU:")
    for row in filter_by_organization(ranklist_rows, users, "Ural FU"):
        print('    {party}, points: {points}'.format(party=row.party, points=row.points))

    print()

    print("Users from Mexico:")
    for row in filter_by_country(ranklist_rows, users, "Mexico"):
        print('    {party}, points: {points}'.format(party=row.party, points=row.points))

while(1):
    print("Choose from following optoins:\n")
    print("1. Know Your Rank.")
    print("2. Know Your History Rating.")
    print("3. Know The final Standing Of a Contest.") 
	print("4. Know The users from an Organization.") 	
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
        getContestRanking(contest
	else 
		get_all_user_handles()
        
        
        
    