def is_leap(year):
    leap = False
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                leap=True
        else:
            leap=True
    return leap

def is_leap(year):
    return (year % 400 == 0) or (( year % 100 != 0) and (year % 4 == 0))



def is_leap(year):
    leap = False
    if year%4==0:
        if year%100!=0:
            leap=True
        else:
            if year%400==0:
                leap=True
    return leap


def is_leap(year):
    leap = False
    if year%4==0:
        if year%100!=0 or year%400==0:
            leap=True
    
    return leap

year = int(input())
print(is_leap(year))