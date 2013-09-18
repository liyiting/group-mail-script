# GroupMail Script
## Description
Script used to send grading emails to a group of students.  
Wrote this script to ease my job of being a teaching assistant.  
It works by parsing a csv file of grading report then send emails based on the UNI in the first column of the csv file.  
## Example
score.xls is a example grade report excel.  
The title row must start with "title" and the total score row must start with "credit".  
Save the xls as a csv file with the Field Delimiter and Quote Char specified in the script (This is supported by most excel tools).  
Help of the command:  
```
age: groupmail.py file [options]

Options:
  -h, --help        show this help message and exit
  -s, --send        send email, if not set, just print e-mail content
  -n, --no-confirm  no ask for comfirmation of the content of each e-mail
                    before send
```
Run the script using the following command:  
```
python groupmail.py <csvfilename> -s
```
Sample email output (All student IDs in the git repo records are not real):
```
Hi, aa1234:

S6666 homework grade report:

Problem 1
Compiles: 7.5/7.5
Runs: 5.5/7.5
Style: 7/7.5
Design: 7.5/7.5
Feedback: bad format;didn't count the correct check number

Problem 2
Compiles: 5/5
Runs: 1/5
Style: 5/5
Design: 3/5
Feedback: cannot accept input; wrong output; wrong algorithm

Late Penalty
0%

Total score
Written: 0
Programming: 41.5
Total: 41.5

Regards,
Yiting

```
