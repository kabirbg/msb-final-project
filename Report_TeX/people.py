#!/usr/bin/env python3

from pandas import read_csv  # necessary for importing csv data as a pandas dataframe

students = read_csv("private/Students.csv")  # initialize dataframe for students
families = read_csv("private/Family.csv")  # and one for families


class Student:
    def __str__(self):
        return (
            str(self.name)
            + "\n"
            + str(self.ranks)
            + "\n"
            + str(self.fam)
            + "\n"
            + str(self.friends)
        )

    @classmethod
    def at_row(cls, n: int):
        row = [student for student in students.iloc[n]]
        return cls(row)

    # Construct a Student from a row of data. This row is expected to be laid
    # out in (first name, last name, ...  musics ..., family member a first name,
    # family member a last name, family number b first name, family number b
    # last name, friend a first name, friend a last name, friend b first name,
    # friend b last name).
    def __init__(self, row):
        self.name = (
            row[0],
            row[1],
        )

        self.fam = [
            (row[15], row[16]),
            (row[17], row[18]),
        ]

        self.friends = [
            (row[19], row[20]),
            (row[21], row[22]),
        ]

        self.ranks = [-1 for n in range(1, 7)]

        # generate & store rankings
        genres = row[2]  # temporarily store genre selections
        musics = [row[n] for n in range(3, 15)]

        # Each genre is represented by a number (1=pop, 2=jazz & blues, etc).
        for genre in range(1, 7):
            if str(genre) in genres:  # liked the genre
                self.ranks[genre - 1] = (
                    3 + musics[genre * 2 - 2] + musics[genre * 2 - 1]
                )
            else:  # disliked the genre
                self.ranks[genre - 1] = musics[genre * 2 - 2] + musics[genre * 2 - 1]


class Family:  # I'll have one object of this type for each participating family member; identical to Student but lacks fam[] and friends[]
    def __str__(self):
        return str(self.name) + "\n" + str(self.ranks)

    @classmethod
    def at_row(cls, n: int):
        row = [family for family in families.iloc[n]]
        return cls(row)

    # Construct a Family from a row of data. This row is expected to be laid
    # out in (first name, last name, genres,  musics ...).
    def __init__(self, row):
        self.name = (
            row[0],
            row[1],
        )

        self.ranks = [-1 for n in range(1, 7)]

        # generate & store rankings
        genres = row[2]  # temporarily store genre selections
        musics = [row[n] for n in range(3, 15)]

        # Each genre is represented by a number (1=pop, 2=jazz & blues, etc).
        for genre in range(1, 7):
            if str(genre) in genres:  # liked the genre
                self.ranks[genre - 1] = (
                    3 + musics[genre * 2 - 2] + musics[genre * 2 - 1]
                )
            else:  # disliked the genre
                self.ranks[genre - 1] = musics[genre * 2 - 2] + musics[genre * 2 - 1]
