This directory contains a program written in python to simulate a twitter feed. 

How to run: 

TODO 

Assumptions made: 

* A username cannot contain the name 'follows'.
* Every line in the user.txt file must contain the word 'follows'.
* Every line in the user.txt file must contain a user or users after the token 'follows'. If there are multiple users, they will be comma seperated. 
* Every line in user.txt and tweet.txt will be seperated with a 'newline'. A CR and LF as provided in the sample input files.
* A username can only contain alphanumeric characters (letters A-Z, numbers 0-9) with the exception of underscores [1].
* Feeds for users listed in users.txt are displayed. Users in tweet.txt which are not in user.txt are not processed.
* Invalid input files will not process an output feed.
* Input files should not contain non-ascii characters. 
* In the statement: "Then for each tweet, emit a line with the following format: <tab>@user: <space>message." Tab is assumed to be 4 spaces.


References:
[1] https://help.twitter.com/en/managing-your-account/twitter-username-rules