class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall_obj):
        cls._hall_list.append(hall_obj)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = []
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._allocate_seats()

        Star_Cinema.entry_hall(self)

    def _allocate_seats(self):
        for _ in range(self._rows):
            seat_row = ['Free'] * self._cols
            self._seats.append(seat_row)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, show_id, seat_list):
        for row, col in seat_list:
            if row not in range(1, self._rows + 1) or col not in range(1, self._cols + 1):
                print("Invalid seat selected.")
                return
            if self._seats[row - 1][col - 1] != 'Free':
                print("Seat already booked.")
                return
            self._seats[row - 1][col - 1] = show_ida

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        print()
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
     if show_id not in [show[0] for show in self._show_list]:
        print("Invalid show ID.")
        return

     print(f"Available seats for show {show_id}:")
     for row in range(self._rows):
        seat_row_str = ""
        for seat in self._seats[row]:
            if seat == 'Free':
                seat_row_str += "0 "
            else:
                seat_row_str += "1 "
        print(seat_row_str)


    def _get_show_by_id(self, show_id):
        for show in self._show_list:
            if show[0] == show_id:
                return show
        print("Invalid show ID.")
        return None

    def run(self):
        print("--------Welcome to Star Cinema--------")
        while True:
            print("\n1. View all shows running")
            print("2. View available seats for a show")
            print("3. Book seats")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_show_list()
            elif choice == '2':
                show_id = input("Enter show ID: ")
                self.view_available_seats(show_id)
            elif choice == '3':
                show_id = input("Enter show ID: ")
                show = self._get_show_by_id(show_id)
                if show:
                    row = int(input("Enter row number: "))
                    col = int(input("Enter column number: "))
                    seat_list = [(row, col)]
                    self.book_seats(show_id, seat_list)
            elif choice == '4':
                print("Thank you for choosing Star Cinema!")
                break
            else:
                print("Invalid choice. Please try again.")


hall1 = Hall(5, 10, 1)
hall1.entry_show("001", "Jawan Maji(001)", "6:00 PM")
hall1.entry_show("002", "The Shawshank Redemption(002)", "9:00 PM")

hall1.run()
