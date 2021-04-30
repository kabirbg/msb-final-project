###########################
###########################
######### SETUP ###########
###########################
###########################

from scipy.stats import wilcoxon,chi2_contingency
from statistics import multimode
from pandas import read_csv
students=read_csv("private/Students.csv")
families=read_csv("private/Family Members.csv")
from people import *
studs=[]
fams=[]
env_results=[]
gene_results=[]
numstudents=students.shape[0]
numfamilies=families.shape[0]
print(students)
print(families)
print("CSVs were successfully imported into the pandas dataframe; proceeding to creating objects for each individual.")


############################
############################
####### BASIC TESTS ########
############################
############################

# add a student/family object for each row in the dataframe
for row in range(numstudents):
    studs.append(student(row))
for row in range(numfamilies):
    fams.append(family(row))
print("Student/Family objects were successfully created; running statistical tests to check the integrity of each individual's data.")
# run tests to check integrity of each individual's data
for student in studs:
    student.selftest()
for family in fams:
    family.selftest()


#############################
#############################
###### WILCOXON TESTS #######
#############################
#############################

print("Running tests between each student and each family member/friend.")

# assign family members and friends
for index in range(len(studs)):
    stud=studs[index]
    fam1=fams[index]
    fam2=fams[index+numstudents-1]
    for row in range(len(studs)):
        if stud.friend1first==studs[row].first and stud.friend1last==studs[row].last:
            friend1=studs[row]
        if stud.friend2first==studs[row].first and stud.friend2last==studs[row].last:
            friend2=studs[row]

    # run tests between stud and each fam/friend
    for person in [fam1.selections, fam2.selections, friend1.selections, friend2.selections]:
        w,p = wilcoxon(stud.selections,person)
        print("The Wil-Coxon test statistic for {} {} is {}, for a p-value of {}.".format(stud.first,stud.last,w,p))
        if p<0.5:
            if p<0.1:
                if person is (fam1.selections or fam2.selections):
                    gene_results.append("highly statistically significant")
                else:
                    env_results.append("highly statistically significant")
            else:
                if person is (fam1.selections or fam2.selections):
                    gene_results.append("statistically significant")
                else:
                    env_results.append("statistically significant")
        else:
            if person is (fam1.selections or fam2.selections):
                gene_results.append("insignificant")
            else:
                env_results.append("insignificant")
        # that's it unless i want to do something with the statistic (W)

print("Here are the results of the Wilcoxon Tests for the family members:")
print(gene_results)
print("Here are the results of the Wilcoxon Tests for the friends:")
print(env_results)


############################
############################
##### CHI-SQUARE TESTS #####
############################
############################

# find the mode of the test results for each relationship
print("Here is the more common result of the tests for the family members:")
print(multimode(gene_results))
print("Here is the more common result of the tests for the friends:")
print(multimode(env_results))

# conduct chi-square test for association
chi2observed=[[gene_results.count("insignificant"),gene_results.count("statistically significant"),gene_results.count("highly statistically significant")],
        [env_results.count("insignificant"),env_results.count("statistically significant"),env_results.count("highly statistically significant")]]
print("Here are the observed frequencies of each type of result for family members and friends, respectively:")
print(chi2observed)
X2,p,df,ex=chi2_contingency(chi2observed)
print("Here are the expected frequencies of each type of result for family members and friends, respectively:")
print(ex)
print("The result of the Chi-Square Test for Association is test statistic X^2 = {}, which gives us a p-value of {} with {} degrees of freedom.".format(X2,p,df))

