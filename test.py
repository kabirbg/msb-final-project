from pandas import *

# general function to create a df from a csv and read it in two ways
def read_df(csv_filename,type):
    dataframe=read_csv(csv_filename)
    if type=="pandas" or type=="pd":
        print("Displayed as Pandas dataframe:")
        print(dataframe)
    elif type=="loop":
        print("Displayed with loops :)\n")
        for row in range(1,19):
            print("Student #%s:"%(row))
            for column in responses:
                print("%s: "%(column)+str(responses.at[row,column]))
            print("\n")

students=read_csv("Students.csv")
family=read_csv("Family Members.csv")
