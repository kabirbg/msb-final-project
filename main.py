#!/usr/bin/env python3

def findmatches(student,studs,fams):
    # assign family members and friends for a given student
    fam0='' #an empty string by default
    fam1=''
    friend0=''
    friend1=''
    for friend in studs:
        if student.friends[0]==friend.name:
            friend0=friend
        if student.friends[1]==friend.name:
            friend1=friend
    for family in fams:
        if student.fam[0]==family.name:
            fam0=family
        if student.fam[1]==family.name:
            fam1=family
    return (fam0,fam1,friend0,friend1)

def wc(studs, fams):
    #initialize arrays to hold the results of the WC tests
    fam_results=[]
    friend_results=[]

    print("Running tests between each student and each family member/friend.")
    for index in range(len(studs)):
        student=studs[index]
        fam0,fam1,friend0,friend1=findmatches(student,studs,fams)

        if fam0!='': #fam0 exists
            # run tests between student and family member 0
            print(student.ranks)
            print(fam0.ranks)
            if student.ranks==fam0.ranks:
                print("{} {} and {} {} (family member) have the same rankings. The result is hence insignificant.".format(student.name[1],student.name[0],fam0.name[1],fam0.name[0]))
                fam_results.append("insignificant")
            else:
                w,p = wilcoxon(student.ranks,fam0.ranks)
                print("The Wilcoxon test statistic between {} {} and {} {} (family member) is W={} (p={}).".format(student.name[1],student.name[0],fam0.name[1],fam0.name[0],w,p))
                if p<0.05:
                    fam_results.append("statistically significant")
                elif p<0.1:
                    fam_results.append("significant @ 10%")
                else:
                    fam_results.append(p)#"insignificant")
        if fam1!='': #fam1 exists
            # run tests between student and family member 1
            print(student.ranks)
            print(fam1.ranks)
            if student.ranks==fam1.ranks:
                print("{} {} and {} {} (family member) have the same rankings. The result is hence insignificant.".format(student.name[1],student.name[0],fam1.name[1],fam1.name[0]))
                fam_results.append("insignificant")
            else:
                w,p = wilcoxon(student.ranks,fam1.ranks)
                print("The Wilcoxon test statistic between {} {} and {} {} (family member) is W={} (p={}).".format(student.name[1],student.name[0],fam1.name[1],fam1.name[0],w,p))
                if p<0.05:
                    fam_results.append("statistically significant")
                elif p<0.10:
                    fam_results.append("significant @ 10%")
                else:
                    fam_results.append(p)#"insignificant")
        if friend0!='': #friend0 exists
            #run tests between student and friend 0
            print(student.ranks)
            print(friend0.ranks)
            if student.ranks==friend0.ranks:
                print("{} {} and {} {} (friend) have the same rankings. The result is hence insignificant.".format(student.name[1],student.name[0],friend0.name[1],friend0.name[0]))
                friend_results.append("insignificant")
            else:
                w,p = wilcoxon(student.ranks,friend0.ranks)
                print("The Wilcoxon test statistic between {} {} and {} {} (friend) is W={} (p={}).".format(student.name[1],student.name[0],friend0.name[1],friend0.name[0],w,p))
                if p<0.05:
                    friend_results.append("statistically significant")
                elif p<0.10:
                    friend_results.append("significant @ 10%")            
                else:
                    friend_results.append(p)#"insignificant")
        if friend1!='': #friend1 exists
            #run tests between student and friend 1
            print(student.ranks)
            print(friend1.ranks)
            if student.ranks==friend1.ranks:
                print("{} {} and {} {} (friend) have the same rankings. The result is hence insignificant.".format(student.name[1],student.name[0],friend1.name[1],friend1.name[0]))
                friend_results.append("insignificant")
            else:
                w,p = wilcoxon(student.ranks,friend1.ranks)
                print("The Wilcoxon test statistic between {} {} and {} {} (friend) is W={} (p={}).".format(student.name[1],student.name[0],friend1.name[1],friend1.name[0],w,p))
                if p<0.05:
                    friend_results.append("statistically significant")
                elif p<0.10:
                    friend_results.append("significant @ 10%")
                else:
                    friend_results.append(p)#"insignificant")

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
            fam0,fam1,friend0,friend1=findmatches()
            studentranks.append(student.ranks[genre])
            if fam0!='' and fam1!='': #both of them were found
                fam=(fam0.ranks[genre]+fam1.ranks[genre])/2 #median not mean
                famranks.append(fam)
            elif fam0!='': #only fam0 was found
                fam=fam0 #pick the only one we have
                famranks.append(fam)
            elif fam1!='': #only fam1 was found
                fam=fam1
                famranks.append(fam)
            if friend0!='' and friend1!='': #repeat same for the friends
                friend=(friend0.ranks[genre]+friend1.ranks[genre])/2 #median again
                friendranks.append(friend)
            elif friend0!='':
                friend=friend0
                friendranks.append(friend)
            elif friend1!='':
                friend=friend1
                friendranks.append(friend)

        print("The student ranks (x) for Genre #%i were: "%genre, end="")
        print(studentranks)
        print("The family ranks (y1) for Genre #%i were: "%genre, end="")
        print(famranks)
        print("The friend ranks (y2) for Genre #%i were: "%genre, end="")
        print(friendranks)

        r,p=spearmanr(studentranks,famranks)
        print("The correlation coefficient between students and family members for Genre #%i was %%2.5f (p=%2.5f)"%(genre,r,p))
        famccs.append(r,p)
        r,p=spearmanr(studentranks,friend)
        print("The correlation coefficient between students and friends for Genre #%i was %%2.5f (p=%2.5f)"%(genre,r,p))
        friendccs.append(r,p)

        return famccs, friendccs

def main():
    #create lists to hold student and family objects:
    studs=[]
    fams=[]
    print(students)
    print(families)
    print("CSVs were successfully imported into the pandas dataframe; proceeding to creating objects for each individual.")

    # add a student/family object for each row in the dataframe
    print(students.shape[0]) #prints 76
    for row in range(students.shape[0]):
        print(row)
        studs.append(student(row)) #create students
        studs[row].display()
        if len(studs)!=1:
            studs[row-1].display()
    for row in studs:
        print(row.ranks)
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
    genecc,envcc=srcc(studs,fams)

    print("The average correlation coefficient for a genetic  relationship is "+str(mean(genecc)))
    print("The average correlation coefficient for an environmental relationship is "+str(mean(envcc)))

if __name__=="__main__":
    from scipy.stats import wilcoxon,chi2_contingency,spearmanr #needed for statistical testing
    from statistics import mean,multimode #needed for descriptive statistics
    from people import * #needed dataframes & classes from ./people.py
    main()
