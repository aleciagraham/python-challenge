import os
import csv


#Assign variable for data on csv file and loop through lists
months = []    
county = []
candidate_name = []
khan_votes = 0
correy_votes =0
li_votes =0
otooley_votes =0
total_votes_cast=0
names={}
percent_names = {}
vote_count = {}

csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
   
    # Read each row of data after the header
    for row in csvreader:
    
      total_votes_cast = total_votes_cast +1

      if row[2] not in candidate_name:
            candidate_name.append(row[2])
            names[row[2]]=0
      names[row[2]]=names[row[2]]+1
  
 

    max_votes=0
    for x in names:
          percent_names[x]=names[x]/total_votes_cast*100
          votes = names[x]
          if votes>max_votes:
                max_votes=votes
                winner = x



    
    for x in names:
          vote_count[x]=names[x]+1
         
    #       

# set data to be able to print the output

text = (f"  Election Results \n"
      f" ------------------------------\n"
      f"  Total Votes: ({total_votes_cast}) \n"
      f" ------------------------------\n"
      # f"{candidate_name}\n"
      f"{candidate_name}:{percent_names}  {vote_count} \n"
    
      f"  Winner by popular vote: {winner}")
  
print(text)

# create output file for the analysis report
info_text = os.path.join('election.txt')

with open(info_text, "w") as textfile:

  textfile.write(text)

