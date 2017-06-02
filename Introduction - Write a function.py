def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0 and year%4==0:
        return not leap
    else:
        return leap