#Author  : Nikita Sharma
#Created Date    : 16th February 2020
#Purpose : To run the Data Engineering Coding challenge program and get the desired report 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import csv
import sys
import math
from statistics import mean
from itertools import groupby

def Datasummation(input_data):
    sortedreader = sorted(input_data, key=lambda d: (d['Border'], d['Date'], d['Measure'])) #Sorting needed for successive group by function to work properly
    groups = groupby(sortedreader, key=lambda d: (d['Border'], d['Date'], d['Measure']))
    sumresults = [(*k, sum(int(item["Value"]) for item in g)) for k, g in groups]
    return (sorted(sumresults, key=lambda x: (x[1],x[3],x[2],x[0]), reverse=True)) #Sorts the output in decreasing order by Date, Value, Measure & Border

#Code to write final output csv file in output folder
def writeoutputfile(newresult):
    with open(sys.argv[2],"w+") as outreport:
        csvWriter = csv.writer(outreport,delimiter=',',lineterminator='\n')
        csvWriter.writerow(['Border','Date','Measure','Value','Average'])
        csvWriter.writerows(newresult)
        
def Datamean(sumresults):
    newresult = []
    for i in range(len(sumresults)):
        sortedreader = sorted(sumresults[i+1:], key=lambda d: (d[1], d[0]), reverse = True) #Sorting needed for successive group by function to work properly
        groups = groupby(sortedreader, key=lambda d: (d[1], d[0]))
        result = [sum(int(item[3]) for item in g if (item[0] == sumresults[i][0] and item[2] == sumresults[i][2])) for k,g in groups]
        result = list(filter(lambda a: a != 0, result))
        newresult.append([*sumresults[i],0] if not result else [*sumresults[i],math.ceil(mean(result))]) # If no values are present in previous months average is 0
    writeoutputfile(newresult)  #Call to write final report.csv file
      
def main():
    
    #Reading data from input file
    input_data = csv.DictReader(open(sys.argv[1]))
    #Cleaning data if missing values are present(Skip rows)
    input_data = [row for row in input_data if (row['Date'] and row['Border'] and row['Measure'] and row['Value'])]
    
    #Function to perform our summation calculation task
    sumresults = Datasummation(input_data)
    
    #Function to perform our Average calculation task
    Datamean(sumresults)
    

main()