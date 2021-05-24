

def dayOfProgrammer(year):
    # Write your code here
    if 1700 <= year <= 1917 and year % 4 == 0:
        return "12.09."+str(year)
    elif 1700 <= year <= 1917 and year % 4 != 0:
        return "13.09."+str(year)
    elif year >= 1919:
        if year % 400 == 0 or year%4==0 and year%100!=0:
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    elif year == 1918:
        return "26.09.1918"


