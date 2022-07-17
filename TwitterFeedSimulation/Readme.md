## Twitter Feed Simulation Program

This directory contains a program written in python in Windows to simulate a twitter feed. 

### How to Run Program:

Python version 3.7.4, or later and a windows 10 operating system is required to run the program. 

Python can be downloaded from python.org: 
[Download Python](https://www.python.org/downloads/)

One can confirm that python is installed correctly if you open a terminal and type: python. It should return with the version that has been installed. 

In my environment, the return looks something like:

'''
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
'''

Clone the repository as follows: 

https://github.com/AmishaManga/TwitterFeedSim.git

Navigate to TwitterFeedSim -> TwitterFeedSimulation. Once in the TwitterFeedSimulation directory, open a terminal here and type:

$ python TwitterFeedSimulation.py user.txt tweet.txt

(Please ensure the correct path to the input text files are provided if not in current directory.)

For Unit Tests:

$ python TwitterFeedSimulation.py


### Assumptions Made: 

* List of users and their followers will be provided in a file named 'user.txt'.
* List of users and their tweets will be provided in a file named 'tweet.txt'.
* If there is a listed user in tweet.txt, there will be a corresponding tweet. In other words, no 'empty' tweets. Whitespaces are allowed in tweet message.
* If the tweet.txt file is completely empty but the user.txt file is completely valid, a plain list of users will be displayed in output feed.
* A username cannot contain the name 'follows'.
* Every line in the user.txt file must contain the word 'follows' and it must appear exactly once.
* Every line in the user.txt file must contain a user or users after the token 'follows'. If there are multiple users, they will be comma seperated. 
* Every line in user.txt and tweet.txt will be seperated with a 'newline'. A CR and LF as provided in the sample input files.
* A username can only contain alphanumeric characters (letters A-Z, numbers 0-9) with the exception of underscores [1].
* Feeds for users listed in users.txt are displayed. Users in tweet.txt which are not in user.txt are not processed.
* Invalid input files will not process an output feed.
* Input files should not contain non-ascii characters. 
* In the statement: "Then for each tweet, emit a line with the following format: <tab>@user: <space>message." Tab is assumed to be 4 spaces.


### References:
[1] [Twitter Username Rules](https://help.twitter.com/en/managing-your-account/twitter-username-rules)

### Future work: 

* Dockerize application to run on any operating system such that the user does not need to download python to run the code. I struggled to install Docker for windows on my machine therefore did not get this far.
* Add more Unit Tests. There are a few more unit tests I would have added, however due to time constraints this is where I am going to stop.
