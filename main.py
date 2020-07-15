
import os
import csv

#set path

electiondata = os.path.join('..','Resources','election_data.csv')

with open ('election_data.csv') as csvfile:
    csvreder = csv.reader(electiondata, delimiter=',')
#def financialdata(electiondata):

#clarify csv headers
voterid = int(electiondata[0])
county = str(electiondata[1])
candidate = str(electiondata[2])

#The total number of votes cast
totalvotes = int(sum([2]))
print("Total number of votes:", totalvotes)


  #* A complete list of candidates who received votes
 
 #of occurances of the candidate on list
occurances = occurances.Counter(candidate)
return occurances
print (occurances)

  #* The percentage of votes each candidate won
votepercentage = occurances/totalvotes
retreturn (votepercentage)
print(votepercentage)
  #* The total number of votes each candidate won

  #* The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:
