from pandas import read_csv
students=read_csv("private/Students.csv")
families=read_csv("private/Family Members.csv")

class student:
    name=[]
    genres=""
    m=[]
    fam=[]
    friends=[]
    rank=-1

    def rank(self):
        for genre in range(1,7): #each number represents a genre (1=pop, 2=jazz & blues, and so on)
            if genre in self.genres:
                if self.m[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank=5
                elif self.m[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank=4
                else:
                    self.rank=3
            else:
                if self.m[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank=2
                elif self.m[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank=1
                else:
                    self.rank=0

    def __init__(self, row):
        self.name=[students.iat[row,0],students.iat[row,1]]
        self.genres=students.iat[row,2]
        self.m=[students.iat[row,3],students.iat[row,4],students.iat[row,5],students.iat[row,6],students.iat[row,7],students.iat[row,8],students.iat[row,9],students.iat[row,10],students.iat[row,11],students.iat[row,12],students.iat[row,13],students.iat[row,14]]
        self.fam=[(students.iat[row,15],students.iat[row,15]),(students.iat[row,17],students.iat[row,18])]
        self.friends=[(students.iat[row,19],students.iat[row,20]),(students.iat[row,21],students.iat[row,22])]
        self.rank()

    def display(self):
        print(self.name)
        if self.rank==-1:
            print(self.genres)
            print(self.m)
        else:
            print("Rank: " + self.rank)
        print(self.fam)
        print(self.friends)
        print("\n")

class family:
    name=[]
    genres=""
    m=[]
    rank=-1

    def rank(self):
        for genre in range(1,7): #each number represents a genre (1=pop, 2=jazz & blues, and so on)
            if genre in self.genres:
                if self.m[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank=5
                elif self.m[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank=4
                else:
                    self.rank=3
            else:
                if self.m[genre*2-1]==1 and self.m[genre*2]==1:
                    self.rank=2
                elif self.m[genre*2-1]==1 or self.m[genre*2]==1:
                    self.rank=1
                else:
                    self.rank=0

    def __init__(self, row):
        self.name=[students.iat[row,0],students.iat[row,1]]
        self.genres=students.iat[row,2]
        self.m=[students.iat[row,3],students.iat[row,4],students.iat[row,5],students.iat[row,6],students.iat[row,7],students.iat[row,8],students.iat[row,9],students.iat[row,10],students.iat[row,11],students.iat[row,12],students.iat[row,13],students.iat[row,14]]
        self.rank()

    def display(self):
        print(self.name)
        if self.rank==-1:
            print(self.genres)
            print(self.m)
        else:
            print("Rank: " + self.rank)
        print("\n")
