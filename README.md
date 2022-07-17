# Twitter Feed Simulation

This repository contains the solution to the twitter- like feed simulation program written in python. 

## The Task: 

Write a program to simulate a twitter-like feed. Your program will receive two seven-bit ASCII files. The first file contains a list of users and their followers. The second file contains tweets. Given the users, followers and tweets, the objective is to display a simulated twitter feed for each user to the console. 

Each line of a well-formed user file contains a user, followed by the word 'follows' and then a comma separated list of users they follow. Where there is more than one entry for a user, consider the union of all these entries to determine the users they follow.

Lines of the tweet file contain a user, followed by greater than, space and then a tweet that may be at most 140 characters in length. The tweets are considered to be posted by each user in the order they are found in the file.

Your program needs to write console output as follows. For each user / follower (in alphabetical order) output their name on a line. Then for each tweet, emit a line with the following format: <tab>@user: <space>message.

