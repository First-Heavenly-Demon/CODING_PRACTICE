def is_leap(year):
    is_leap = (year % 400 == 0) or year % 4 == 0 and year %100 !=0
    return is_leap
year = int(input())
print(is_leap(year))

#Single line comment
