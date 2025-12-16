#n = int(input("Enter a number: "))

def ator(n):
    if n <= 0 or n > 3999:
        return None
    thousands = n//1000 * "M"
    
    match n%1000//100:
        case 1: hundreds = "C"
        case 2: hundreds = "CC"
        case 3: hundreds = "CCC"
        case 4: hundreds = "CD"
        case 5: hundreds = "D"
        case 6: hundreds = "DC" 
        case 7: hundreds = "DCC"
        case 8: hundreds = "DCCC"
        case 9: hundreds = "CM"
        case _: hundreds = ""

    match n%100//10:
        case 1: tens = "X"
        case 2: tens = "XX"
        case 3: tens = "XXX"
        case 4: tens = "XL"
        case 5: tens = "L"
        case 6: tens = "LX" 
        case 7: tens = "LXX"
        case 8: tens = "LXXX"
        case 9: tens = "XC"
        case _: tens = ""

    match n%10:
        case 1: units = "I"
        case 2: units = "II"
        case 3: units = "III"
        case 4: units = "IV"
        case 5: units = "V"
        case 6: units = "VI" 
        case 7: units = "VII"
        case 8: units = "VIII"
        case 9: units = "IX"
        case _: units = ""

    romanNumber = thousands + hundreds + tens + units
    return romanNumber

#print(ator(n))