## Twitter Feed Simulation Program

This directory contains a program written in python in Windows to simulate a twitter feed. 

### How to Run Program:

Python version 3.7.4, or later and a windows 10 operating system is required to run the program. 

Python can be downloaded from python.org: 
[Download Python](https://www.python.org/downloads/)

Please ensure the correct path to the input text files are provided.

$ python TwitterFeedSimulation.py user.txt tweet.txt

For Unit Tests:

$ python TwitterFeedSimulation.py


### Assumptions Made: 

* List of users and their followers will be provided in a file named 'user.txt'.
* List of users and their tweets will be provided in a file named 'tweets.txt'.
* There will be at minimum, at least one tweet.
* A username cannot contain the name 'follows'.
* Every line in the user.txt file must contain the word 'follows'.
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

* Dockerize application to run on any operating system