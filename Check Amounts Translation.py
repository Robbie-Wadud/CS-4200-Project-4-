# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:54:31 2020

@author: Robbi
"""

#Import Statements
from fractions import Fraction

#Introduce the program
print('Let\'s translate dollar amounts to words up to $1000')

#Create a dictionary for unique words
numberToWords = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', 10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 30: 'THIRTY', 40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY', 80: 'EIGHTY', 90: 'NINETY', 100: 'ONE HUNDRED', 200: 'TWO HUNDRED', 300: '', 400: 'FOUR HUNDRED', 500: 'FIVE HUNDRED', 600: 'SIX HUNDRED', 700: 'SEVEN HUNDRED', 800: 'EIGHT HUNDRED', 900: 'NINE HUNDRED'}

#Ask the user to type in a decimal number up to 1000 (In case the user types in a non-int)
while True:
    try:
        dollarAmount = float(input('Please type in a dollar amount you would like to convert to a word: $'))
        break
    except ValueError:
        print('\nYou have typed in an invalid number. You have to type in a valid dollar amount.')

#Validation loop
while dollarAmount < 0 or dollarAmount > 1000:
    print('\nYou have typed in a number that is not acceptable. You have to type in a valid dollar amount under $1000 (that\'s also not negative)')

    #In case the user types in a non-int
    while True:
        try:
            dollarAmount = float(input('Please type in a dollar amount you would like to convert to a word: $'))
            break

        except ValueError:
            print('\nYou have typed in an invalid number. You have to type in a valid dollar amount.')

#Round the decimal number to two places only
dollarAmount = round(dollarAmount, 2)

#Creating the same number without the decimal portion
dollarAmountNoCents = dollarAmount // 1
dollarAmountNoCents = int(dollarAmountNoCents)

#Creating the cents
cents = (dollarAmount - dollarAmountNoCents) * 100
cents = int(cents)
cents = str(cents)

#Function to get the hundreds digit
def hundredsFunction(aNumber):

    #Creating an empty string for the hundreds part
    hundredsString = ''

    #If statement to see if there is a hundreds position
    if aNumber / 100 >= 1:

        #Get the hundreds digit
        hundreds = aNumber // 100

        #Add the hundreds string to the number string
        hundredsString += numberToWords.get(hundreds * 100)

    return hundredsString

#Function to get the tens digit
def tensFunction(aNumber):

    #Changing our dollar amount so it can be manipulated
    aNumber = aNumber - ((aNumber // 100) * 100)

    #Creating an empty string for the tens part
    tensString = ''

    #In case the number is between 11 - 19
    if (aNumber == 11) or (aNumber == 12) or (aNumber == 13) or (aNumber == 14) or (aNumber == 15) or (aNumber == 16) or (aNumber == 17) or (aNumber == 18) or (aNumber == 19):
        tensString = numberToWords.get(aNumber)

    #If statement to see if there is a tens position
    elif aNumber / 10 >= 1:

        #Get the tens digit
        tens = aNumber // 10

        #Add the tens string to the number string
        tensString += numberToWords.get(tens * 10)

    return tensString

#Function to get the ones digit
def onesFunction(aNumber):

    #Changing our dollar amount so it can be manipulated
    aNumber = aNumber - ((aNumber // 100) * 100)

    #Creating an empty string for the ones part
    onesString = ''

    #In case the number is between 11 - 19
    if (aNumber == 11) or (aNumber == 12) or (aNumber == 13) or (aNumber == 14) or (aNumber == 15) or (aNumber == 16) or (aNumber == 17) or (aNumber == 18) or (aNumber == 19):
        onesString = ''

        #Changing our dollar amount again so it can be manipulated
        aNumber = aNumber - ((aNumber // 10) * 10)

    #Changing our dollar amount if it wasn't already
    aNumber = aNumber - ((aNumber // 10) * 10)

    #We now have the ones digit!
    if aNumber > 0:

        #Add the ones string to the number string
        onesString += numberToWords.get(aNumber)

    return onesString

#Final Sentence
print(hundredsFunction(dollarAmountNoCents) + ' ' + tensFunction(dollarAmountNoCents) + ' ' + onesFunction(dollarAmountNoCents) + ' AND ' + cents + '/100')