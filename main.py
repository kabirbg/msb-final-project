#!/usr/bin/env python3


def findmatches(student, studs, fams):
    # assign family members and friends for a given student
    fam0 = ""  # an empty string by default
    fam1 = ""
    friend0 = ""
    friend1 = ""
    for friend in studs:
        if student.friends[0] == friend.name:
            friend0 = friend
        if student.friends[1] == friend.name:
            friend1 = friend
    for family in fams:
        if student.fam[0] == family.name:
            fam0 = family
        if student.fam[1] == family.name:
            fam1 = family
    return (fam0, fam1, friend0, friend1)


def wc(studs, fams):
    # initialize arrays to hold the results of the WC tests
    fam_results = []
    friend_results = []

    for index in range(len(studs)):
        student = studs[index]
        fam0, fam1, friend0, friend1 = findmatches(student, studs, fams)

        if fam0 != "":  # fam0 exists
            # run tests between student and family member 0
            if student.ranks == fam0.ranks:
                print(
                    "{} {} and {} {} (family member) have the same rankings. p=0".format(
                        student.name[1], student.name[0], fam0.name[1], fam0.name[0]
                    )
                )
                p = 0
            else:
                w, p = wilcoxon(student.ranks, fam0.ranks)
                print(
                    "The Wilcoxon test statistic between {} {} and {} {} (family member) is W={} (p={}).".format(
                        student.name[1],
                        student.name[0],
                        fam0.name[1],
                        fam0.name[0],
                        w,
                        p,
                    )
                )
            fam_results.append(p)

        if fam1 != "":  # fam1 exists
            # run tests between student and family member 1
            if student.ranks == fam1.ranks:
                print(
                    "{} {} and {} {} (family member) have the same rankings. p=0".format(
                        student.name[1], student.name[0], fam1.name[1], fam1.name[0]
                    )
                )
                p = 0
            else:
                w, p = wilcoxon(student.ranks, fam1.ranks)
                print(
                    "The Wilcoxon test statistic between {} {} and {} {} (family member) is W={} (p={}).".format(
                        student.name[1],
                        student.name[0],
                        fam1.name[1],
                        fam1.name[0],
                        w,
                        p,
                    )
                )
            fam_results.append(p)

        if friend0 != "":  # friend0 exists
            # run tests between student and friend 0
            if student.ranks == friend0.ranks:
                print(
                    "{} {} and {} {} (friend) have the same rankings. p=0".format(
                        student.name[1],
                        student.name[0],
                        friend0.name[1],
                        friend0.name[0],
                    )
                )
                p = 0
            else:
                w, p = wilcoxon(student.ranks, friend0.ranks)
                print(
                    "The Wilcoxon test statistic between {} {} and {} {} (friend) is W={} (p={}).".format(
                        student.name[1],
                        student.name[0],
                        friend0.name[1],
                        friend0.name[0],
                        w,
                        p,
                    )
                )
            friend_results.append(p)

        if friend1 != "":  # friend1 exists
            # run tests between student and friend 1
            if student.ranks == friend1.ranks:
                print(
                    "{} {} and {} {} (friend) have the same rankings. p=0".format(
                        student.name[1],
                        student.name[0],
                        friend1.name[1],
                        friend1.name[0],
                    )
                )
                p = 0
            else:
                w, p = wilcoxon(student.ranks, friend1.ranks)
                print(
                    "The Wilcoxon test statistic between {} {} and {} {} (friend) is W={} (p={}).".format(
                        student.name[1],
                        student.name[0],
                        friend1.name[1],
                        friend1.name[0],
                        w,
                        p,
                    )
                )

            friend_results.append(p)

    return (fam_results, friend_results)


def chi2(group1, group2):
    # conduct chi-square test for association
    g1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    g2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(10):
        for p in group1:
            if p >= 0.1 * x and p < 0.1 * (x + 1):
                g1[x] += 1
        for p in group2:
            if p > 0.1 * x and p < 0.1 * (x + 1):
                g2[x] += 1
    for p in group1:
        if p == 1:
            g1[9] += 1
    for p in group2:
        if p == 1:
            g2[9] += 1

    chi2observed = [g1, g2]
    print(
        "Here are the observed frequencies of each type of result for family members and friends, respectively:"
    )
    print(chi2observed)
    X2, p, df, ex = chi2_contingency(chi2observed)
    print(
        "Here are the expected frequencies of each type of result for family members and friends, respectively:"
    )
    print(ex)
    print(
        "The result of the Chi-Square Test for Association is test statistic X^2 = {} with {} degrees of freedom, which gives us a p-value of {}.".format(
            X2, df, p
        )
    )
    return p


