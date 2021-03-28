import pandas as d
print("Enter the filename for a CSV: ")
filename=input()
responses=d.read_csv(filename)

print("Displayed as Pandas dataframe:")
print(responses.to_string())
print("\nDisplayed with loops :)\n")
for row in range(19):
    print("Student #%s:"%(row))
    for column in responses:
        print("%s: "%(column)+str(responses.at[row,column]))
    print("\n")
