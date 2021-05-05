#!/usr/bin/env python3

from pandas import read_csv #necessary for importing csv data as a pandas dataframe
students=read_csv("private/Students.csv") #initialize dataframe for students
families=read_csv("private/Family Members.csv") #and one for families

class student:#I'll have one object of this type for each participating student
    name=[]#holds first and last name
    fam=[]#holds family members' names
    friends=[]#holds friends' names
    rank=[]#holds ordinal rankings for each genre

    def display(self):
        print("Name: "+self.name)
        print("Ranks: "+self.rank)
        print("Family: "+self.fam)
        print("Friends: "+self.friends)
        print("\n")

    def __init__(self, row):
        #basic info
        self.name=[students.iat[row,0],students.iat[row,1]] #name (last,first) is a list
        self.fam=[(students.iat[row,15],students.iat[row,15]),(students.iat[row,17],students.iat[row,18])]#each family member occupies a list similar to above; fam contains both lists
        self.friends=[(students.iat[row,19],students.iat[row,20]),(students.iat[row,21],students.iat[row,22])]#same as above, for friends
        #generate & store rankings
        genres=students.iat[row,2]#temporarily store genre selections
        musics=[students.iat[row,3],students.iat[row,4],students.iat[row,5],students.iat[row,6],students.iat[row,7],students.iat[row,8],students.iat[row,9],students.iat[row,10],students.iat[row,11],students.iat[row,12],students.iat[row,13],students.iat[row,14]]#temporarily store song selections
        for genre in range(1,7): #each number represents a genre (1=pop, 2=jazz & blues, and so on)
            #assign rank system based on flowchart:
            if genre in self.genres:
                if musics[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank[genre-1]=5
                elif musics[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank[genre-1]=4
                else:
                    self.rank[genre-1]=3
            else:
                if musics[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank[genre-1]=2
                elif musics[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank[genre-1]=1
                else:
                    self.rank[genre-1]=0
        self.display()#display info to ensure operation completed successfully

class family:#I'll have one object of this type for each participating family member; identical to Student but lacks fam[] and friends[]
    name=[]
    rank=[]

    def display(self):
        print("Name: "+self.name)
        print("Ranks: "+self.rank)
        print("\n")

    def __init__(self, row):
        self.name=[students.iat[row,0],students.iat[row,1]]
        genres=students.iat[row,2]
        musics=[students.iat[row,3],students.iat[row,4],students.iat[row,5],students.iat[row,6],students.iat[row,7],students.iat[row,8],students.iat[row,9],students.iat[row,10],students.iat[row,11],students.iat[row,12],students.iat[row,13],students.iat[row,14]]
        for genre in range(1,7):
            if genre in self.genres:
                if musics[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank[genre-1]=5
                elif musics[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank[genre-1]=4
                else:
                    self.rank[genre-1]=3
            else:
                if musics[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank[genre-1]=2
                elif musics[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank[genre-1]=1
                else:
                    self.rank[genre-1]=0
        self.display()
