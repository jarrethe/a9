To use the microservice, write the expected username and password to the file "auth.txt" Then, write the entered username and password. The order can be reversed, you can write the entered username and password first then the expected username and password. The format of auth.txt should be as follow:

{bof}
expected username
expected password
entered username
entered password
{eof}

This could be written into auth.txt with the following python code:
with open("auth.txt", "w") as file:
  file.write("expected username\nexpected password\nentered username\nentered password")

It is important that there is no empty line at the end of the file. The file needs to be exactly 4 lines for the program to read and assess the data properly.

To receive the data, wait one second (or remove the time.sleep(1)/line 25 of auth.py), and read the file. Then, read the file into a variable. Reading could be done with the following python code:

with open("auth.txt", "r") as file:
  authorized = file.read()
if authorized == "1":
  #the credentials match
if authorized == "0":
  #the credentials do not match

UML diagram:

<img width="598" alt="Screenshot 2023-07-31 at 7 11 17 PM" src="https://github.com/jarrethe/a9/assets/103973092/7be03a93-47d6-4840-8c4f-5c425fba1cd3">

