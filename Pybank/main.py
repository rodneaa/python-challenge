import os
import csv

#read csv file from path : C:\Users\rodne\python-challenge\PyBank\Resources

csvpath = os.path.join(".","Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first , then read and print the addl rows
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


#*******************Enter output file info here, ************************
 
# #create empty lists
    total_months = 0
    date_column = []
    profit_losses = []

    for row in csvreader:
        #print(row)
        date_column.append(row[0])  
        profit_losses.append(int(row[1]))

#print to python
    print(f"FINANCIAL ANALYSIS")
    print(f'---------------------------------------------')
   

        #The total number of months included in the dataset
total_months = len(profit_losses)
print(f'Total Months:', total_months)

        #The net total amount of "Profit/Losses" over the entire period

net_pl = sum(profit_losses)
print(f'Total:', net_pl)

        #Variables
changes=[]
count = 0
max_profit = 0
max_profit_month = ""
min_profit = 0
min_profit_month = ""
previous_profit = 0
change_in_profit = 0

#The changes in "Profit/Losses" over the entire period, and then the average of those changes 
for profit_loss in profit_losses:
    if count > 0:
        change_in_profit = profit_loss-previous_profit
        changes.append(change_in_profit)

        #find maximun
    if change_in_profit > max_profit:
        max_profit = change_in_profit
        max_profit_month = date_column[count]    
        #find minimum
    if change_in_profit < min_profit:
        min_profit = change_in_profit
        min_profit_month = date_column[count]
    count += 1
    previous_profit = profit_loss
    #print(changes) 
    #average = sum(changes)/len(changes)   
average = sum(changes)/((total_months) - 1)

print(f'Average Change:', round(average,2))

 
        #The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {max_profit_month} ({max_profit})' )
       
        #The greatest decrease in profits (date and amount) over the entire period
print(f'Greatest Decrease in Profits: {min_profit_month} ({min_profit})' )


# Print the contents in the text file
# Create text file to store results and store the contents in the variable "text_file"

new_txt_path = r'C:\Users\rodne\python-challenge\Pybank\Analysis'
text_file1 = "PyBank Analysis.text"
name= os.path.join(new_txt_path, text_file1)
if os.path.exists (new_txt_path):
    # create the file
    with open(name, "a") as f:
        print("FINANCIAL ANALYSIS", file=f)
        print("----------------------------", file=f)

        print("Total Months: ", total_months , file=f)
        print("Total:", net_pl,file=f)
        print("Average Change: ", round(average,2), file=f)
        print("Greatest Increase in Profits: ", ({max_profit_month}), ({max_profit}), file=f)
        print("Greatest Decrease in Profits: ", ({min_profit_month}), ({min_profit}), file=f)
        f.close()
#("'Total Months:', total_months") # \n'Total:', net_pl\n'Average Change: ' average\n, 'Greatest Increase in Profits: {max_profit_month} ({max_profit})'\n 'Greatest Decrease in Profits: {min_profit_month} ({min_profit})'")

