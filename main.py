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
            if student.friends[1]==studs[row].name:
                friend1=studs[row]
        for row in range(len(fams)):
            if student.fam[0]==fams[row].name:
                fam0=fams[row]
            if student.fam[1]==fams[row].name:
                fam1=fams[row]
        if "fam0" in locals(): #fam0 exists
            # run tests between student and family member 0
            w,p = wilcoxon(student.ranks,fam0.ranks,zero_method="zsplit")
            print("The Wilcoxon test statistic between {} {} and {} {} (family member) is W={} (p={}).".format(student.name[1],student.name[0],fam0.name[1],fam0.name[0],w,p))
            if p<0.01:
                fam_results.append("highly statistically significant")
            elif p<0.05:
                fam_results.append("statistically significant")
            else:
                fam_results.append("insignificant")
        if "fam1" in locals(): #fam1 exists
            # run tests between student and family member 1
            w,p = wilcoxon(student.ranks,fam1.ranks,zero_method="zsplit")
            print("The Wilcoxon test statistic between {} {} and {} {} (family member) is W={} (p={}).".format(student.name[1],student.name[0],fam1.name[1],fam1.name[0],w,p))
            if p<0.01:
                fam_results.append("highly statistically significant")
            elif p<0.05:
                fam_results.append("statistically significant")
            else:
                fam_results.append("insignificant")
        if "friend0" in locals(): #friend0 exists
            #run tests between student and friend 0
            w,p = wilcoxon(student.ranks,friend0.ranks,zero_method="zsplit")
            print("The Wilcoxon test statistic between {} {} and {} {} (friend) is W={} (p={}).".format(student.name[1],student.name[0],friend0.name[1],friend0.name[0],w,p))
            if p<0.01:
                friend_results.append("highly statistically significant")
            elif p<0.05:
                friend_results.append("statistically significant")
            else:
                friend_results.append("insignificant")
        if "friend1" in locals(): #friend1 exists
            #run tests between student and friend 1
            w,p = wilcoxon(student.ranks,friend1.ranks,zero_method="zsplit")
            print("The Wilcoxon test statistic between {} {} and {} {} (friend) is W={} (p={}).".format(student.name[1],student.name[0],friend1.name[1],friend1.name[0],w,p))
            if p<0.01:
                friend_results.append("highly statistically significant")
            elif p<0.05:
                friend_results.append("statistically significant")
            else:
                friend_results.append("insignificant")

    return (fam_results, friend_results)

def chi2(group1, group2):
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

def srcc(students,families):
    famccs=[]
    friendccs=[]
    for genre in range(6):#
        studentranks=[]
        famranks=[]
        friendranks=[]
        for student in students:
            studentranks.append(student.ranks[genre])
            for row in range(len(studs)):
                if student.fam[0]==fams[row].name:
                    fam0=studs[row]
                if student.fam[1]==fams[row].name:
                    fam1=studs[row]
                if student.friends[0]==studs[row].name:
                    friend0=studs[row]
                if student.friends[1]==studs[row].name:
                    friend1=studs[row]
            fam=(fam0.ranks[genre]+fam1.ranks[genre])/2 #median not mean
            friend=(friend0.ranks[genre]+friend1.ranks[genre])/2 #median again
            famranks.append(fam)
            friendranks.append(friend)

        print("The student ranks for Genre #%i were: "%genre, end="")
        print(studentranks)
        print("The family ranks for Genre #%i were: "%genre, end="")
        print(famranks)
        print("The friend ranks for Genre #%i were: "%genre, end="")
        print(friendranks)

        r,p=spearmanr(studentranks,famranks)
        print("The correlation coefficient between students and family members for Genre #%i was %%2.5f (p=%2.5f)"%(genre,r,p))
        famccs.append(r,p)
        r,p=spearmanr(studentranks,friend)
        print("The correlation coefficient between students and friends for Genre #%i was %%2.5f (p=%2.5f)"%(genre,r,p))
        friendccs.append(r,p)

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

    print("Student/Family objects were successfully created; running Wilcoxon tests between each individual and their friends/family members.")
    genetic,environmental=wc(studs, fams); #run wilcoxon tests 
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
    srcc(studs,fams)

if __name__=="__main__":
    from scipy.stats import wilcoxon,chi2_contingency,spearmanr #needed for statistical testing
    from statistics import multimode #needed for descriptive statistics
    from people import * #needed dataframes & classes from ./people.py
    main()