def srcc(students, families):
    famccs = []
    friendccs = []
    fig, (famplot, friendplot) = plt.subplots(1, 2)
    for genre in range(6):  #
        studentranksa = []  # for fam
        studentranksb = []  # for friend
        famranks = []
        friendranks = []

        for student in students:
            fam0, fam1, friend0, friend1 = findmatches(student, students, families)

            studentranksa.append(student.ranks[genre])
            if fam0 != "" and fam1 != "":  # both of them were found
                famranks.append(
                    (fam0.ranks[genre] + fam1.ranks[genre]) / 2
                )  # median not mean
            elif fam0 != "":  # only fam0 was found
                famranks.append(fam0.ranks[genre])  # pick the only one we have
            elif fam1 != "":  # only fam1 was found
                famranks.append(fam1.ranks[genre])
            else:  # no family members were found
                studentranksa.remove(
                    student.ranks[genre]
                )  # we can't use this student's data

            studentranksb.append(student.ranks[genre])
            if friend0 != "" and friend1 != "":  # repeat same for the friends
                friendranks.append(
                    (friend0.ranks[genre] + friend1.ranks[genre]) / 2
                )  # median again
            elif friend0 != "":
                friendranks.append(friend0.ranks[genre])
            elif friend1 != "":
                friendranks.append(friend1.ranks[genre])
            else:
                studentranksb.remove(student.ranks[genre])

        print("The student ranks (x1) for Genre #%i were: " % (genre + 1), end="")
        print(studentranksa)
        print("The family ranks (y1) for Genre #%i were: " % (genre + 1), end="")
        print(famranks)
        print("The student ranks (x2) for Genre #%i were: " % (genre + 1), end="")
        print(studentranksb)
        print("The friend ranks (y2) for Genre #%i were: " % (genre + 1), end="")
        print(friendranks)

        gen_name = "Genre #%i" % (genre + 1)

        famplot.scatter(
            studentranksa, famranks, label=gen_name
        )  # add stud and fam to scatter plot
        friendplot.scatter(
            studentranksb, friendranks, label=gen_name
        )  # add stud and friend to scatter plot

        r, p = spearmanr(studentranksa, famranks)
        print(
            "The correlation coefficient between students and family members for Genre #%i was %2.5f (p=%2.5f)"
            % ((genre + 1), r, p)
        )
        famccs.append(r)
        r, p = spearmanr(studentranksb, friendranks)
        print(
            "The correlation coefficient between students and friends for Genre #%i was %2.5f (p=%2.5f)"
            % ((genre + 1), r, p)
        )
        friendccs.append(r)

    famplot.legend(loc="upper left")  # create legends
    famplot.set_xlabel("Student's score")
    famplot.set_ylabel("Family Members' median score")
    friendplot.legend(loc="upper left")
    friendplot.set_xlabel("Student's score")
    friendplot.set_ylabel("Friends' median score")
    friendplot.yaxis.set_label_position("right")  # so that it has room to be seen
    plt.savefig("scatter_plots.png")  # export to a png

    return famccs, friendccs


def main():
    # create lists to hold student and family objects:
    studs = []
    fams = []
    print(students)
    print(families)
    print(
        "CSVs were successfully imported into the pandas dataframe; proceeding to creating objects for each individual."
    )

    # add a student/family object for each row in the dataframe
    for row in range(students.shape[0]):
        studs.append(Student.at_row(row))  # create students
    for row in range(families.shape[0]):
        fams.append(Family.at_row(row))  # create family

    print(
        "Student/Family objects were successfully created; running Wilcoxon tests between each individual and their friends/family members."
    )

    # run wilcoxon tests
    genetic, environmental = wc(studs, fams)
    print()
    print("Here are the results of the Wilcoxon Tests for the family members:")
    print(genetic)
    print("Here are the results of the Wilcoxon Tests for the friends:")
    print(environmental)
    print("Here is the most common result of the tests for the family members:")
    print(multimode(genetic))
    print("Here is the most common result of the tests for the friends:")
    print(multimode(environmental))

    p = chi2(genetic, environmental)
    if p > 0.5:
        print(
            "WARNING: There is not a statistically significant association between relationship type and similarity of music choice. Following results may be very unreliable."
        )
    print()
    genecc, envcc = srcc(studs, fams)

    print("Genetic correlation coefficients, as a list: " + str(genecc))
    print("Environmental correlation coefficients, as a list: " + str(envcc))

    print(
        "The average correlation coefficient for a genetic relationship is "
        + str(mean(genecc))
    )
    print(
        "The average correlation coefficient for an environmental relationship is "
        + str(mean(envcc))
    )

    print()
    t, p = ttest_rel(genecc, envcc)  # paired t-test for two samples
    print(
        "The paired t-test for a difference between genetic and environmental correlation coefficients gave the test statistic t="
        + str(t)
        + "."
    )
    print("The p-value was " + str(p) + ".")


if __name__ == "__main__":
    from scipy.stats import (
        wilcoxon,
        chi2_contingency,
        spearmanr,
        ttest_rel,
    )  # needed for statistical testing
    from statistics import mean, multimode  # needed for descriptive statistics
    import matplotlib.pyplot as plt  # needed for graphing SRCC data
    from people import *  # needed dataframes & classes from ./people.py

    main()
