import csv
import os

#set path
Budget_answers = os.path.join("Pybank.txt")


#give python the worksheet to work with
csvpath = os.path.join("./budget_data.csv")

#set variables
i = 0
i = i + 1
Net_total = 0
Total = 0
Current_month_change= []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]


with open(csvpath) as csvfile:
    

#seperate each  file
    csvreader = csv.reader(csvfile)

#skip header #runs once 
    header = next(csvreader) 
    #print = next(header)
    print(header)
    print(f"Date: {header}")
    
    #Net total = first row
    First_row = next(csvreader)
    Total+= 1
    Net_total += int(First_row[1])
    prev_net = int(First_row[1]) 
       
    
#read each row #runs over and over again 85 time through csv reader(# of rows)
    for row in csvreader: # moves it down one at a time
        
        Total+= 1  #total+= 1 is the same thing 
        Net_total += int(row[1])
      


 #track net change 
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        Current_month_change += [row[0]]

        #calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #calculate greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

        #calculate average net change
        net_monthly_avg = sum(net_change_list) / len(net_change_list)


#Total months equation
print(Total)
print(Net_total)
print(net_monthly_avg)
print(greatest_increase)
print(greatest_decrease)
with open(Budget_answers,"w") as file:    #choose file location, #specify write mode
   file.write(f"Total Months: {Total} \n"
              f"Net Total: {Net_total}\n"
              f"Average Change: {round(net_monthly_avg, 2)}\n"
              f"Greatest Increase In Profits: {greatest_increase[0]} profit: $ {greatest_increase[1]}\n"
              f"Greatest Decrease In Profits: {greatest_decrease[0]} profit: $ {greatest_decrease[1]}\n")
 #f str = anything in braces {} is python code. 


Py_Results =(
        f"\nFinancial Analysis\n"
        f"--------------------------------------\n"
        f"Total Months: {Total}\n"
    f"Total: $ {Net_total}\n"
    f"Average Change: $ {round(net_monthly_avg, 2)}\n"
    f"Greatest Increase In Profits: {greatest_increase[0]} profit: $ {greatest_increase[1]}\n"
    f"Greatest Decrease In Profits: {greatest_decrease[0]} profit: $ {greatest_decrease[1]}\n")

print(Py_Results)    
    

with open (Budget_answers, "w") as file:
    file.write(Py_Results)

  


  

