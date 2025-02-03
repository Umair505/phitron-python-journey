class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall_obj):
        cls._hall_list.append(hall_obj)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
      show_info = (show_id, movie_name, time)
      self._show_list.append(show_info)

      seats = []
      for _ in range(self._rows):
        seat_row = []
        for _ in range(self._cols):
            seat_row.append(0)
        seats.append(seat_row)

      self._seats[show_id] = seats

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            print("Invalid show ID.")
            return

        for row, col in seat_list:
            if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                print("Invalid seat selected.")
                continue
            if self._seats[show_id][row - 1][col - 1] != 0:
                print("Seat already booked.")
                continue
            self._seats[show_id][row - 1][col - 1] = 1

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        print()
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print("Invalid show ID.")
            return

        print(f"Available seats for show {show_id}:")
        for row in range(self._rows):
            for seat in self._seats[show_id][row]:
             print(seat, end=" ")
            print()


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
hall1.entry_show("002", "SHAITAAN(002)", "9:00 PM")
hall1.entry_show("003", "KUNGFU PANDA(003)", "5:00 PM")

hall1.run()
