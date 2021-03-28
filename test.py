from pandas import *

# general function to create a df from a csv and read it in two ways
def read_df(csv_filename,type):
    dataframe=read_csv(csv_filename)
    if type=="pandas" or type=="pd":
        print("Displayed as Pandas dataframe:")
        print(dataframe.to_string())
    elif type=="loop":
        print("Displayed with loops :)\n")
        for row in range(1,19):
            print("Student #%s:"%(row))
            for column in responses:
                print("%s: "%(column)+str(responses.at[row,column]))
            print("\n")

students=read_csv("Students.csv")
family=read_csv("Family Members.csv")

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

for x in range(0,students.shape[0]):
    student_x=student(x)
