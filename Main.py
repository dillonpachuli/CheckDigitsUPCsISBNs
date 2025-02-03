# Dillon Chapuli Check Digits, UPCs, and ISBNs 1.31.25

import random
from barcode import UPCA
from barcode import Code39
from barcode import EAN13
from barcode.writer import ImageWriter

def UPC_check_digit(numList):
    result = 0     
    for i in range (len(numList)):
        if (i % 2 == 0):
            result += int(numList[i])
    result *= 3
    for i in range (len(numList)):
        if (i % 2 == 1):
            result += int(numList[i])
    result = result % 10
    result = 10 - result
    if (result == 10):
        result = 0
    return result

def ISBN_10_check_digit(numList):
    result = 0
    for i in range (len(numList)):
        result += int(numList[i]) * (10 - i)
    result = result % 11
    result = 11 - result
    if (result == 10):
        result = "X"
    return result

def ISBN_13_check_digit(numList):
    result = 0
    for i in range (len(numList)):
        if (i % 2 == 0):
            result += int(numList[i])
        elif (i % 2 == 1):
            result += int(numList[i]) * 3
    result = result % 10
    result = 10 - result
    if (result == 10):
        result = 0
    return result

#----------------------------------------------------------------------------------------------------------------------------

print("")

print("Welcome to the computer program for Dillon and Nicole's group project, programmed by Dillon!")
print("There are three different programs that lie ahead.")
print("You get to choose which program you would like to try:")
print("")
print("  1. Check Digit Validator")
print("  You enter a full code, and the program verifies if the check digit is valid or not.")
print("")
print("  2. Check Digit Calculator")
print("  You enter the first bit of a code, and the program calculates the check digit for you.")
print("")
print("  3. Barcode Generator")
print("  The program generates a random valid code and creates a corresponding barcode.")
print("")
program = int(input("Which program would you like to use? Enter 1, 2, or 3: "))
if (program == 1):
    print("You have selected program 1: Check Digit Validator.")
if (program == 2):
    print("You have selected program 2: Check Digit Calculator.")
if (program == 3):
    print("You have selected program 3: Barcode Generator.")
print("---------------------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------------------------------------

if (program == 1):
    code = input("Enter a UPC or ISBN: ")

    if (len(code) == 12):
        print("Your code has 12 digits, therefore it's a UPC")

        digitsList = []
        for digit in code:
            digitsList.append(digit)   
        digitsList.pop(11)
        checkDigit = UPC_check_digit(digitsList)

        print("The calculated check digit is " + str(checkDigit) + ".")
        if (checkDigit == int(code[11])):
            print("It matches the check digit in the code, therefore this UPC is valid! :)")
        else:
            print("It does not match the check digit in the code, therefore this UPC is invalid. :(")
    
    if (len(code) == 10):
        print("Your code has 10 digits, therefore it's an ISBN-10.")

        digitsList = []
        for digit in code:
            digitsList.append(digit) 
        digitsList.pop(9)
        checkDigit = ISBN_10_check_digit(digitsList)

        print("The calculated check digit is " + str(checkDigit) + ".")
        if (checkDigit == int(code[9])):
            print("It matches the check digit in the code, therefore this ISBN-10 is valid! :)")
        else:
            print("It does not match the check digit in the code, therefore this ISBN-10 is invalid. :(")

    if (len(code) == 13):
        print("Your code has 13 digits, therefore it's an ISBN-13.")

        digitsList = []
        for digit in code:
            digitsList.append(digit) 
        digitsList.pop(12)
        checkDigit = ISBN_13_check_digit(digitsList)

        print("The calculated check digit is " + str(checkDigit) + ".")
        if (checkDigit == int(code[12])):
            print("It matches the check digit in the code, therefore this ISBN-13 is valid! :)")
        else:
            print("It does not match the check digit in the code, therefore this ISBN-13 is invalid. :(")

#----------------------------------------------------------------------------------------------------------------------------

if (program == 2):
    code = input("Enter an incomplete UPC or ISBN that is missing its check number: ")

    if (len(code) == 11):
        print("There are 11 digits, therefore it's an incomplete UPC.")

        digitsList = []
        for digit in code:
            digitsList.append(digit)   
        checkDigit = UPC_check_digit(digitsList)

        print("The calculated check digit is " + str(checkDigit) + ".")
        print("The final UPC is " + code + str(checkDigit) + "! :)")
    
    if (len(code) == 9):
        print("There are 9 digits, therefore it's an incomplete ISBN-10.")

        digitsList = []
        for digit in code:
            digitsList.append(digit) 
        checkDigit = ISBN_10_check_digit(digitsList)

        print("The calculated check digit is " + str(checkDigit) + ".")
        print("The final ISBN-10 is " + code + str(checkDigit) + "! :)")

    if (len(code) == 12):
        print("There are 12 digits, therefore it's an incomplete ISBN-13.")

        digitsList = []
        for digit in code:
            digitsList.append(digit) 
        checkDigit = ISBN_13_check_digit(digitsList)

        print("The calculated check digit is " + str(checkDigit) + ".")
        print("The final ISBN-13 is " + code + str(checkDigit) + "! :)")

#----------------------------------------------------------------------------------------------------------------------------

if (program == 3):
    type = int(input("Would you like to generate a UPC, an ISBN-10, or an ISBN-13? Enter 1, 2, or 3: "))

    if (type == 1):
        print("You have selected UPC.")

        code = ""
        for i in range (11):
            code += str(random.randint(0, 9))
        digitsList = []
        for digit in code:
            digitsList.append(digit)
        code += str(UPC_check_digit(digitsList))

        print("The generated UPC is " + code + "! :)")
        barcode = UPCA(code, writer=ImageWriter())
        barcode.save("UPC_barcode")
        print("The UPC barcode has been generated! Go check it out! :)")
    
    if (type == 2):
        print("You have selected ISBN-10.")

        code = ""
        for i in range (9):
            if (i == 0):
                code += str(random.randint(0, 1))
            else:
                code += str(random.randint(0, 9))
        digitsList = []
        for digit in code:
            digitsList.append(digit)   
        code += str(ISBN_10_check_digit(digitsList))

        print("The generated ISBN-10 is " + code + "! :)")
        barcode = Code39(code, writer=ImageWriter(), add_checksum=False)
        barcode.save("ISBN-10_barcode")
        print("The ISBN-10 barcode has been generated! Go check it out! :)")
    
    if (type == 3):
        print("You have selected ISBN-13.")

        code = "97"
        for i in range (10):
            if (i == 0):
                code += str(random.randint(8, 9))
            else:
                code += str(random.randint(0, 9))
        digitsList = []
        for digit in code:
            digitsList.append(digit)   
        code += str(ISBN_13_check_digit(digitsList))

        print("The generated ISBN-13 is " + code + "! :)")
        barcode = EAN13(code, writer=ImageWriter())
        barcode.save("ISBN-13_barcode")
        print("The ISBN-13 barcode has been generated! Go check it out! :)")

print("")