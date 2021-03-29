# import something statistical, or change the following func to make it meaningful:
def stattest(list1, list2):
    intersect=set(list1).intersection(list2)

from pandas import *
students=read_csv("Students.csv")
families=read_csv("Family Members.csv")
from people import *
studs=[]
fams=[]
env_results=[]
gene_results=[]

print("CSVs were successfully imported into the pandas dataframe; proceeding to creating objects for each individual.")

# add a student/family object for each row in the dataframe
for row in range(students.shape[0]):
    studs.append(student(row))
for row in range(families.shape[0]):
    fams.append(family(row))

print("Student/Family objects were successfully created; running statistical tests to check the integrity of each individual's data.")

# run tests to check integrity of each individual's data
for student in studs:
    student.selftest()
    student.display()
for family in fams:
    family.selftest()
    family.display()

print("Running tests between each student and each family member/friend.")

# assign family members and friends
for index in range(len(studs)):
    stud=studs[index]
    fam1=fams[index]
    fam2=fams[index+19]
    for row in range(len(studs)):
        if stud.friend1first==studs[row].first and stud.friend1last==studs[row].last:
            friend1=studs[row]
        if stud.friend2first==studs[row].first and stud.friend2last==studs[row].last:
            friend2=studs[row]

    # run tests between stud and each fam/friend
    gene_results.append(stattest(stud.selections,fam1.selections))
    gene_results.append(stattest(stud.selections,fam2.selections))
    env_results.append(stattest(stud.selections,friend1.selections))
    env_results.append(stattest(stud.selections,friend2.selections))

print("Here are the results of the statistical tests for the family members:")
print(gene_results)
print("Here are the results of the statistical tests for the friends:")
print(env_results)

# find the mode of the test results for each relationship
from statistics import multimode
print("Here is the more common result of the statistical tests for the family members:")
print(multimode(gene_results))
print("Here is the more common result of the statistical tests for the friends:")
print(multimode(env_results))
