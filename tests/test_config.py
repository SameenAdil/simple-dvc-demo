# assert syntax:   assert condition, "error message"
# Meaning:    check condition (in my thinking check/use returned value)
          #If condition is True  → continue
       #If condition is False → raise AssertionError

# example: 1
# age = 5
# assert age>=5 
# print("Allowed to play")        Output: Allowed to play

#example: 2
# age =10
# assert age>=18, "Age must be 18 or above"
# print("Allowed to Drive")       Output: Age must be 18 or above

#################################################

import pytest

class NotInRange(Exception):
    def __init__(self, message="wrong value"):
        self.Message = message
        super().__init__(message)


def test_generic():     #1st method to use pytest
    a=5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange("value not in range")
        

# def divide(a,b):             #2nd method to use pytest
#     if b==0:
#         raise ZeroDivisionError()
#     return a/b
# def test_divide():
#     with pytest.raises(ZeroDivisionError):
#         divide(10,0)
