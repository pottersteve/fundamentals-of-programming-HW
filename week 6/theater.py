class Theater:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.seats = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append("O")
            self.seats.append(row)

    def book_seat(self, row, col):
        #Books a seat at the given row and column. Returns True onsuccess, otherwise False
        if self.seats[row][col] == "O":
            self.seats[row][col] = "X"
            return True
        else:
            return False
        
    def cancel_booking(self, row, col):
        #Cancels a booking for the specified location. Returns True on success, otherwise False
        if self.seats[row][col] == "X":
            self.seats[row][col] = "O"
            return True
        else:
            return False
        
    def available_seats(self):
        #Returns the number of available seats
        count = 0
        for row in self.seats:
            for seat in row:
                if seat == "O":
                    count += 1
        return count
