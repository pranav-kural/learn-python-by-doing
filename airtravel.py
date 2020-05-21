""" Model for aircraft flights """
# ex: Flight("BA758", Aircraft("G-EUPT", "Airbus 319", num_rows=22, num_seats_per_row=6))

# import pprint for easier command line testing
from pprint import pprint as ppr

class Flight:
    """ A flight with a particular passenger aircraft """
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}")
        
        self._number = number
        self._aircraft = aircraft
        
        # get seating plan
        rows, seats = self._aircraft.seating_plan()
        
        # initialize seating
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        
        
    def aircraft_model(self):
        return self._aircraft.model()
    
    def number(self):
        return self._number
    
    # allocate a seat
    def allocate_seat(self, seat, passenger):
        """ 
        Allocate a seat to a passenger
        
        Args:
            seat: A seat designator such as '12C' or '32F'
            passenger: Name of the passenger
            
        Raises:
            ValueError: if seat is invalid or unavailable
        """
        # validate seat information provided
        row, seat_letter = self._parse_seat(seat)
        
        # verify if seat is available
        if self._seating[row][seat_letter] is not None:
            raise ValueError(f"Seat {seat} already occupied.")
        
        # if all validations successful and seat available
        self._seating[row][seat_letter] = passenger
    
    #seat validation method
    def _parse_seat(self, seat):
        # get the aircraft seating plan for validation
        rows, seat_letters = self._aircraft.seating_plan()
        
        # extract seat letter from seat requested
        seat_letter = seat[-1]
        if seat_letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {seat_letter}")
        
        # get row number requested
        row_text = seat[:-1]
        # validate if row number provided is an integer value
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text}")
        
        # validate if row number within seating plan
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")
        
        return row, seat_letter
    
    
    # relocate a passenger
    def relocate_passenger(self, from_seat, to_seat):
        """ 
        Relocate a passengar to a different seat
        
        Args: 
            from_seat: existing seat of passenger
            to_seat: seat to be transferred to
        """
        
        # validate from_seat
        from_row, from_letter = self._parse_seat(from_seat)
        # verify if seat is actually occupied and correct
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"Seat {from_seat} is not occupied by anyone. Please verify from which seat the passenger needs to be relocated.")
        
        # validate from_seat
        to_row, to_letter = self._parse_seat(to_seat)
        # verify if seat is available
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} is already occupied.")
        
        # if validations successful
        # assign passenger to the new seat
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        # remove passenger from old seat
        self._seating[from_row][from_letter] = None
        
    
    # check number of available seats
    def num_available_seats(self):
        # iterate through rows and check for available seats (none)
        return sum(sum(1 for s in row.value() if s is None) 
                   for row in self._seating if row is not None)


    # An iterable series of passenger seating locations
    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        # for every occupied seat return passenger name and seat number
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")

    # print boarding passes
    def make_boarding_cards(self):
        for passenger, seat in sorted(self._passenger_seats()):
            console_card_printer(passenger, seat, self.number(), self.aircraft_model())

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows +1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

# Method to print boarding passes
def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}" \
             f"  Flight: {flight_number}" \
             f"  Seat: {seat}" \
             f"  Aircraft: {aircraft}" \
            " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    card = "\n".join([banner, border, output, border, banner])
    # print out the card
    print(card) 


# TEST: create sample flight
def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus 319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A", "Simon Fisher")
    f.allocate_seat("10A", "Daniel Kahnmen")
    f.allocate_seat("3E", "Srinivas Sundar")
    f.allocate_seat("9F", "Michael Sharkov")
    f.allocate_seat("12B", "Rajat Pradhan")
    f.allocate_seat("1C", "Pammi Singh")
    f.allocate_seat("4D", "Noor Fateh")
    return f


# TEST: for easier printing from command line
def pp(text):
    ppr(text)