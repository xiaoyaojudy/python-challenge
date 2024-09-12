# Import the os module
import os

# Module for reading CSV files
import csv

# Improved Reading using CSV module

with open ('budget_data.csv') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile, delimiter=',')

    # Read the header row first
    header=next(csvreader)

    # Prepare variables
    months=[]
    profitlosses=[]

    # Set start conditions
    total=0
    a_change=0
    m_change=0
    m_count=0
    delta1=0
    delta2=0
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

    #Read data after the header and write data into lists
    for row in csvreader:
        month=row[0]
        proloss=row[1]
        months.append(month)
        profitlosses.append(proloss)
    
    m_count = len(months)
    
    # Data analysis

# First loop
for loop1 in range (m_count):
    total=total+int(profitlosses[loop1])

# Second loop
for loop2 in range (m_count-1):
    a_change=a_change+(float(profitlosses[loop2+1])-float(profitlosses[loop2]))

    m_change=(float(profitlosses[loop2+1])-float(profitlosses[loop2]))
    if m_change>delta1:
        delta1=m_change
        delta_line1=loop2
    else:
        delta1=delta1

    if m_change<delta2:
        delta2=m_change
        delta_line2=loop2
    else:
        delta2=delta2

# Generate output lines - analysis

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

# Print results
print(analysis)

# Export a text file with the results
file1=open("pybank.txt","w")
file1.writelines(analysis)
file1.close()