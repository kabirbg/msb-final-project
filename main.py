#!/usr/bin/env python3

def wc(studs, fams):
    #initialize arrays to hold the results of the WC tests
    fam_results=[]
    friend_results=[]

    print("Running tests between each student and each family member/friend.")
    for index in range(len(studs)):
        # assign family members and friends
        student=studs[index]
        for row in range(len(studs)):
            if student.friends[0]==studs[row].name:
                friend0=studs[row]
            if student.friends[1]==studs[row].first and student.friend2last==studs[row].last:
                friend1=studs[row]
            if student.fam[0]==fams[row].name:
                fam0=studs[row]
            if student.fam[1]==fams[row].first and student.friend2last==studs[row].last:
                fam1=studs[row]

        # run tests between student and each family member
        for person in (fam1, fam2):
            w,p = wilcoxon(student.ranks,person.ranks)
            print("The Wilcoxon test statistic between {} {} and {} {} (family member) is W={} (p={}).".format(student.name[1],student.name[0],person.name[1],person.name[0],w,p))
            if p<0.1:
                fam_results.append("highly statistically significant")
            elif p<0.5:
                fam_results.append("statistically significant")
            else:
                fam_results.append("insignificant")
        #run tests between student and each friend
        for person in (friend1, friend2):
            w,p = wilcoxon(student.ranks,person.ranks)
            print("The Wilcoxon test statistic between {} {} and {} {} (friend) is W={} (p={}).".format(student.name[1],student.name[0],person.name[1],person.name[0],w,p))
            if p<0.1:
                friend_results.append("highly statistically significant")
            elif p<0.5:
                friend_results.append("statistically significant")
            else:
                friend_results.append("insignificant")

    return (fam_results, friend_results)

def chi2(group1, group1):
    # conduct chi-square test for association
    chi2observed=[[group1.count("insignificant"),group1.count("statistically significant"),group1.count("highly statistically significant")],
            [group2.count("insignificant"),group2.count("statistically significant"),group2.count("highly statistically significant")]]
    print("Here are the observed frequencies of each type of result for family members and friends, respectively:")
    print(chi2observed)
    X2,p,df,ex=chi2_contingency(chi2observed)
    print("Here are the expected frequencies of each type of result for family members and friends, respectively:")
    print(ex)
    print("The result of the Chi-Square Test for Association is test statistic X^2 = {} with {} degrees of freedom, which gives us a p-value of {}.".format(X2,df,p))
    return p

def correlation_regression(students,families):
    #TODO: WORK ON THIS!

def main():
    #create lists to hold student and family objects:
    studs=[]
    fams=[]
    print(students)
    print(families)
    print("CSVs were successfully imported into the pandas dataframe; proceeding to creating objects for each individual.")

    # add a student/family object for each row in the dataframe
    for row in range(students.shape[0]):
        studs.append(student(row)) #create students
    for row in range(families.shape[0]):
        fams.append(family(row)) #create family

    print("Student/Family objects were successfully created; running statistical tests to check the integrity of each individual's data.")
    genetic,environmental=wc(studs, fams); #run basic tests 
    print("Here are the results of the Wilcoxon Tests for the family members:")
    print(genetic)
    print("Here are the results of the Wilcoxon Tests for the friends:")
    print(environmental)
    print("Here is the most common result of the tests for the family members:")
    print(multimode(genetic))
    print("Here is the most common result of the tests for the friends:")
    print(multimode(environmental))

    chi2(genetic, environmental)
    if p>0.5:
        print("WARNING: There is not a statistically significant association between relationship type and similarity of music choice. Following results may be very unreliable.")
    correlation_regression(studs,fams)

if __name__=="__main__":
    from scipy.stats import wilcoxon,chi2_contingency #needed for statistical testing
    from statistics import multimode #needed for descriptive statistics
    from people import * #needed dataframes & classes from ./people.py   
    main()
