class TooLowNumberException(Exception):
    pass

a = int(input())

if a < 5:
    raise TooLowNumberException("The number is too low, enter higher")
