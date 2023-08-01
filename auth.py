"""
Henry Jarrett - Jarrethe - CS361
This is the microservicce to implement into the partners project
This Microservice verifies the entered credentials with the expected credentials

Input: Expected credentials, entered credentials
format:
{bof}
expectedusername
expectedpassword
enteredusername
enteredpassword
{eof}

These can be entered one at a time or all at once. The program won't do anything until
all 4 are present.

Output: 1 (if they match), or 0 (if they do not match)
"""

import time

while (1 == 1):
    # delay, can be removed
    time.sleep(1)
    # read entire file into list of strings
    with open("auth.txt", "r") as file:
        lines = file.readlines()
    # if all 4 values are present, evaluate for matching
    if len(lines) == 4:
        with open("auth.txt", "w") as file:
            1
            if (lines[0] == lines[2]) and (lines[1].strip() == lines[3]):
                file.write("1")
                print("Credentials checkout")
            else:
                file.write("0")
                print("Error, expected values do not match entered values")
