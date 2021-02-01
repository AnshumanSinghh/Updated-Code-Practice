def leap_year(year): 
    '''
    Checks whether the given year is leap or not.
    ''' 
    if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
        return True
    return False

# Driver Code Starts
if __name__ == "__main__":
    year = int(input("Enter the year to check: "))
    if leap_year(year):
        print("It's a leap year!")
    else:
        print("Not a leap year!")
    
