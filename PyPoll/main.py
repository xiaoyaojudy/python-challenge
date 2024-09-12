# Import csv module
import csv

with open ('election_data.csv') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    # Prepare variables
    ballotids=[]
    counties=[]
    candidates=[]
    totalpercandidate=[]
    resultpercandidate=[]
    totalpercandiperc=[]

    # Set start conditions
    line_count=0
    winnervotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    # Read data after the header and write data into lists
    for row in csvreader:
        voterid=row[0]
        county=row[1]
        candidate=row[2]
        ballotids.append(voterid)
        counties.append(county)
        candidates.append(candidate)
    
    # Count the total number of votes cast in the "Voter ID" column
    line_count= len(ballotids) 
    

# Data analysis

candidates.append(candidates[0])

# First loop
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidates:
        candidates.append(candidates[loop1+1])

n=len(candidates)

# Second loop
for loop2 in range (n):
    totalpercandidate.append(candidates.count(candidates[loop2]))

# Third loop
# Calculate % per candidate
# Find candidate with highest/lowest vote count

for loop3 in range(n): 
    totalpercandiperc.append(f'{round((totalpercandidate[loop3]/line_count*100), 4)}%') 
    if totalpercandidate[loop3]>winnervotes: 
        winner=candidates[loop3]
        winnervotes=totalpercandidate[loop3]

#Fourth loop
#Format
for loop4 in range(n):
    resultpercandidate.append(f'{candidates[loop4]}: {totalpercandiperc[loop4]} ({totalpercandidate[loop4]})') 

# New combined list
resultlines='\n'.join(resultpercandidate) 

# Generate outputs
analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner}\n\
----------------------------\n'

print(analysis)

# Export a text file with the results
file1=open("pypoll.txt","w")
file1.writelines(analysis)
file1.close()