#!/usr/bin/env python3

from pandas import read_csv #necessary for importing csv data as a pandas dataframe
students=read_csv("private/Students.csv") #initialize dataframe for students
families=read_csv("private/Family.csv") #and one for families

class student:#I'll have one object of this type for each participating student
    name=()#holds first and last name
    fam=[]#holds family members' names
    friends=[]#holds friends' names
    ranks=[-1,-1,-1,-1,-1,-1]#holds ordinal rankings for each genre

    def display(self):
        print(self.name)
        print(self.ranks)
        print(self.fam)
        print(self.friends)

    def __init__(self, row):
        #basic info
        self.name=(students.iat[row,0],students.iat[row,1]) #name (last,first) is a list
        self.fam=[(students.iat[row,15],students.iat[row,16]),(students.iat[row,17],students.iat[row,18])]#each family member occupies a list similar to above; fam contains both lists
        self.friends=[(students.iat[row,19],students.iat[row,20]),(students.iat[row,21],students.iat[row,22])]#same as above, for friends
        #generate & store rankings
        genres=students.iat[row,2]#temporarily store genre selections
        musics=[students.iat[row,3],students.iat[row,4],students.iat[row,5],students.iat[row,6],students.iat[row,7],students.iat[row,8],students.iat[row,9],students.iat[row,10],students.iat[row,11],students.iat[row,12],students.iat[row,13],students.iat[row,14]]#temporarily store song selections
        for genre in range(1,7): #each number represents a genre (1=pop, 2=jazz & blues, and so on)
            #assign rank system based on flowchart:
            if str(genre) in genres: #liked the genre
                if musics[genre*2-2]==1 and musics[genre*2-1]==1: #liked both musics
                    self.ranks[genre-1]=5
                elif musics[genre*2-2]==1 or musics[genre*2-1]==1: #liked one music
                    self.ranks[genre-1]=4
                else: #liked none
                    self.ranks[genre-1]=3
            else: #disliked the genre
                if musics[genre*2-2]==1 and musics[genre*2-1]==1: #liked both musics
                    self.ranks[genre-1]=2
                elif musics[genre*2-2]==1 or musics[genre*2-1]==1: #liked one music
                    self.ranks[genre-1]=1
                else: #liked none
                    self.ranks[genre-1]=0

class family:#I'll have one object of this type for each participating family member; identical to Student but lacks fam[] and friends[]
    name=[]
    ranks=[-1,-1,-1,-1,-1,-1]

    def display(self):
        print(self.name)
        print(self.ranks)

    def __init__(self, row):
        self.name=(families.iat[row,0],families.iat[row,1])
        genres=families.iat[row,2]
        musics=[families.iat[row,3],families.iat[row,4],families.iat[row,5],families.iat[row,6],families.iat[row,7],families.iat[row,8],families.iat[row,9],families.iat[row,10],families.iat[row,11],families.iat[row,12],families.iat[row,13],families.iat[row,14]]
        for genre in range(1,7):
            if str(genre) in genres:
                if musics[genre*2-2]==1 and musics[genre*2-1]==1:
                    self.ranks[genre-1]=5
                elif musics[genre*2-2]==1 or musics[genre*2-1]==1:
                    self.ranks[genre-1]=4
                else:
                    self.ranks[genre-1]=3
            else:
                if musics[genre*2-2]==1 and musics[genre*2-1]==1:
                    self.ranks[genre-1]=2
                elif musics[genre*2-2]==1 or musics[genre*2-1]==1:
                    self.ranks[genre-1]=1
                else:
                    self.ranks[genre-1]=0
