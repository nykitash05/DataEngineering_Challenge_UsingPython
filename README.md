# DataEngg_Challenge_Solution
This repository gives the solution to Insight's Data Engineering Coding Challenge.

# Introduction
This repository is designed to solve Insight's Data Engineering Coding challenge. The Dataset used for this project is the Border crossing Dataset regularly maintained by Bureau of Transportation services. 

# Problem Statement:
To calculate the total number of times vehicles or equipment or passengers or pedestrians cross the U.S-Canadian and U.S-Mexican borders each month. Also calculate the running monthly average of total number of crossings for that type of crossing and border.

# Solution:
The solution to the given problem is designed using Python Programming language with basic Data Structures i.e. without involving any external packages like numpy , pandas etc as per Insight's Coding Challenge rules & regulations. The main code to the problem is written in border_analytics.py file placed under 'src' folder. The code reads input csv file from 'input' folder and then reads data line by line to do further processing. Two main modules are written in the code one which does the summation task & other which calculates the Average as desired and then sorts the data in descending order by : Date, Value, Measure & border. Summation task involves summing the total number of crossings (Value) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of the port used.The Average is calculated as below:

Ex:
Border,Date,Measure,Value,Average
US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,114487

To calculate the Average for the first line (i.e., running monthly average of total pedestrians crossing the US-Mexico Border in all of the months preceding March), we have taken average sum of total number of US-Mexico pedestrian crossings in February 156,891 + 15,272 = 172,163 and January 56,810, and rounded it to the nearest whole number round(228,973/2) = 114,487

The given data is quite cleaned so we didn't have much issues but incase the data is not cleaned and there are certain missing values then a provision is made in the code which will skip the row if entire row is missing or if values of the important fields are missing like Border, Date,Measure, Value. This is done with a mindset that if these values are missing one cannot decide on whether they should be added with the sum or not. In case data has duplicate rows, no such rows will be removed or skipped. All rows will be taken in consideration as we cannot say if these are duplicates or a true record.

# Program execution can be done using following command:
python3 ./src/border_analytics.py ./input/Border_Crossing_Entry_data.csv ./output/report.csv

[Note: If the above 'python3' command gives you error, you may also use 'python' inplace of 'python3']

(To run the program, download this repository and go to the directory of our repository in command prompt where you will see all the folders like- input, src,output etc. Copy above line of code & run it or use run.sh shell script to perform the execution)

(To run the testsuits, go one step further and enter inside insight_testsuit folder, run run_tests.sh file in command prompt. Upon successful execution, both the tests will show as Pass)

As per this command, input data file will be read from 'input' folder, main code named- border_analytics.py will be read from 'src' folder and then corresponding output csv file called 'report.csv' will be generated under 'output' folder. Insight has also provided us with Insight testsuit which has been updated with one more test case - dataset having missing values. Both of these tests passed successfully.

