# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:54:31 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s translate dollar amounts to words up to $1000')

#Create a dictionary for unique words
numberToWords = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', 10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 30: 'THIRTY', 40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY', 80: 'EIGHTY', 90: 'NINETY', 100: 'ONE HUNDRED', 200: 'TWO HUNDRED', 300: '', 400: 'FOUR HUNDRED', 500: 'FIVE HUNDRED', 600: 'SIX HUNDRED', 700: 'SEVEN HUNDRED', 800: 'EIGHT HUNDRED', 900: 'NINE HUNDRED'}

#Var to store the number in a string
wordNumber = ''

#Ask the user to type in a decimal number up to 1000
decimalNumber = float(input('Please type in a dollar amount you would like to convert to a word: $'))

#Round the decimal number to two places only
decimalNumber = round(decimalNumber, 2)








#Printing out vars
#print(decimalNumber)
#print(wordNumber