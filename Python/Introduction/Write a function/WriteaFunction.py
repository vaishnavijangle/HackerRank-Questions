def is_leap(n):
    leap = False
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return leap
   
year = int(input())
print(is_leap(year))