from pandas import *
students=read_csv("Students.csv")
families=read_csv("Family Members.csv")

from people import *


# MAKE THIS WORK
"""
for x in range(students.shape[0]):
    student_x=student(x)
"""

student0=student(0)
family0=family(0)

student0.display()
family0.display()









# general function to create a df from a csv and read it in two ways
def read_df(csv_filename,type):
    dataframe=read_csv(csv_filename)
    if type=="pandas" or type=="pd":
        print("Displayed as Pandas dataframe:")
        print(dataframe.to_string())
    elif type=="loop":
        print("Displayed with loops :)\n")
        for row in range(19):
            print("Student #%s:"%(row))
            for column in responses:
                print("%s: "%(column)+str(responses.at[row,column]))
            print("\n")

