def is_leap(year):
    
    if (year%4==0)&(year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False
        
    
    return leap


