# MSB Final Project
This repo contains code for my MSB final project (licensed under GPLv3.0), which includes the following:
- requirements.txt: use `python3 -m pip install -r requirements.txt` to install all deps
- wrapper.sh: just run as `./wrapper.sh`; it's a shell script to clean up data and run the Python programs.

- main.py: main Python script used to analyze data (run statistical tests) 
- people.py: Python script with class definitions for students and family members

- Report.tex/Report.pdf: source code and compiled version of the project report, describing the results

In order to use this program in its current working state, you would need to place two spreadsheets, "Students.csv" and "Family.csv", inside a subfolder called `private`. Note that the anonymized versions of the data in family_data.tex and students_data.tex (for use in the report) will not work for this purpose.
- I may try to rework the code so that the anonymized data can be used too, but it might not be accomplished anytime soon (as the study itself is already complete).
