# Modules-------------------------------------------------------------------------------------------------------
import os
import csv



# PyBank Code----------------------------------------------------------------------------------------------------

# List Variables

Date_List = []
PL_List = []
Change_List = []

# Numerical Values

Total_Months = int(0)
RowCounter = int(0)
Change_Value = float(0)

# Import CSV
budget_csv = os.path.join("Resources","budget_data.csv")

# CSV Loop to Record Values to List

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
     # Read the header row first
    
    csv_header = next(csvreader)

    # Read each row of data after the header
    
    for row in csvreader:
        Date_List.append(row[0])
        PL_List.append(float(row[1]))
    
# For Loop to Calculate Changes in P/L (Current minus Last Months)

for i in range(len(Date_List)):
    
    if i==0:
        Change_List.append(float(0))
    else:
        Change_Value = PL_List[i] - PL_List[i-1]
        Change_List.append(Change_Value)

# Find Total P/L and Format

Total_PL = "%.0f" % sum(PL_List)

# Find Average Change and Format

Avg_Change = "%.2f" % (sum(Change_List)/len(Change_List))

# Find Greatest Increases & Decrease Indices

Inc_Ind = Change_List.index(max(Change_List))
Dec_Ind = Change_List.index(min(Change_List))

Inc_Val = "%.0f" % (Change_List[Inc_Ind])
Dec_Val = "%.0f" % (Change_List[Dec_Ind])

# Output Assignment Anwsers

print(" ")
print(" ")
print("PyBank Assignment Output")
print(" ")
print(" ")
print("Total Months: "+str(len(Date_List)))
print("Total: $"+str(Total_PL))
print("Average Change: $"+str(Avg_Change))
print("Greatest Increase in Profits: "+str(Date_List[Inc_Ind])+" ($"+str(Inc_Val)+")")
print("Greatest Decrease in Profits: "+str(Date_List[Dec_Ind])+" ($"+str(Dec_Val)+")")
print(" ")
print(" ")








# PyPoll Code----------------------------------------------------------------------------------------------------

# List Variables
Votes_List = []
Candidates_List = []
Total_Vote_List = []

# Variable for CSV Path

election_csv = os.path.join("Resources","election_data.csv")

# CSV Loop to Record Values to List

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
     # Read the header row first
    
    csv_header = next(csvreader)

    # Read each row of data after the header
    
    for row in csvreader:
        Votes_List.append(row[2])

# Assign Unique Candidates to List

Candidate_List = list(set(Votes_List))

# Calculate Total Votes in Election

Total_Votes = len(Votes_List)

# Count Total Votes for Candidate List by Index #

Votes_Ind0 = Votes_List.count(Candidate_List[0])
Votes_Ind1 = Votes_List.count(Candidate_List[1])
Votes_Ind2 = Votes_List.count(Candidate_List[2])
Votes_Ind3 = Votes_List.count(Candidate_List[3])

# Append Vote_Total List

Total_Vote_List.append(Votes_Ind0)
Total_Vote_List.append(Votes_Ind1)
Total_Vote_List.append(Votes_Ind2)
Total_Vote_List.append(Votes_Ind3)

# Calculate Percentage of Votes Won

Percent_Ind0 ="%.3f" % ((Votes_Ind0/Total_Votes)*100)
Percent_Ind1 ="%.3f" % ((Votes_Ind1/Total_Votes)*100)
Percent_Ind2 ="%.3f" % ((Votes_Ind2/Total_Votes)*100)
Percent_Ind3 ="%.3f" % ((Votes_Ind3/Total_Votes)*100)

# Determine Winner

Winner_Ind = Total_Vote_List.index(max(Total_Vote_List))
Winner_Name = Candidate_List[Winner_Ind]

# Output Assignment Anwsers

print("PyPoll Assignment Output")
print(" ")
print(" ")
print("Election Results")
print("--------------------------")
print("Total Votes: "+str(Total_Votes))
print("--------------------------")
print(str(Candidate_List[1])+": "+str(Percent_Ind1)+"% ("+str(Votes_Ind1)+")")
print(str(Candidate_List[2])+": "+str(Percent_Ind2)+"% ("+str(Votes_Ind2)+")")
print(str(Candidate_List[3])+": "+str(Percent_Ind3)+"% ("+str(Votes_Ind3)+")")
print(str(Candidate_List[0])+": "+str(Percent_Ind0)+"% ("+str(Votes_Ind0)+")")
print("--------------------------")
print("Winner: "+Winner_Name)
print("--------------------------")
print(" ")
print(" ")

# End--------------------------------------------------------------------------------------------------------

