from pandas import *
students=read_csv("Students.csv")
families=read_csv("Family Members.csv")

class student:
    last=""
    first=""
    genres=""
    m1=0
    m2=0
    m3=0
    m4=0
    m5=0
    m6=0
    m7=0
    m8=0
    m9=0
    m10=0
    m11=0
    m12=0
    fam1last=""
    fam1first=""
    fam2last=""
    fam2first=""
    friend1last=""
    friend2last=""
    friend2first=""

    def __init__(self, row):
        self.last=students.iat[row,0]
        self.first=students.iat[row,1]
        self.genres=students.iat[row,2]
        self.m1=students.iat[row,3]
        self.m2=students.iat[row,4]
        self.m3=students.iat[row,5]
        self.m4=students.iat[row,6]
        self.m5=students.iat[row,7]
        self.m6=students.iat[row,8]
        self.m7=students.iat[row,9]
        self.m8=students.iat[row,10]
        self.m9=students.iat[row,11]
        self.m10=students.iat[row,12]
        self.m11=students.iat[row,13]
        self.m12=students.iat[row,14]
        self.fam1last=students.iat[row,15]
        self.fam1first=students.iat[row,16]
        self.fam2last=students.iat[row,17]
        self.fam2first=students.iat[row,18]
        self.friend1last=students.iat[row,19]
        self.friend1first=students.iat[row,20]
        self.friend2last=students.iat[row,21]
        self.friend2first=students.iat[row,22]

    def display(self):
        print(self.last,end=", ")
        print(self.first,end="\t")
        print(self.genres)
        print(self.m1,end=", ")
        print(self.m2,end=", ")
        print(self.m3,end=", ")
        print(self.m4,end=", ")
        print(self.m5,end=", ")
        print(self.m6,end=", ")
        print(self.m7,end=", ")
        print(self.m8,end=", ")
        print(self.m9,end=", ")
        print(self.m10,end=", ")
        print(self.m11,end=", ")
        print(self.m12)
        print(self.fam1last,end=", ")
        print(self.fam1first,end="\t")
        print(self.fam2last,end=",")       
        print(self.fam2first,end="\t")
        print(self.friend1last,end=",")  
        print(self.friend1first,end="\t")
        print(self.friend2last,end=", ")
        print(self.friend2first)
        print("\n")


class family:
    last=""
    first=""
    genres=""
    m1=0
    m2=0
    m3=0
    m4=0
    m5=0
    m6=0
    m7=0
    m8=0
    m9=0
    m10=0
    m11=0
    m12=0

    def __init__(self, row):
        print(families.iat[row,0])
        self.last=families.iat[row,0]
        self.first=families.iat[row,1]
        self.genres=families.iat[row,2]
        self.m1=families.iat[row,3]
        self.m2=families.iat[row,4]
        self.m3=families.iat[row,5]
        self.m4=families.iat[row,6]
        self.m5=families.iat[row,7]
        self.m6=families.iat[row,8]
        self.m7=families.iat[row,9]
        self.m8=families.iat[row,10]
        self.m9=families.iat[row,11]
        self.m10=families.iat[row,12]
        self.m11=families.iat[row,13]
        self.m12=families.iat[row,14]

    def display(self):
        print(self.last,end=", ")
        print(self.first,end="\t")
        print(self.genres)
        print(self.m1,end=", ")
        print(self.m2,end=", ")
        print(self.m3,end=", ")
        print(self.m4,end=", ")
        print(self.m5,end=", ")
        print(self.m6,end=", ")
        print(self.m7,end=", ")
        print(self.m8,end=", ")
        print(self.m9,end=", ")
        print(self.m10,end=", ")
        print(self.m11,end=", ")
        print(self.m12)
        print("\n")
