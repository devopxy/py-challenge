Metrichor Challenge
=================

The purpose of this exercise is to create an utility that finds a total of `seqlen` values in all files matching `*.data.json` pattern that are found in a given folder

What you need to do
-------------------

1. Create a python script that takes a folder name as an input parameter, parses all the files and prints a total sum of all values for `seqlen` field
    - The script should handle invalid values appearing in `seqlen` field
    - Write at least one test for your code
    - Track your changes using git

2. You should deliver your solution as a `git` repository, preferably hosted on GitHub.

What we are looking for:
-------------------
1. Functionality (you write code that does what it's supposed to do)
2. Readability (you clean your code)
3. Good code design (you demonstrate code re-use)
4. Best practice (you acknowledge established code conventions from the Python community)


The `seqlen` total utility:
--------------------------

The python sources are as follows :

1. app.py - is the python application 
2. test.py - unit test for the application

Both these indivisual sources need the command-line parameter stating the path of the `*.data.json` files to them.

Example:
   
`$ python3 app.py -p <path to the data dir>`
 
`$ python3 test.py -p <path to the data dir>`


A Bash script `run-app-test.sh` automates a sample run and test of using both of these files. The script
needs to set the variable DATAPATH to the path of the directory containing `*.data.json` files.

Future Improvements:
-----------------------
1. Decision making and exception handling of commandline parameters
2. Improving the performance with respect to disk I/O as the app.py is making freqent disk calls while reading the data line-by-line. 
