class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {
            'I': 1,
            'IV': 4,
            'V':5,
            'IX': 9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C': 100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        } ## Storing the roman numerals in a dictionary
        strArray = [*s]
        ## parse the string that is passed into the function
        number = 0
        i = 0
        while i < len(strArray):
            if strArray[i] == 'I':
                ## Check the next index for V or X
                try:
                    if strArray[i+1] == 'V':
                        number = number + romanNumerals.get('IV')
                        i = i + 2
                        break
                    elif strArray[i + 1] == 'X':
                        number = number + romanNumerals.get('IX')
                        i = i + 2
                    else:
                        number = number + romanNumerals.get('I')
                        i = i + 1
                except(IndexError):
                    number = number + romanNumerals.get('I')
                    break

            elif strArray[i] == 'X':
                ## Check the next index for L or C
                try:
                    if strArray[i+1] == 'L':
                        number = number + romanNumerals.get('XL')
                        i = i+2
                    elif strArray[i + 1] == 'C':
                        number = number + romanNumerals.get('XC')
                        i = i + 2
                    else:
                        number = number + romanNumerals.get('X')
                        i = i + 1
                except(IndexError):
                    number = number + romanNumerals.get('X')
                    break
            elif strArray[i] == 'C':
                ## Check the next index for D or M
                try:
                    if strArray[i+1] == 'D':
                        number = number + romanNumerals.get('CD')
                        i = i+ 2
                    elif strArray[i + 1] == 'M':
                        number = number + romanNumerals.get('CM')
                        i = i + 2
                    else:
                        number = number + romanNumerals.get('C')
                        i = i + 1
                except(IndexError):
                    number = number + romanNumerals.get('C')
                    break
                    
            else: 
                if strArray[i] == "M" or strArray[i] == "D" or strArray[i] == "L" or strArray[i] == "C" or strArray[i] == "V" or strArray[i] == "X":
                    number = number + romanNumerals.get(strArray[i])
                    i = i + 1

        return number
