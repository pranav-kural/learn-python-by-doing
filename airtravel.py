""" Model for aircraft flights """

class Flight:
    
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}")
        
        self._number = number
    
    def number(self):
        return