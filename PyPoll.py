import os
import csv

Poll_answers = os.path.join("PyPoll.txt")

csvpath = os.path.join("./election_data.csv")

#set variables
Total_cast = 0
Candidate_dict = {}
Candidate_list = []
Percentage_list = []
Perentage_won = 0
Total_won = 0
Winner = ""
Winner_Count = 0
Winner_Percentage = 0

with open(csvpath) as csvfile: #name what i opened as csv file 



    #seperate each file, ready to read what i opened
    csvreader = csv.reader(csvfile)

    #skip header, not interested in computation
    header = next(csvreader) 
    print(header)
    print(f"Ballot ID {header}")

   

    for row in csvreader: #one row of csv at a time            

        #add total votes
        Total_cast +=1

    
        #keeps track of all votes 
        Current_Candidate = row[2] # rows and colums 0-2, go to index 2 and read what i opened, charles stock
        if Current_Candidate not in Candidate_list: 
            Candidate_list.append(Current_Candidate) #if first candidate isn't in there then add there name to the list
            Candidate_dict[Current_Candidate] = 0 #if candidate not in the list then add to dict
        
        #add a vote to that candiates vote    
        Candidate_dict[Current_Candidate]+=1

     #print variable through for loop   
    print(Total_cast)
   
# with open(Poll_answers, "w") as txt_file:
    Election_results =(
        f"\nElection Results\n"
        f"--------------------------------------\n"
        f"Total Votes: {Total_cast}:\n"
        f"----------------------------------------\n")
    print(Election_results)    
    


    # percetages for each candidate    
    #print winner, goes through loop once and goes to last second
    txt_write = {}
    for candidate in Candidate_list:
        Perentage_won = round(Candidate_dict[candidate] / Total_cast * 100, 3) #total votes, rounded
        Percentage_list.append(Perentage_won) #all %'s, go to the next
        txt_write[candidate] = f"{candidate}: {Perentage_won:.1f}% ({Candidate_dict[candidate]:,})\n"
        print(txt_write[candidate])
    



        if (Total_won < Candidate_dict[candidate]) and (Perentage_won) > (Winner_Percentage): #candiate = each candidate, #dict = all canddiates %
            Total_won = Candidate_dict[candidate]
            Winner_Percentage = Perentage_won
            Winner = candidate

    print(f"Winner: {Winner} {Winner_Percentage:.1f}% ({Total_won:,})\n")
        
    
    winning_person =( 
    f"------------------------------------------ \n"
    f"Winner: {Winner}\n"

f"------------------------------------------ \n")    

print(Winner)


with open(Poll_answers,"w") as file:
        
    
    file.write(Election_results)
    for can in Candidate_list:
        file.write(txt_write[can])
    file.write(winning_person)