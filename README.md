# secure_password_checker
This script allows to check  if user's password was ever pawned without sharing the password with anybody. 

User saves password in the file locally, script takes that file, hash it, make a request with frist 5 chars of hashed password. After recieving a response, if it is not empty, script compares left chars from hashed password to see if user's password has a match.
